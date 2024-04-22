Please open the main driver (titled as Julia Levy Final Astr 330 Project) in a Jupyter Notebook. You can download the individual python files to import them. 

The sample FITS file is M51_HST (2).fits. Please put this in same jupyter folder as code. You can find it at this link: 
https://drive.google.com/file/d/1ldSkh9U7gyq3bMqqtjBIDzSt25XFqV07/view?usp=sharing

You are able to run code with any fits file and dynamically adjust scalings and vmin and vmax and have a dropdown menu for scaling types. The image will then quickly, dynamically render below. 

# Please be patient with the initial loading time of the FITs file. After that, things should load at a much faster rate. It may take a little time to adjust color, scaling, and output the buttons. 
# I suggest subsample of 10 to load FITS faster. 
# You can view the statistics and recommended scalings of the image by clicking on the buttons under the image
# You can change the title, color, and save the image as png to your Jupyter Notebook file. 

My project aims to create an interactive FITS downloadable png in Jupyter Notebook in which a user can upload their FITS file and is given suggestions on the ideal binning and scaling for a png visual image. The user can then further adjust contrast with sliders and suggestions such as knowing the min and the max value of the image. The project assesses valuable fitting steps if it is a good image. The goal of the project was to complete this process much more quickly than other platforms such as SAO DS9. Strategies to do this included making the image smaller, subsmapling over a larger number of pixels while scaling, and quick loading times of the sliders. The program also gives the user insight on the scaling suggestions and relevant statisitcs like mean, median, and standard deviation. This is intended as a quick way to assess how to scale their image and produce a fast result. The only process that still is slow is the initial loading time of the FITS, but after that, the process is quite quick. 
