from logging_utils import log_action
from data_init import categories, warehouses
from others import check_category, check_warehouse, price_min, price_max
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def fltr_category(df): # Фильтрация товаров по категории
    print(f"\n{GREEN}Фильтрация товаров по категории.{RESET}")

    category = check_category(categories)
    if category is None:
        return df
    f = df[df["Категория"] == category]
    print(f"\n{GREEN}Фильтрация товаров по категории {category}:{RESET}\n\n{f}")
    log_action(f"Пользователь запросил фильтрацию по категории {category}.")

def fltr_warehouse(df): # Фильтрация товаров по складу
    print(f"\n{GREEN}Фильтрация товаров по складу.{RESET}")

    warehouse = check_warehouse(warehouses)
    if warehouse is None:
        return df
    f = df[df["Складское помещение"] == warehouse]
    print(f"\n{GREEN}Фильтрация товаров по {warehouse}:{RESET}\n\n{f}")
    log_action(f"Пользователь запросил фильтрацию по {warehouse}.")

def min_max_price_warehouse(df):  # Вывод товаров, цена которых больше и меньше всего на конкретном складе
    try:
        print(f"\n{GREEN}Вывод товаров, цена которых больше и меньше всего на конкретном складе.{RESET}")

        warehouse = check_warehouse(warehouses)
        if warehouse is None:
            return df
        df1 = df[(df["Складское помещение"] == warehouse)]
        max_t = df1.loc[df1["Цена за единицу"].idxmax()]
        min_t = df1.loc[df1["Цена за единицу"].idxmin()]
        
        print(f"\n{GREEN}Товар с максимальной ценой на {warehouse}:{RESET} \n{max_t}")
        print(f"\n{GREEN}Товар с минимальной ценой на {warehouse}:{RESET} \n{min_t}")
        log_action(f"Пользователь запросил товары, цена которых больше и меньше всего на конкретном {warehouse}.")
                
    except Exception as e:
        print("Произошла ошибка при выводе товаров, цена которых больше и меньше всего на конкретном складе.")
        log_action("Произошла ошибка при выводе товаров, цена которых больше и меньше всего на конкретном складе.")

def show_category(df): # Вывод всех товаров определённой категории
    try:
        category = check_category(categories)
        if category is None:
            return df
        fltr = df[df["Категория"] == category]
        print(f"\n{GREEN}Все товары категории {category}:{RESET} \n\n{fltr}")
        log_action(f"Пользователь запросил вывод всех товаров категории {category}.")
        
    except Exception as e:
        print("Произошла ошибка при выводе всех товаров по категории.")
        log_action("Произошла ошибка при выводе всех товаров по категории.")

def filter_price(df): # Фильтрация данных по цене в заданном диапазоне
    try:
        print(f"\n{GREEN}Фильтрация данных по цене в заданном диапазоне.{RESET}")

        min_price = price_min(df)
        if min_price is None:
            return df
        max_price = price_max(df, min_price)
        if max_price is None:
            return df
        df1 = df[(df["Цена за единицу"] >= min_price) & (df["Цена за единицу"] <= max_price)]
        if df1.empty:
            print(f"\n{RED}Товаров в диапазоне цен ({min_price}-{max_price}) нет.{RESET}")
            log_action(f"Товаров в диапазоне цен ({min_price}-{max_price}) нет.")
        else:
            print(f"\n{GREEN}Товары в диапазоне цен ({min_price}-{max_price}):{RESET} \n\n{df1}")
            log_action(f"Пользователь запросил фильтрацию товаров по цене в диапазоне ({min_price}-{max_price}).")
            
    except Exception:
        print("Произошла ошибка при фильтрации товаров по цене в заданном диапазоне.")
        log_action("Произошла ошибка при фильтрации товаров по цене в заданном диапазоне.")
