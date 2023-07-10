import math
import constants


class Particle:
    def __init__(self, name, pos, vel, mass):
        self.name = name
        self.pos = pos
        self.velocity = vel
        self.mass = mass

    def update(self, particles, dt):
        for other in particles:
            if self != other:
                dx = other.pos[0] - self.pos[0]
                dy = other.pos[1] - self.pos[1]
                distance = math.sqrt(dx**2 + dy**2)

                force = (constants.G * self.mass * other.mass) / (distance**2)

                acceleration_x = force * dx / distance  # Fx
                acceleration_y = force * dy / distance  # Fy

                self.velocity[0] += acceleration_x * dt / self.mass
                self.velocity[1] += acceleration_y * dt / self.mass

        # Update position based on velocity
        self.pos[0] += self.velocity[0] * dt
        self.pos[1] += self.velocity[1] * dt

    def check_collision(self, particles):
        for particle in particles:
            if particle != self:
                dx = particle.x - self.x
                dy = particle.y - self.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance <= self.radius + particle.radius:
                    self.merge_particles(particle)
                    particles.remove(particle)

    def merge_particles(self, particle):
        # inelastic collision handling
        combined_mass = self.mass + particle.mass
        self.x = (self.x * self.mass +
                  particle.x * particle.mass) / combined_mass
        self.y = (self.y * self.mass +
                  particle.y * particle.mass) / combined_mass
        self.mass = combined_mass
        self.velocity_x = (self.velocity_x * self.mass +
                           particle.velocity_x * particle.mass) / combined_mass
        self.velocity_y = (self.velocity_y * self.mass +
                           particle.velocity_y * particle.mass) / combined_mass
