from Parcial import Parcial
from time import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


n = 14000000

# Sample data
x_values = [i for i in range(1, 6)]  # X-axis values in large numbers
search = [(14000000 * 2 * i) + 3 for i in range(1, 6)]  # First series
delete = [6] * 5  # Second series (constant)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, search, marker='o', linestyle='-', color='b', label="Search")
plt.plot(x_values, delete, marker='s', linestyle='--', color='r', label="Delete")

# Labels and title
plt.xlabel("Elements in terms of N (14M)")
plt.ylabel("Occurrences")
plt.title("Search and Delete Occurrences")
plt.legend()
plt.grid(True)

# Format x-axis to show values in millions
#plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))

# Save and show the plot
plt.savefig("search_delete_plot.png", dpi=300)
plt.show()

"""parcial = Parcial(n)
start_time = time()
s1 = parcial.poblar(1)  # 14,000,000 elementos
s2 = parcial.poblar(2)  # 28,000,000 elementos
s3 = parcial.poblar(3)  # 42,000,000 elementos
s4 = parcial.poblar(4)  # 56,000,000 elementos
s5 = parcial.poblar(5)  # 70,000,000 elementos
end_time = time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")

start_time = time()
print(s1.pop())
end_time = time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")

start_time = time()
print(s2.pop())
end_time = time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")

start_time = time()
print(s3.pop())
end_time = time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")

start_time = time()
print(s4.pop())
end_time = time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")

start_time = time()
print(s5.pop())
end_time = time()
print(f"Execution Time: {end_time - start_time:.6f} seconds")"""