import pandas as pd
import numpy as np

categories = ["Одежда", "Продукты", "Электроника", "Мебель"]
warehouses = ["Склад_А", "Склад_В", "Склад_С"]
names = [f"Товар_{i}" for i in range(1, 31)]

names_categories = {}
for name in names:
    category = np.random.choice(categories)
    names_categories[name] = category

df = pd.DataFrame({
    "Название": np.random.choice(names, size = 30),
    "Количество": np.random.randint(1, 100, size = 30),
    "Цена за единицу": np.random.randint(10, 10_000, size = 30),
    "Складское помещение": np.random.choice(warehouses, size = 30)
})

df["Категория"] = df["Название"].map(names_categories)
df1 = df.drop_duplicates(subset = ["Название", "Складское помещение"]).reset_index(drop = True)

while len(df1) < 30:
    new_name = np.random.choice(names)
    new_row = {
        "Название": new_name,
        "Категория": names_categories[new_name],
        "Количество": np.random.randint(1, 100),
        "Цена за единицу": np.random.randint(10, 10_000),
        "Складское помещение": np.random.choice(warehouses)
    }
    df1 = pd.concat([df1, pd.DataFrame([new_row])], ignore_index = True)
    df1 = df1.drop_duplicates(subset = ["Название", "Складское помещение"]).reset_index(drop = True)

df = df1.reset_index(drop = True)
