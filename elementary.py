#!/usr/bin/env python3

# Jacob Anabi and Abby Wheaton
# 2294644 and 2299246
# anabi@chapman.edu and wheaton@chapman.edu
# PHYS220
# CW05

from scipy import constants

"""Module Description
This module includes a Particle object
"""

class Particle(object):
    """Class Description
    The Particle class creates a Particle object, with a .impulse and .move functions

    Attributes:
        mass: the mass of the particle (float)
        position: the position of the particle in the xyz-coordinate system (tuple)
        momentum: the momentum of the particle in the xyz-coordinate system (tuple)
    """

    mass = 0.0

    def __init__(self, x, y, z):
        """Class constructor
        Sets the initial floats of the .position tuple to the three values (x, y, z) passed into the constructor,
        sets the mass to 1.0,
        and sets the initial momentum to (0.0, 0.0, 0.0)
        """
        self.position = (x, y, z)
        mass = 1.0
        self.momentum = (0.0, 0.0, 0.0)

    def impulse(self, px, py, pz):
        """Function docstring
        The .impulse functions increments the .momentum tuple by values px, py, pz

        Args:
            px: increments the x-position of the momentum tuple
            py: increments the y-position of the momentum tuple
            pz: increments the z-position of the momentum tuple
        """
        self.momentum = (self.momentum[0]+px, self.momentum[1]+py, self.momentum[2]+pz)

    def move(self, dt):
        """Function docstring
        The .move functions moves the position function given a dt value, and the mass and momentum of the paricle

        Args:
            dt: a time increment to move the position of the paricle
        """
        self.position = ((self.momentum[0]/self.mass)*dt, (self.momentum[1]/self.mass)*dt, (self.momentum[2]/self.mass)*dt)

class ChargedParticle(Particle):
    charge = 0.0

    def __init__(self, x, y, z):
        super(ChargedParticle, self).__init__(x, y, z)
        self.charge = 1.0

class Electron(ChargedParticle):
    def __init__(self, x, y, z):
        super(Electron, self).__init__(x, y, z)
        self.mass = constants.m_e
        self.charge = -constants.e

class Proton(ChargedParticle):
    def __init__(self, x, y, z):
        super(Proton, self).__init__(x, y, z)
        self.mass = constants.m_p
        self.charge = constants.e