# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
w = 7.292115*10**-5
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year  = float('nan') 
month = float('nan') 
day   = float('nan') 
hour  = float('nan') 
min   = float('nan') 
sec   = float('nan') 
eci_x_km   = float('nan') 
eci_y_km   = float('nan') 
eci_z_km   = float('nan') 



# parse script arguments
if len(sys.argv)==10:
    year  = float(sys.argv[1])
    month = float(sys.argv[2])
    day   = float(sys.argv[3])
    hour  = float(sys.argv[4])
    min   = float(sys.argv[5])
    sec   = float(sys.argv[6])
    eci_x_km  = float(sys.argv[7])
    eci_y_km  = float(sys.argv[8])
    eci_z_km  = float(sys.argv[9])
else:
    print(\
        'Usage: '\
        'python3 year month day hour min sec eci_x_km eci_y_km eci_z_km'\
    )
    exit()

# calculate fractional julian date 
JD =  math.floor(day - 32075 + 1461* (year+4800+(month-14)/12)/4 +367*(month-2-(month-14)/12*12)/12 -3*((year+4900+(month-14)/12)/100)/4)
JD_midnight = JD - 0.5
D_frac = (sec+60*(min+60*hour))/86400
JD_frac = JD_midnight+D_frac
T_uti = (JD_frac-2451545)/36525
theta_GMST = 67310.54841 +(876600*60*60+8640184.812866)*T_uti+0.093104*(T_uti**2)-6.2*(10**-6)*(T_uti**3)
#rad_GMST = theta_GMST*(2*math.pi)/(86400)
#rad_GMST = theta_GMST*(math.pi)
#rad_GMST = .523603
rad_GMST = math.fmod(theta_GMST%86400*w+2*math.pi,2*math.pi)

c = math.cos(-rad_GMST)
s = math.sin(-rad_GMST)

ecef_v = [[c*eci_x_km+(-s)*eci_y_km+0], 
         [s*eci_x_km+c*eci_y_km+0],
         [0+0+eci_z_km]]
ecef_x_km, ecef_y_km, ecef_z_km = ecef_v 

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)

