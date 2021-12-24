"""
Converts coordinates from hours-minutes-seconds to decimal degrees
"""
def hms_to_dec(h, m, s):
  dec_deg = 15 * (h + (m/60) + (s / (60 * 60)))
  return dec_deg
