Please open this file in a Jupyter Notebook. You can also download the individual python files. 

The sample FITS file is M51_HST (2).fits. Please put this in same jupyter folder as code. You can find it at this link: 
https://drive.google.com/file/d/1ldSkh9U7gyq3bMqqtjBIDzSt25XFqV07/view?usp=sharing

You are able to run code with any fits file and dynamically adjust scalings and vmin and vmax.

# I suggest subsample of 10 to load FITS faster. 
# You can view the statistics and recommended scalings of the image by clicking on the buttons
# You can change the title, color, and save the image as png. If there is wcs, it should appear in axes of the image

My project aims to create an interactive FITS downloadable png in Jupyter Notebook in which a user can upload their FITS file and is given suggestions on the ideal binning and scaling for a png visual image. The user can then further adjust contrast with sliders and suggestions such as knowing the min and the max value of the image. The project assesses valuable fitting steps if it is a good image. The goal of the project was to complete this process much more quickly than other platforms such as SAO DS9. Stratedgies to do this included making the image smaller, subsmapling over a larger number of pixels while scaling, and quick loading times of the sliders. The program also gives the user insight on the scaling suggestions and relevant statisitcs like mean, median, and standard deviation. This is intended as a quick way to assess how to scale their image and produce a fast result. The only process that still is slow is the initial loading time of the FITS, but after that, the process is quite quick. 
