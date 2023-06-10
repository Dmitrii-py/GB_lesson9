"""
Задача 40: Работать с файлом california_housing_train.csv,
который находится в папке sample_data. Определить среднюю стоимость дома,
где кол-во людей от 0 до 500 (population).
"""
import pandas as pd

db = pd.read_csv('sample_data/california_housing_test.csv')
res = db[db["population"] < 501]["median_house_value"].mean()
print(f"Средняя стоимость дома: {round(res, 2)}")
