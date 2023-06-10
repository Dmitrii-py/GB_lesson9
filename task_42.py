""" Задача 42:
Узнать какая максимальная households в зоне минимального значения population.
"""
import pandas as pd

db = pd.read_csv('sample_data/california_housing_test.csv')
res = db[db["population"] == db["population"].min()]["households"].agg(['max'])  # .max()
print(f"Максимальная households в зоне минимального значения population: \n{round(res, 2)}")
