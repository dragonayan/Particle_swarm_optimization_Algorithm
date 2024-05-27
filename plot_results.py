import matplotlib.pyplot as plt

# Read data from results.txt
grid_sizes = []
times_taken = []
with open('results.txt', 'r') as f:
    next(f)  # Skip header
    for line in f:
        grid_size, time_taken = line.strip().split(',')
        grid_sizes.append(int(grid_size.strip()))
        times_taken.append(float(time_taken.strip()))

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(grid_sizes, times_taken, color='blue', label='Completion Time')
plt.plot(grid_sizes, times_taken, color='blue', alpha=0.5)
plt.title('Completion Time vs Grid Size')
plt.xlabel('Grid Size (n)')
plt.ylabel('Completion Time (seconds)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('completion_time_vs_grid_size.png')

# Display the plot
plt.show()
