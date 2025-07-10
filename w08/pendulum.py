import math

length = float(input("Enter the length of a pendulum: "))

time = (math.pi * 2) * (math.sqrt(length / 9.81))

print(f"Time (seconds): {time:.2f}")