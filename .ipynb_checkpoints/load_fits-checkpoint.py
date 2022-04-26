"""
Reads in a FITS file, displays the image, and displays the position of the
brightest pixel
"""
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def load_fits(fits_file):
  hdulist = fits.open(fits_file)
  data = hdulist[0].data

  plt.style.use('dark_background')
  plt.imshow(data.T, cmap = 'inferno')
  plt.colorbar()
  plt.xlabel('x-pixels (RA)')
  plt.ylabel('y-pixels (Dec)')
  plt.show()

  arg_max = np.argmax(data)
  max_pos = np.unravel_index(arg_max, data.shape)
  return max_pos
