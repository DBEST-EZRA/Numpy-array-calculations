import unittest


class TestTemperatureFunctions(unittest.TestCase):
    def setUp(self):
        self.temperature_of_cities = [
            [30, 32, 34, 33, 31, 29, 28],
            [22, 24, 25, 26, 27, 28, 29],
            [35, 36, 33, 32, 31, 34, 35]
        ]
        self.array_of_temperature = np.array(self.temperature_of_cities)

    def test_day4_temperature_city_b(self):
        day4_temperature_list = self.temperature_of_cities[1][3]
        day4_temperature_array = self.array_of_temperature[1, 3]

        self.assertEqual(day4_temperature_list, 26, "Temperature on Day 4 in City B using list is incorrect")
        self.assertEqual(day4_temperature_array, 26, "Temperature on Day 4 in City B using NumPy array is incorrect")

    def test_average_temperature_city_c(self):
        average_temperature_list = sum(self.temperature_of_cities[2]) / len(self.temperature_of_cities[2])
        average_temperature_array = np.mean(self.array_of_temperature[2])

        self.assertEqual(average_temperature_list, 33.71, "Average temperature in City C using list is incorrect")
        self.assertAlmostEqual(average_temperature_array, 33.71, places=2,
                               msg="Average temperature in City C using NumPy array is incorrect")

    def test_highest_temperature(self):
        highest_temperature_list = max(max(city) for city in self.temperature_of_cities)
        highest_temperature_array = np.max(self.array_of_temperature)

        self.assertEqual(highest_temperature_list, 36, "Highest temperature recorded using list is incorrect")
        self.assertEqual(highest_temperature_array, 36, "Highest temperature recorded using NumPy array is incorrect")

    def test_update_temperature_city_a_day7(self):
        self.temperature_of_cities[0][6] = 27
        self.array_of_temperature[0, 6] = 27
        self.assertEqual(self.temperature_of_cities[0][6], 27, "City A Day 7 temperature not updated correctly in list")
        self.assertEqual(self.array_of_temperature[0, 6], 27,
                         "City A Day 7 temperature not updated correctly in NumPy array")

if __name__ == '__main__':
    unittest.main()
