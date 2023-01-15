import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QComboBox, QFileDialog, QLabel


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
import numpy as np
from astropy.io import fits

def averageStack(list_img):
    # Calculate the mean and standard deviation of the list 
    mean = np.mean(list_img, axis=0)
    std = np.std(list_img, axis=0)
    
    # create a new list for modified images
    modified_list_img = []
    
    # Calculate the z-score of each pixel in the image
    for img in list_img:
        z = (img - mean) / std
        # Set pixels with a z-score greater than 3 to nan
        img = img.astype(float)
        img[z > 3] = np.nan
        # Append the modified image to the list
        modified_list_img.append(img)
    
    # Calculate the mean of the modified list of images without nan values
    avg = np.nanmean(modified_list_img, axis=0)
    
    return avg


def medianStack(list_img):
    #stacking method by median
    avg= np.median(list_img, axis=0)
    return avg





class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.files = []
        
        
        #set a background as a label of the app
        self.label = QLabel(self)
        self.label.setStyleSheet("QLabel { border-image: url(./img/background.jpg) stretch; }")
        
        # Set the size and position of the QLabel to cover the entire background
        self.label.setGeometry(0, 0, 800, 600)
        
        # Create an instance of Figure and FigureCanvas which allow to put the matplotlib result in the app
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)

        

        #set the title and the size of the window
        self.setWindowTitle("Fits-Stacking")
        self.resize(800,600)
        
        #browse files button
        self.button = QPushButton("Browse Files")
        self.button.clicked.connect(self.press_button)
        
        #combo box which allow to select the stacking method
        self.combo = QComboBox()
        self.combo.addItems(["Moyenne","Mediane"])
        
        #starting button
        self.confirmButton = QPushButton("Starting process")
        self.confirmButton.clicked.connect(self.confirm_method)
        
        #save button
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.save_image)
        
        #layout of the application
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.combo)
        layout.addWidget(self.confirmButton)
        layout.addWidget(self.saveButton)
        self.setLayout(layout)
        
    def press_button(self):
        folder_name = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_name:
            # Get a list of all the files in the selected folder
            self.files = [os.path.join(folder_name, f) for f in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, f))]

        
    def confirm_method(self):
        # Remove the FigureCanvas widget from the layout
        self.remove_canvas()
        stacking_method = self.combo.currentText()
        if stacking_method == "Moyenne":
            # Perform the mean stacking process
            list_img = []
            for f in self.files:
                # Load the image file and add it to the list
                img = fits.getdata(f)
                list_img.append(img)
            result = averageStack(list_img)
            ax = self.fig.add_subplot(111)
            ax.imshow(result, cmap='gray')
            ax.axis('off')
            self.canvas.draw()

        if stacking_method == "Mediane":
            # Perform the median stacking process
            list_img = []
            for f in self.files:
                # Load the image file and add it to the list
                img = fits.getdata(f)
                list_img.append(img)
            result = medianStack(list_img)
            ax = self.fig.add_subplot(111)
            ax.imshow(result, cmap='gray')
            ax.axis('off')
            self.canvas.draw()
            
        # Add the FigureCanvas widget to the layout
        self.add_canvas()
            
    #add the image method
    def add_canvas(self):
        layout = self.layout()
        layout.addWidget(self.canvas)
        
    #remove the image method
    def remove_canvas(self):
        layout = self.layout()
        layout.removeWidget(self.canvas)
        
    def save_image(self):
        # Open a file dialog to select the location and name of the saved image
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "FITS Files (*.fits)")
        if file_name:
            # Get the image data from the Figure and convert it to an array
            data = self.fig.gca().images[0].get_array()
            data = data.filled()

            # Create a new FITS file and save the image data
            hdu = fits.PrimaryHDU(data)
            hdu.writeto(file_name)


        


        
        

#loading the app
app = QApplication.instance() 
if not app:
    app = QApplication(sys.argv)
    
fen = Window()


fen.show()

app.exec_()

