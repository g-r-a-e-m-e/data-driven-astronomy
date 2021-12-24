"""
Converts coordinates from degrees-arcminutes-arcseconds to decimal degrees
"""
def dms_to_dec(deg, arc_m, arc_s):
  if deg > 0:
    dec_deg = deg + (arc_m / 60) + (arc_s / (60 * 60))
  else:
    dec_deg = -1 * (abs(deg) + (arc_m / 60) + (arc_s / (60 * 60)))

  return dec_deg
