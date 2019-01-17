#heat exchanger code

#entering information about the heat exchanger
Tin_Celsius = input("Enter the inlet temperature (in C): ")
q = input("Enter the expected heat flow rate (in Watts): ")
Tout_Celsius = input("Enter the desired outlet temperature (in C): ")
D = input("Enter the diameter of your pipe (in m): ")
x = 'n'
while x != 'o' and x != 'w':
    x = input("Enter your cooling fluid (w for water and o for engine oil): ")

Tin = float(Tin_Celsius) + 273
Tout = float(Tout_Celsius) + 273

#additional variables
T_avg = (Tin + Tout) / 2
deltaT = Tout - Tin;
Cp_avg = 0
p_avg = 0
#data for water and oil
H2O = [[280,290,300,310,320,330,340,350,360,370], [1000,1/.001001,1/.001003,1/.001007,1/.001007,1/.001011,1/.001016,1/.001021,1/.001027,1/.001034,1/.001041],[4198,4184,4179,4178,4180,4184,4188,4195,4203,4214]]
Oil = [[280,290,300,310,320,330,340,350,360,370],[895.31,890,884.1,877.8,871.8,865.8,859.9,853.9,847.8,841.8],[1827,1868,1909,1951,1993,2035,2076,2118,2161,2206]]
print(H2O[1][0])
print(H2O[2][0])

i=0
while H2O[0][i] < T_avg:
    if i>= len(H2O[0]):
        break
    i=i+1
b = i - 1

if b+1 > len(Oil[0]) or b==0:
    print('Temperature out of range')
elif x == 'o':
    p_avg = (Oil[1][b] + (T_avg - Oil[0][b])*(Oil[1][b+1] - Oil[1][b]) / 10)
    Cp_avg = (Oil[2][b] + (T_avg - Oil[0][b])*(Oil[2][b+1] - Oil[2][b]) / 10)
else:
    p_avg = (H2O[1][b] + (T_avg - H2O[0][b])*(H2O[1][b+1] - H2O[1][b]) / 10)
    Cp_avg = (H2O[2][b] + (T_avg - H2O[0][b])*(H2O[2][b+1] - H2O[2][b]) / 10)

#equations
#Cc*deltaT = q
#q/deltaT/Cp = mdot, q/(deltaT * Cp *pi/4 * d^2 * p) = v
v = 4 * float(q) / (deltaT * Cp_avg * 3.14159 * p_avg * float(D) * float(D))
#output information of the heat exchanger
print("Average density heat of cooling fluid: " + str(p_avg) + " kg/m^3")
print("Average specific heat of cooling fluid: " + str(Cp_avg) + " J/kg*K")
print("The flow velocity of cooling liquid should be:  " + str(v) + " m/s")
