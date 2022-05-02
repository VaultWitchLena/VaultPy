import numpy as np
from matplotlib import pyplot as plt

from VaultPy import PointedArch, RotatedArch

fig = plt.figure()
ax3d = fig.add_subplot(projection="3d")

#RotatedArch
B,c,r = 50,50,500
profondeur = 100
x,y = np.linspace(-B, 0, 501), np.linspace(-profondeur/2, profondeur/2,501)
X,Y = np.meshgrid(x,y)

Z = np.zeros_like(X)

for i in range(0,5):
    arch = RotatedArch(B, c, r, i*np.pi/5)
    Z = np.maximum(Z,arch(X,Y))
    
R2 = X**2 + Y**2
limit = (R2 <= 50**2).astype(int)

Z *= limit

dico = {(X[i][j], Y[i][j]): Z[i][j] for j in range(501) for i in range(501)}

ax3d.plot_surface(X,Y,Z)
ax3d.set_xlim3d(-50,50)
ax3d.set_ylim3d(-50,50)

r = np.linspace(0,50,101)

angle = np.pi/10

x_line = np.around(-r*np.sin(angle),0)
y_line = np.around(-r*np.cos(angle),0)
z_line = [dico[x_line[i], y_line[i]] for i in range(101)]

ax3d.plot(x_line, y_line, z_line, zorder=3)

plt.show()

output = np.array([[x_line[i], y_line[i], z_line[i]] for i in range(101)])
print(output)
