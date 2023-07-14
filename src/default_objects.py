from particle import Particle
import constants
import math

sun_pos = [constants.width / 2, constants.height / 2]
sun_vel = [0, 0]
sun_displayed = 6

earth_distance_to_sun = 1 * constants.AU  # distance to sun
earth_pos = [earth_distance_to_sun, 0]
earth_vel = [
    0, -math.sqrt((constants.G * constants.sun_mass) / earth_distance_to_sun)
]
earth_displayed = 2


def get_sun():
    return Particle('Sun', sun_pos, sun_vel, constants.sun_mass, sun_displayed)


def get_earth():
    return Particle('Earth', earth_pos, earth_vel, constants.earth_mass,
                    earth_displayed)
