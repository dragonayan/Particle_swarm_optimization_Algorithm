import numpy as np
import random
import time
import os
import json

def generate_random_path(grid_size, source, destination, obstacles):
    path = [source]
    current_position = source
    while current_position != destination:
        x, y = current_position
        if x < grid_size[0] - 1:
            x += random.choice([0, 1])
        if y < grid_size[1] - 1:
            y += random.choice([0, 1])
        new_position = (x, y)
        if new_position not in obstacles and new_position not in path:
            path.append(new_position)
            current_position = new_position
    return path

def fitness_function(path, destination):
    if path[-1] != destination:
        return float('inf')  # Invalid path
    return len(path)  # Shorter paths are better

def particle_swarm_optimization(n, m, obstacles, start, end, num_particles=30, num_iterations=100):
    grid_size = (n, m)
    source = tuple(start)
    destination = tuple(end)

    particles = []
    for _ in range(num_particles):
        path = generate_random_path(grid_size, source, destination, obstacles)
        velocity = [(0, 0) for _ in range(len(path))]
        particles.append({'position': path, 'velocity': velocity, 'best_position': path, 'best_fitness': fitness_function(path, destination)})

    global_best_particle = min(particles, key=lambda p: p['best_fitness'])
    global_best_position = global_best_particle['best_position']
    global_best_fitness = global_best_particle['best_fitness']

    for iteration in range(num_iterations):
        for particle in particles:
            fitness = fitness_function(particle['position'], destination)
            if fitness < particle['best_fitness']:
                particle['best_fitness'] = fitness
                particle['best_position'] = particle['position']
            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle['position']

        for particle in particles:
            new_velocity = []
            new_position = [source]
            for i in range(1, min(len(particle['position']), len(global_best_position))):
                inertia = np.array(particle['velocity'][i]) * inertia_weight
                cognitive = cognitive_coefficient * random.random() * (np.array(particle['best_position'][i]) - np.array(particle['position'][i]))
                social = social_coefficient * random.random() * (np.array(global_best_position[i]) - np.array(particle['position'][i]))
                new_vel = inertia + cognitive + social
                new_pos = np.array(particle['position'][i]) + new_vel
                new_velocity.append(tuple(new_vel.astype(int)))
                new_position.append(tuple(new_pos.astype(int)))

            particle['velocity'] = [(0, 0)] + new_velocity
            particle['position'] = new_position + [destination] if new_position[-1] != destination else new_position

    return global_best_position

# PSO parameters
inertia_weight = 0.5
cognitive_coefficient = 2.0
social_coefficient = 2.0

# Process test cases from 'testcases' directory
completion_times = []
test_case_files = [f for f in os.listdir('testcases') if f.endswith('.json')]

for test_case_file in test_case_files:
    with open(f'testcases/{test_case_file}', 'r') as f:
        test_case = json.load(f)
    
    start_time = time.time()
    best_path = particle_swarm_optimization(
        test_case["n"],
        test_case["m"],
        [tuple(obstacle) for obstacle in test_case["obstacles"]],
        test_case["start"],
        test_case["end"]
    )
    end_time = time.time()
    completion_time = end_time - start_time
    completion_times.append((test_case["n"], test_case["m"], completion_time))
    print(f"Test Case: {test_case_file}, Grid Size: {test_case['n']}x{test_case['m']}, Completion Time: {completion_time:.4f} seconds")
    print("Best Path Found:", best_path)

# Additional test cases
additional_test_cases = [
    {
        "n": 14,
        "m": 14,
        "obstacles": [
            [1, 0],
            [2, 2],
            [3, 4],
            [4, 6],
            [5, 8],
            [6, 10]
        ],
        "start": [0, 0],
        "end": [13, 13]
    },
    {
        "n": 15,
        "m": 15,
        "obstacles": [
            [0, 1],
            [1, 3],
            [2, 5],
            [3, 7],
            [4, 9],
            [5, 11]
        ],
        "start": [0, 0],
        "end": [14, 14]
    }
]

for idx, test_case in enumerate(additional_test_cases, start=1):
    start_time = time.time()
    best_path = particle_swarm_optimization(
        test_case["n"],
        test_case["m"],
        [tuple(obstacle) for obstacle in test_case["obstacles"]],
        test_case["start"],
        test_case["end"]
    )
    end_time = time.time()
    completion_time = end_time - start_time
    completion_times.append((test_case["n"], test_case["m"], completion_time))
    print(f"Additional Test Case {idx}: Grid Size: {test_case['n']}x{test_case['m']}, Completion Time: {completion_time:.4f} seconds")
    print("Best Path Found:", best_path)

# Save results to 'results.txt'
with open('results.txt', 'w') as f:
    f.write("Grid Size, Time Taken (seconds)\n")
    for n, m, time_taken in completion_times:
        grid_size = n 
        f.write(f"{grid_size}, {time_taken:.4f}\n")

print("\nResults saved to 'results.txt'.")
