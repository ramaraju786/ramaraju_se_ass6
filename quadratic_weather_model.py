def quadratic_weather_model(t):
    # Example quadratic equation: T = a*t^2 + b*t + c
    a, b, c = 0.05, -0.3, 25   # you can change values
    return a * t**2 + b * t + c

print("=== WATERFALL MODE ===")
for hour in range(0, 25, 6):  # every 6 hours
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

print("\n=== ITERATIVE MODE ===")
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    for hour in range(0, 25, 12):  # every 12 hours
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")

print("\n=== AGILE MODE ===")
times_to_check = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    for t in times_to_check:
        temp = quadratic_weather_model(t)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
