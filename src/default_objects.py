from particle import Particle
import constants
import math

sun_mass = 1.989 * math.pow(10, 30)  # kg 
sun_pos = [constants.width / 2, constants.height / 2] 
sun_vel = [0, 0]

earth_mass = 5.972 * math.pow(10, 24) # kg
earth_distance_to_sun = 1 * constants.AU # distance to sun
earth_pos = [earth_distance_to_sun, 0]
earth_vel = [0, -math.sqrt((constants.G * sun_mass) / earth_distance_to_sun)]

def get_sun():
    return Particle("Sun", sun_pos, sun_vel, sun_mass)

def get_earth():
    return Particle("Earth", earth_pos, earth_vel, earth_mass)
