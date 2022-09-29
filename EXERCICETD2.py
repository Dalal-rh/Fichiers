import numpy as np
#les paramètres selon td2
ahe=0.03412
bhe= 0.02370
#les données opératoires
T=500
P=200
#a corriger
R=0.082
d=P*bhe+R*T
volume = [P,-d, ahe,-ahe*bhe]
sol=np.roots(volume)
print("volume = ",sol[0].real)



