# Problem 1

# Constants
FNormal = 216000  # Sea level static
CL_0 = 0.2
CD_0 = 0.016
S = 125
dC_Ldalpha = 5.7296  # rad^-1
epsilon = 0.048
TSFC = 3.553E-5
VE = 128.6  # Equivalent airspeed

# 1. Set the altitude ℎ(t) equal to 0 m, i.e., sea-level.
h = 0

# 2. Set the true airspeed V_T(t) equal to 128.6 m/s.
V_t = 128.6

# 3. Compute the thrust F_N(t) at sea-level and 128.6 m/s.
P = 101325  # Static pressure
p = 1.225  # density of air at sea level
# Look for dynamic pressure
q = 1/2 * p * VE ** 2  # dynamic pressure, equivalent airspeed used
P_0 = P + q # Stagnation P =  static P + dynamic( 1/2pv^2)
F = FNormal * (P / P_0)
print(F)

