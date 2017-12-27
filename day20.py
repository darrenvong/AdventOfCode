"""
Solution for Day 20 of Advent of Code 2017.

Problem: Particle Swarm

Part 1: Given that each particle updates by applying the velocity and acceleration,
which particle will be closest to the origin in the long run?

Part 2: How many particles are left over after all collisions occurred?
"""
import re
import numpy as np

def parse_particles_info(name):
    line_re = (r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, "
               r"a=<(-?\d+),(-?\d+),(-?\d+)>")
    line_pat = re.compile(line_re)
    particles = np.empty((1000, 3, 3), dtype=np.int32)

    with open(name) as f:
        for i, line in enumerate(f):
            particle_info = list(map(int, line_pat.search(line).groups()))
            particle = np.array([[particle_info[j], particle_info[j + 1], particle_info[j + 2]]
                                 for j in range(0, 9, 3)], np.int32)
            particles[i] = particle
    return particles

def get_closest_particle(particles):
    # get the magnitude (size) of each particles' given vectors (p, v, a)
    particles_collapsed = np.sum(np.absolute(particles), axis=2)

    # sort by a, then v, then p, since particle with lowest acceleration/velocity
    # will be closest to origin in the long run (i.e. particles which are closest to
    # stationery should be closest to origin)
    # Somewhat counter-intuitive that the sort "appears backwards"
    indexed_particles = enumerate(particles_collapsed)
    position_sort = sorted(indexed_particles, key=lambda x: x[1][0])
    velocity_sort = sorted(position_sort, key=lambda x: x[1][1])
    acc_sort = sorted(velocity_sort, key=lambda x: x[1][2])

    return acc_sort[0][0]

def update_particles(particles):
    # Updates the velocity of each particle
    particles[:, 1, :] += particles[:, 2, :]
    # Updates the position of each particle
    particles[:, 0, :] += particles[:, 1, :]

    # Get information such as number (count) of particles in certain 3D coordinate.
    _, indices, counts = np.unique(particles[:, 0, :], return_index=True, return_counts=True, axis=0)
    return indices, counts

def get_num_particle_after_time(time, particles):
    num_particles_left = 1000
    same_num_iterations = 0
    threshold = 20
    for _ in range(time):
        unique_inds, counts = update_particles(particles)
        # If a coordinate has count > 1, then all particles at that coordinate is
        # colliding, so we only want the indices (particle nums) situated in a
        # unique coordinate at time t
        non_collided_inds = unique_inds[counts == 1]

        particles = particles[non_collided_inds]

        # number of particles remained the same level after a threshold num of seconds,
        # => converging so return, otherwise update number of particles left
        if same_num_iterations == threshold:
            return num_particles_left
        elif num_particles_left == particles.shape[0]:
            same_num_iterations += 1
        else:
            num_particles_left = particles.shape[0]

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    particles = parse_particles_info("day20_input.txt")
    print(f"Particle {get_closest_particle(particles)} will stay closest to the origin.")
    print()

    print("=" * 15, "Part 2", "=" * 15)
    print(f"{get_num_particle_after_time(100, particles)} particles left after all "
          "collisions resolved.")
