import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
# print(pd.DataFrame({ 'City name': city_names, 'Population': population }))

# data_file_location = "https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv"
# california_housing_data_frame = pd.read_csv(data_file_location, sep=",")
# print(california_housing_data_frame.describe())

# print(california_housing_data_frame.head())

# california_housing_data_frame.hist('housing_median_age')
# plt.show()

cities = pd.DataFrame({'City name': city_names, 'Population': population})
# print(type(cities['City name']))
# print(cities['City name'])

cities['val'] = population.apply(lambda val: val > 1000000)
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
# print(cities)

# Exercise 1
# Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:
# The city is named after a saint.
# The city has an area greater than 50 square miles
cities['saint_and_big'] = (cities['City name'].str.slice(0, 3) == 'San') & (cities['Area square miles'] > 50)
# cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities)

cities.reindex(np.random.permutation(cities.index))
print(cities)


# Exercise 2
# The reindex method allows index values that are not in the original DataFrame's index values.
# Try it and see what happens if you use such values! Why do you think this is allowed?
print(cities.reindex([53, 106, 972]))
print(cities)
