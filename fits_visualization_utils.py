import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, Dropdown, Text, Button, interactive, VBox
from fits_plotter import FitsPlotter

def create_widgets(data, wcs):
    vmin_slider = FloatSlider(min=np.min(data)-20, max=np.max(data), step=0.1, description='vmin', value=np.min(data), layout={'width': '80%'})
    vmax_slider = FloatSlider(min=np.min(data), max=np.max(data)+20, step=0.1, description='vmax', value=np.max(data), layout={'width': '80%'})
    subsample_slider = FloatSlider(min=1, max=20, step=1, description='Subsample Factor', value=1, layout={'width': '80%'})
    scaling_dropdown = Dropdown(
        options=['linear', 'log', 'sqrt', 'sinh', 'power:2', 'power:3'], 
        value='linear',
        description='Scaling Method:'
    )
    x_axis_input = Text(value='Default X Coordinates', description='X Axis Label:')
    y_axis_input = Text(value='Default Y Coordinates', description='Y Axis Label:')
    title_input = Text(value='Title', description='Plot Title:')
    save_filename = Text(value='plot.png', description='Filename:')
    return vmin_slider, vmax_slider, subsample_slider, scaling_dropdown, x_axis_input, y_axis_input, title_input, save_filename

def create_plot(vmin, vmax, subsample_factor, scaling, x_label, y_label, plot_title, cmap, data, wcs):
    fits_plotter = FitsPlotter(data, wcs=wcs)
    fits_plotter.plot_image(vmin, vmax, scaling, subsample_factor=int(subsample_factor), cmap=cmap, x_axis=x_label, y_axis=y_label, title=plot_title)

def display_stats(data, wcs):
    fits_plotter = FitsPlotter(data, wcs=wcs)
    fits_plotter.display_statistics()

def save_plot(filename, fits_plotter):
    try:
        print("Saving plot...")
        if fits_plotter.fig is not None:
            if not filename:
                filename = "plot.png"
            print("Filename:", filename)
            fits_plotter.save_plot(filename)
            print("Plot saved successfully.")
        else:
            print("No plot to save.")
    except Exception as e:
        print("Error saving plot:", e)

# Define a function to display suggested scalings
def display_suggested_scalings(data, wcs):
    fits_plotter = FitsPlotter(data, wcs=wcs)
    suggested_scalings = fits_plotter.evaluate_scaling_methods()
    if suggested_scalings:
        print("Top three suggested scaling methods:")
        for i, (method, suggested_vmin, suggested_vmax) in enumerate(suggested_scalings):
            print(f"{i+1}. Scaling Method: {method}, Suggested vmin: {suggested_vmin}, Suggested vmax: {suggested_vmax}")

# Define the interactive plot function
def interactive_plot(data, wcs):
    widgets = create_widgets(data, wcs)
    interactive_plot = interactive(create_plot, vmin=widgets[0], vmax=widgets[1], subsample_factor=widgets[2], scaling=widgets[3],
                                   x_label=widgets[4], y_label=widgets[5], plot_title=widgets[6], cmap=plt.colormaps(), data=data, wcs=wcs)
    stats_button = Button(description="Display Statistics")
    display_scalings_button = Button(description="Display Scalings")
    save_button = Button(description="Save Plot")
    save_button.on_click(lambda _: save_plot(widgets[7].value, fits_plotter))  # Pass the filename and fits_plotter instance
    stats_button.on_click(lambda _: display_stats(data, wcs))
    display_scalings_button.on_click(lambda _: display_suggested_scalings(data, wcs))
    return VBox([interactive_plot, stats_button, display_scalings_button, widgets[7], save_button])

# Usage:
# interactive_plot(data, wcs)
