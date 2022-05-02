import numpy as np

#B = demi largeur 
#c = hauteur
#r = rayon de l arc

class PointedArch:
    '''
    The most basic PointedArch

    Paramameters:
        B (number): half-width of the arch
        c (number): height of the arch
        r (number): radii of the circles used for the arch

    '''

    def __init__(self, B : float, c : float, r : float):
        '''
        Initiates the parameters a,b of the arch using the caracteristics
        '''
        self.B, self.c, self.r = B, c, r

        j = -B**3 + np.sqrt((-c**2)*(B**2 + c**2)*(B**2 + c**2 - 4*r**2)) - B*(c**2)
        self.a = j/(2*(B**2 + c**2))

        k = -B*np.sqrt((-c**2)*(B**2 + c**2)*(B**2 + c**2 - 4*r**2)) + (B**2)*(c**2) + c**4
        self.b = k/(2*c*(B**2 + c**2))

    def __call__(self, x:np.ndarray):
        '''
        Returns the Ys of an Arch given a set of Xs

        Parameters:
            x (np.ndarray of numbers): a numpy array containing the abscisses to compute the ordinates of

        Returns:
            y (np.ndarray of numbers): a numpy array containing the computed ordinates
        '''
        x = -np.abs(x)
        y = np.zeros_like(x)
        for idx, e in np.ndenumerate(x):
            if(abs(e) <= self.B):
                y[idx] = self.b + np.sqrt(self.r**2 - (e - self.a)**2)
        return y

class RotatedArch(PointedArch):
    '''
    A wrapper for rotated 3d archs around the z axis

    Paramameters:
        B (number): half-width of the arch
        c (number): height of the arch
        r (number): radii of the circles used for the arch
        theta (number): angle the arch is rotated
    '''
    def __init__(self, B,c,r,theta):
        super().__init__(B, c, r)
        self.theta = theta
    def __call__(self, X, Y):
        '''
        Returns the Ys of an Arch given a set of Xs

        Parameters:
            X (np.ndarray of numbers): a numpy array containing the abscisses to compute the heights of
            Y (np.ndarray of numbers): a numpy array containing the ordinates to compute the heights of

        Returns:
            Z (np.ndarray of numbers): a numpy array containing the computed heights
        '''
        Xr = np.cos(-self.theta) * X + np.sin(-self.theta)*Y #rotate 
        return super().__call__(Xr)

if __name__ == "__main__":
    arch = PointedArch(50, 75, 100)