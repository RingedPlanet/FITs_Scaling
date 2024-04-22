import matplotlib.pyplot as plt
import numpy as np

class FitsPlotter:
    def __init__(self, data, wcs=None):
        self.data = data
        self.wcs = wcs
        self.fig = None
        self.ax = None

    def plot_image(self, vmin, vmax, scaling='linear', subsample_factor=1, figsize=(8, 8), cmap='gray_r',
                   x_axis='Default X Coordinates', y_axis='Default Y Coordinates', title='Title'):
        if self.data is not None:
            # Subsample the data
            data_subsampled = self.data[::subsample_factor, ::subsample_factor]

            # Apply scaling to the data
            if scaling == 'log':
                data_scaled = np.where(data_subsampled > 0, np.log(data_subsampled), 0)
            elif scaling == 'sqrt':
                data_scaled = np.sqrt(data_subsampled)
            elif scaling == 'sinh':
                data_scaled = np.sinh(data_subsampled)
            elif scaling == 'linear':
                data_scaled = data_subsampled
            elif scaling.startswith('power'):
                power = float(scaling.split(':')[1])
                data_scaled = np.power(data_subsampled, power)
            else:
                raise ValueError('Invalid scaling method')

            if self.fig is None or self.ax is None:
                self.fig, self.ax = plt.subplots(figsize=(5, 5))
                if self.wcs:
                    self.ax = plt.subplot(projection=self.wcs)

            self.ax.clear()
            data_rotated = np.rot90(data_scaled, 2)
            data_rotated[data_rotated == 0] = np.nan

            im = self.ax.imshow(data_rotated, cmap=cmap, vmin=vmin, vmax=vmax)
            self.ax.set_title(title)
            self.ax.set_xlabel(x_axis)
            self.ax.set_ylabel(y_axis)
            plt.colorbar(im, ax=self.ax)
            plt.show()

    def evaluate_scaling_methods(self):
        if self.data is not None:
            # Compute data statistics
            data_min = np.nanmin(self.data)
            data_max = np.nanmax(self.data)
            data_mean = np.nanmean(self.data)
            data_std = np.nanstd(self.data)

            # Evaluate each scaling method
            scaling_methods = ['linear', 'log', 'sqrt', 'sinh']
            scaling_results = {}
            for scaling_method in scaling_methods:
                if scaling_method == 'linear':
                    score = 1
                    suggested_vmin = data_min
                    suggested_vmax = data_max
                else:
                    # Apply the scaling method to the data
                    if scaling_method == 'log':
                        scaled_data = np.where(self.data > 0, np.log(self.data), 0)
                    elif scaling_method == 'sqrt':
                        scaled_data = np.sqrt(self.data)
                    elif scaling_method == 'sinh':
                        scaled_data = np.sinh(self.data)
                    # Compute the score based on data distribution
                    scaled_min = np.nanmin(scaled_data)
                    scaled_max = np.nanmax(scaled_data)
                    scaled_mean = np.nanmean(scaled_data)
                    scaled_std = np.nanstd(scaled_data)
                    # A better score will be better scaling
                    score = data_std / scaled_std
                    # Suggested vmin and vmax values
                    suggested_vmin = scaled_min - 0.1 * (scaled_max - scaled_min)
                    suggested_vmax = scaled_max + 0.1 * (scaled_max - scaled_min)
                scaling_results[scaling_method] = {'score': score, 'suggested_vmin': suggested_vmin,
                                                   'suggested_vmax': suggested_vmax}
            sorted_methods = sorted(scaling_results, key=lambda x: scaling_results[x]['score'], reverse=True)
            top_three_results = [(method, scaling_results[method]['suggested_vmin'],
                                  scaling_results[method]['suggested_vmax']) for method in sorted_methods[:3]]
            return top_three_results
        else:
            return None

    def display_statistics(self):
        if self.data is not None:
            print("Mean:", np.nanmean(self.data))
            print("Median:", np.nanmedian(self.data))
            print("Standard Deviation:", np.nanstd(self.data))
        else:
            print("No data available to compute statistics.")

    def save_plot(self, filename):
        if self.fig is not None:
            self.fig.savefig(filename)
