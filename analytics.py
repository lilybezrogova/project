from logging_utils import log_action
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def total_sum(df): # Общая стоимость всех товаров
    total = (df["Количество"] * df["Цена за единицу"]).sum()
    print(f"\n{GREEN}Общая стоимость всех товаров:{RESET} {total}.")
    log_action(f"Пользователь запросил общую стоимость всех товаров.")

def avr_price(df): # Средняя цена по категориям
    avr_price = df.groupby("Категория")["Цена за единицу"].mean()
    print(f"\n{GREEN}Средняя цена по категориям:{RESET} \n\n{avr_price}.")
    log_action(f"Пользователь запросил среднюю цену по категориям.")

def top5_expensive(df): # Топ-5 самых дорогих позиций
    top5 = df.sort_values('Цена за единицу', ascending = False).head(5)
    print(f"\n{GREEN}Топ-5 самых дорогих позиций:{RESET} \n\n{top5}")
    log_action(f"Пользователь запросил топ-5 самых дорогих позиций.")

def cnt_category(df): # Число товаров одной категории
    cnt = df.groupby("Категория")["Количество"].sum()
    print(f"\n{GREEN}Число товаров по категориям:{RESET} \n\n{cnt}.")
    log_action(f"Пользователь запросил число товаров одной категории.")

def cnt_warehouse(df): # Число товаров на одном складе
    cnt = df.groupby("Складское помещение")["Количество"].sum()
    print(f"\n{GREEN}Число товаров на каждом складе:{RESET} \n\n{cnt}.")
    log_action(f"Пользователь запросил число товаров на каждом складе.")


