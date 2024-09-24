import numpy as np

temperature_of_cities = [
    [30, 32, 34, 33, 31, 29, 28],
    [22, 24, 25, 26, 27, 28, 29],
    [35, 36, 33, 32, 31, 34, 35]
]


array_of_temperature = np.array(temperature_of_cities)

# a) What is the temperature on day 4 in City B using both the list and NumPy array?
day4_temperature_list = temperature_of_cities[1][3]
day4_temperature_array = array_of_temperature[1, 3]
print(f"Day 4 Temperature in City B using list: {day4_temperature_list}")
print(f"Day 4 Temperature in City B using NumPy Array: {day4_temperature_array}")

# b. What is the average temperature across the week for City C using both the list and NumPy array?
average_temperature_list = sum(temperature_of_cities[2]) / len(temperature_of_cities[2])
average_temperature_array = np.mean(array_of_temperature[2])
print(f"City C temperature average using List: {average_temperature_list}")
print(f"City C temperature average using NumPy Array: {average_temperature_array}")

# c. What is the highest temperature recorded in any city during the week?
highest_temperature_list = max(max(city) for city in temperature_of_cities)
highest_temperature_array = np.max(array_of_temperature)
print(f"The Highest week temperature recorded using List is: {highest_temperature_list}")
print(f"The Highest week temperature recorded using Numpy Array is: {highest_temperature_array}")

# Modify the data to reflect a new temperature for City A on day 7 using both the list and the NumPy array. Verify the change by printing the new data.
temperature_of_cities[0][6] = 27
array_of_temperature[0, 6] = 27
print(f"City A updated temperature list using List: {temperature_of_cities[0]}")
print(f"City A updated temperature list using numpy array: {array_of_temperature[0]}")
