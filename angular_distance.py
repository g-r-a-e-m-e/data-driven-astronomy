"""
Calculates the angular distance between two objects given right ascension and
declination in degrees for both objects.
"""
import numpy as np

def angular_distance(ra1, dec1, ra2, dec2):
  r1 = np.radians(ra1)
  d1 = np.radians(dec1)
  r2 = np.radians(ra2)
  d2 = np.radians(dec2)

  a = np.sin(abs(d2 - d1) / 2)**2
  b = np.cos(d1) * np.cos(d2) * (np.sin(abs(r1 - r2) / 2)**2)
  d = 2 * np.arcsin(np.sqrt(a + b))
  return np.degrees(d)
