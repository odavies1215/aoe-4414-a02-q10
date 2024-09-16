# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
# Description: Converts latitude, longitude, and altitude in LLH coordinates to ECEF coordinates.
#
# Parameters:
#  lat_deg: Latitude given in degrees
#  lon_deg: Longitude given in degrees
#  hae_km: Altitude given in kilometers
#
# Output:
#  The ECEF coordinates (x, y, z) in kilometers
#
# Written by Owen
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import math
import sys

# Constants
R_E_KM = 6378.137
e_E = 0.081819221456
r_E_km = 6378.1363

# Helper functions
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0 - ecc * ecc * math.pow(math.sin(lat_rad), 2.0))

# Check and parse script arguments
if len(sys.argv) == 4:
    try:
        lat_deg = float(sys.argv[1])
        lon_deg = float(sys.argv[2])
        hae_km = float(sys.argv[3])
    except ValueError:
        print('Error: Latitude, longitude, and altitude must be numbers.')
        sys.exit()
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    sys.exit()

# Calculate ECEF coordinates
lat_rad = lat_deg * math.pi / 180.0 #converts lattitude measurement from degrees to radians
lon_rad = lon_deg * math.pi / 180.0 #converts longitutde measurement from degrees to radians
denom = calc_denom(e_E, lat_rad)
C_E = r_E_km / denom
S_E = (r_E_km * (1 - e_E * e_E)) / denom
r_x = (C_E + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y = (C_E + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z = (S_E +hae_km) * math.sin(lat_rad)


# Print results
print(f'ECEF coordinates (km):')
print(f'X: {r_x:.6f}')
print(f'Y: {r_y:.6f}')
print(f'r: {r_z:.6f}')

