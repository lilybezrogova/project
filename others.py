import numpy as np
import random
import re
from logging_utils import log_action
from data_init import df
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def confirm_operation():
    cnt = 0
    while cnt < 2:
        name = input("\nВведите 'yes' для подтверждения операции или 'no' для отмены: ").strip()
        if name == "yes":
            return True
        elif name == "no":
            print(f"{RED}Операция отменена.{RESET} Возврат в меню.")
            log_action("Операция отменена.")
            return False
        else:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
    print(f"\n{RED}Превышено количество попыток. Операция отменена.{RESET} Возврат в меню.")
    log_action("Превышено количество попыток. Операция отменена.")
    return False

def check_cancel(name):
    if name == "0":
        print(f"{RED}Операция отменена.{RESET} Возврат в меню.")
        return True
    return False

def check_name_st(df):
    names = [str(x) for x in df["Название"].unique()]
    cnt = 0
    pattern = r"^Товар_\d+$"

    while cnt < 2:
        name = input(f"\nВведите имя из предложенных {names} или новое имя (например, Товар_100), 0 для отмены: ").strip()
        if check_cancel(name):
            return None

        if name in names:
            return name
        
        elif re.match(pattern, name):
            if confirm_operation():  
                names.append(name)    
                log_action(f"Пользователь добавил {name}")
                return name
            else:
                return None
        else:
            cnt += 1
            print(f"{RED}Некорректный ввод нового имени (попытка {cnt} из 2).{RESET} Допустимый формат: Товар_число.")

    name = random.choice(names)
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрано случайное: {name}")
    log_action(f"Превышено количество попыток. Выбрано случайное: {name}")
    if confirm_operation() is False:
        return None
    return name

def check_name(df):
    names = [str(x) for x in df["Название"].unique()]
    cnt = 0
    while cnt < 2:
        name = input(f"\nВведите имя из предложенных {names} или 0 для отмены: ").strip()
        if check_cancel(name):
            return None
        if name in names:
            return name 
        else:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
    name = random.choice(names)
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрано случайное: {name}")
    log_action(f"Превышено количество попыток. Выбрано случайное: {name}")
    if confirm_operation() is False:
        return None
    return name

def check_category(categories):
    cnt = 0
    while cnt < 2:
        category = input(f"\nВведите категорию из предложенных {categories} или 0 для отмены: ").strip()
        if check_cancel(category):
            return None
        if category in categories:
            return category 
        else:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
    category = random.choice(categories)
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрана случайная: {category}")
    log_action(f"Превышено количество попыток. Выбрана случайная: {category}")
    if confirm_operation() is False:
        return None
    return category

def check_cnt(df):
    c = 0
    while c < 2:
        cnt = input(f"\nВведите количество или 0 для отмены: ").strip()
        if check_cancel(cnt) is True:
            return None
        try:
            cnt = int(cnt)
        except ValueError:
            c += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
        else:
            if cnt < 0:
                c += 1
                print(f"{RED}Некорректный ввод (попытка {cnt} из 2). {RESET} Количество не может быть отрицательным.")
            else:
                return cnt     
    cnt = np.random.randint(0, df["Количество"].max())
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрано случайное: {cnt}.")
    log_action(f"Превышено количество попыток. Выбрано случайное: {cnt}.")
    if confirm_operation() is False:
        return None
    return cnt

def check_price(df):
    cnt = 0
    while cnt < 2:
        price = input(f"\nВведите цену или 0 для отмены: ").strip()
        if check_cancel(price) is True:
            return None
        try:
            price = int(price)
        except ValueError:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
        else:
            if price < 0:
                cnt += 1
                print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET} Цена не может быть отрицательной.")
            else:
                return price     
    price = np.random.randint(0, df["Цена за единицу"].max())
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрана случайная: {price}.")
    log_action(f"Превышено количество попыток. Выбрана случайная: {price}.")
    if confirm_operation() is False:
        return None
    return price

def check_warehouse(warehouses):
    cnt = 0
    while cnt < 2:
        warehouse = input(f"\nВведите склад из предложенных {warehouses} или 0 для отмены: ").strip()
        if check_cancel(warehouse) is True:
            return None
        if warehouse in warehouses:
            return warehouse 
        cnt += 1
        print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
    warehouse = random.choice(warehouses)
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбран случайный: {warehouse}")
    log_action(f"Превышено количество попыток выбора склада. Выбран случайный: {warehouse}")
    if confirm_operation() is False:
        return None
    return warehouse

def check_warehouse1(warehouses):
    cnt = 0
    while cnt < 2:
        warehouse = input(f"\nВведите склад из предложенных или 0 для всех складов: ").strip()
        if warehouse == "0":  
            return 0
        if warehouse in warehouses:
            return warehouse 
        cnt += 1
        print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
    warehouse = random.choice(warehouses)
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбран случайный: {warehouse}")
    log_action(f"Превышено количество попыток выбора склада. Выбран случайный: {warehouse}")
    if confirm_operation() is False:
        return None
    return warehouse

def check_warehouse2(warehouses):
    cnt = 0
    while cnt < 2:
        warehouse = input(f"\nВведите склад из предложенных или 0 для отмены: ").strip()
        if check_cancel(warehouse) is True:
            return None
        if warehouse in warehouses:
            return warehouse 
        cnt += 1
        print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
    warehouse = random.choice(warehouses)
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбран случайный: {warehouse}")
    log_action(f"Превышено количество попыток выбора склада. Выбран случайный: {warehouse}")
    if confirm_operation() is False:
        return None
    return warehouse

def price_min(df):
    cnt = 0
    while cnt < 2:
        min_price = input(f"\nВведите минимальную цену или 0 для отмены: ").strip()
        if check_cancel(min_price) is True:
            return None
        try:
            min_price = int(min_price)
        except ValueError:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
        else:
            if min_price < 0:
                cnt += 1
                print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET} Цена не может быть отрицательной.")
            else:
                return min_price     
    min_price = np.random.randint(0, df["Цена за единицу"].max())
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрана случайная: {min_price}.")
    log_action(f"Превышено количество попыток. Выбрана случайная: {min_price}.")
    if confirm_operation() is False:
        return None
    return min_price

def price_max(df, min_price):
    cnt = 0
    while cnt < 2:
        max_price = input(f"\nВведите максимальную цену или 0 для отмены: ").strip()
        if check_cancel(max_price) is True:
            return None
        try:
            max_price = int(max_price)
        except ValueError:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}")
        else:
            if max_price < 0:
                cnt += 1
                print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET} Цена не может быть отрицательной.")
            elif max_price < min_price:
                cnt += 1
                print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET} Максимальная цена < минимальной цены.")
            else:
                return max_price
    max_price = np.random.randint(min_price, df["Цена за единицу"].max())
    print(f"\n{RED}Превышено количество попыток.{RESET} Выбрана случайная: {max_price}.")
    log_action(f"Превышено количество попыток. Выбрана случайная: {max_price}.")
    if confirm_operation() is False:
        return None
    return max_price       
