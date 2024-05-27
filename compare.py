import matplotlib.pyplot as plt

# ACO data
aco_grid_sizes = [10, 11, 12, 13, 14, 15]
aco_times = [0.3526, 0.3964, 0.5089, 0.5159, 0.5454, 0.5968]

# GA data
hexagonal_grid_sizes = [10, 11, 12, 13, 14, 15, 16]
hexagonal_times = [0.17660856246948242, 0.21645021438598633, 0.360029935836792, 0.32512617111206055, 0.3001677989959717, 0.3502769470214844, 0.5424623489379883]

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(aco_grid_sizes, aco_times, marker='o', label='ACO')
plt.plot(hexagonal_grid_sizes, hexagonal_times, marker='o', label='GA')

plt.xlabel('Grid Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Comparison of Genetic Algorithm and Ant Colony Optimization')
plt.legend()

plt.grid(True)
plt.show()
