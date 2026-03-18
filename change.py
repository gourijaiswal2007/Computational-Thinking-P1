data = [[10, 20], [30, 40], [50, 60]]

# Create a shallow copy
update_data = list(data)

# Modify inner element
update_data[1][1] = 99

# Print both
print("Original data:", data)
print("Updated data:", update_data)