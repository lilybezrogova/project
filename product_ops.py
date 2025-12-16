import pandas as pd
from logging_utils import log_action
from data_init import categories, warehouses, names
from others import check_name_st, check_name, check_category, check_cnt, check_price, check_warehouse1, check_warehouse, check_warehouse2
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def show_data(df): # Показать таблицу
    print(f"\n{GREEN}Текущие товары на складе:{RESET} \n\n{df}") 
    log_action("Пользователь посмотрел таблицу.")

def add_product(df): #Добавить товар
    try:
        print(f"\n{GREEN}Добавить товар.{RESET}")
        
        name = check_name_st(df)
        if name is None:
            return df

        category = check_category(categories)
        if category is None:
            return df

        cnt = check_cnt(df)
        if cnt is None:
            return df

        price = check_price(df)
        if price is None:
            return df

        warehouse = check_warehouse(warehouses)
        if warehouse is None:
            return df
        
        p_categories = [str(x) for x in df.loc[df["Название"] == name, "Категория"].unique()]        
        if p_categories and category not in p_categories:
            print(f"\n{RED}{name} уже существует в другой категории {p_categories}.{RESET}")
            log_action(f"Попытка пользователя добавить {name} в категорию {category} отклонена.")
            return df

        p1 = df[(df["Название"] == name) & (df["Категория"] == category) & (df["Цена за единицу"] == price) & (df["Складское помещение"] == warehouse)]

        if not p1.empty:
            idx = p1.index[0]
            df.at[idx, "Количество"] += cnt
            print(f"\n{GREEN}{cnt} шт. добавлено к существующему {name} на {warehouse}.{RESET}")
            log_action(f"Пользователь увеличил количество {name} на {warehouse} на {cnt} шт.")
            return df

        p2 = df[(df["Название"] == name) & (df["Категория"] == category) & (df["Цена за единицу"] == price)]

        if not p2.empty:
            new_row = {
                "Название": name,
                "Категория": category,
                "Количество": cnt,
                "Цена за единицу": price,
                "Складское помещение": warehouse
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index = True)
            print(f"\n{GREEN}{name} добавлен на новый склад {warehouse}.{RESET}")
            log_action(f"Пользователь добавил {name} на новый склад {warehouse}.")
            return df

        p3 = df[(df["Название"] == name) & (df["Категория"] == category)]
        if not p3.empty:
            print(f"\n{RED}{name} в категории {category} уже существует с другой ценой.{RESET}")
            log_action(f"Попытка добавить {name} с другой ценой в категории {category} отклонена.")
            return df

        new_row = {
            "Название": name,
            "Категория": category,
            "Количество": cnt,
            "Цена за единицу": price,
            "Складское помещение": warehouse
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index = True)
        print(f"\n{GREEN}{name} добавлен на {warehouse}.{RESET}")
        log_action(f"Пользователь добавил {name} на {warehouse}.")
    except Exception as e:
        print("Произошла ошибка при добавлении товара.")
        log_action("Произошла ошибка при добавлении товара.")
    return df

def remove_product(df):  # Удалить товар с одного или со всех складов
    try:
        print(f"\n{GREEN}Удалить товар с одного или со всех складов.{RESET}")

        name = check_name(df)
        if name is None:
            return df
        
        df1 = df[df["Название"] == name]

        if len(df1) > 1:
            print(f"\n{GREEN} {name} есть на нескольких складах: {RESET}")
            print(df1[["Название", "Складское помещение"]])
            warehouse = check_warehouse1(warehouses) 
            if warehouse is None:
                return df
            if warehouse == 0:
                mask = (df["Название"] == name)
                w = "на всех складах"
            else:
                mask = (df["Название"] == name) & (df["Складское помещение"] == warehouse)
                w = f"на {warehouse}"
        else:
            mask = (df["Название"] == name)
            warehouse = df1.iloc[0]["Складское помещение"]
            w = f"на {warehouse}"

        if df.loc[mask].empty:
            print(f"\n{RED}{name} {w} нет.{RESET}")
            log_action(f"Пользователь попытался удалить отсутствующий {name} {w}.")
            return df
        else:
            df = df.loc[~mask].reset_index(drop = True)
            print(f"\n{GREEN}{name} {w} удалён.{RESET}")
            log_action(f"Пользователь удалил {name} {w}.")

    except Exception as e:
        print(f"\n{RED}Произошла ошибка при удалении товара.{RESET}")
        log_action("Произошла ошибка при удалении товара.")
    return df

def update_cnt(df):  # Изменить количество товара на всех или на одном складе
    try:
        print(f"\n{GREEN}Изменить количество товара на всех или на одном складе.{RESET}")

        name = check_name(df)
        if name is None:
            return df

        df1 = df[df["Название"] == name]

        if len(df1) > 1:
            print(f"\n{GREEN}{name} есть на нескольких складах:{RESET}")
            print(df1[["Название", "Складское помещение", "Количество"]])
            warehouse = check_warehouse1(warehouses)
            if warehouse is None:
                return df
            if warehouse == 0:
                mask = (df["Название"] == name)
                w = "на всех складах"
            else:
                mask = (df["Название"] == name) & (df["Складское помещение"] == warehouse)
                w = f"на {warehouse}"
        else:  
            mask = (df["Название"] == name)
            warehouse = df1.iloc[0]["Складское помещение"]
            w = f"на {warehouse}"

        if df.loc[mask].empty:
            print(f"\n{RED}{name} {w} нет.{RESET}")
            log_action(f"Пользователь попытался изменить количество отсутствующего {name} {w}.")
        else:
            cnt = check_cnt(df)
            if cnt is None:
                return df
            df.loc[mask, "Количество"] = cnt
            print(f"\n{GREEN}Количество {name} {w} изменено на {cnt}.{RESET}")
            log_action(f"Пользователь изменил количество {name} {w} на {cnt}.")

    except Exception as e:
        print(f"\n{RED}Произошла ошибка при изменении количества товара.{RESET}")
        log_action("Произошла ошибка при изменении количества товара.")
    return df

def update_price(df): # Изменить цену товара на всех или на одном складе
    try:
        print(f"\n{GREEN}Изменить цену товара на всех или на одном складе.{RESET}")

        name = check_name(df)
        if name is None:
            return df

        df1 = df[df["Название"] == name]

        if len(df1) > 1:
            print(f"\n{GREEN}{name} есть на нескольких складах:{RESET}")
            print(df1[["Название", "Складское помещение", "Цена за единицу"]])
            warehouse = check_warehouse1(warehouses)
            if warehouse is None:
                return df
            if warehouse == 0:
                mask = (df["Название"] == name)
                w = "на всех складах"
            else:
                mask = (df["Название"] == name) & (df["Складское помещение"] == warehouse)
                w = f"на {warehouse}"
        else:  
            mask = (df["Название"] == name)
            warehouse = df1.iloc[0]["Складское помещение"]
            w = f"на {warehouse}"

        if df.loc[mask].empty:
            print(f"\n{RED}{name} {w} нет.{RESET}")
            log_action(f"Пользователь попытался изменить цену отсутствующего {name} {w}.")
        else:
            price = check_price(df)
            if price is None:
                return df
            df.loc[mask, "Цена за единицу"] = price
            print(f"\n{GREEN}Цена {name} {w} изменена на {price}.{RESET}")
            log_action(f"Пользователь изменил цену {name} {w} на {price}.")

    except Exception as e:
        print(f"\n{RED}Произошла ошибка при изменении цены товара.{RESET}")
        log_action("Произошла ошибка при изменении цены товара.")
    return df

def order_product(df):  # Заказать один или несколько товаров
    try:
        print(f"\n{GREEN}Заказать один или несколько товаров.{RESET}")

        name = check_name(df)
        if name is None:
            return df

        cnt = check_cnt(df)
        if cnt is None:
            return df

        df1 = df[df["Название"] == name]

        if len(df1) > 1:
            print(f"\n{GREEN}{name} есть на нескольких складах:{RESET}")
            print(df1[["Название", "Складское помещение", "Количество"]])
            warehouse = check_warehouse2(warehouses)
            if warehouse is None:
                return df
            mask = (df["Название"] == name) & (df["Складское помещение"] == warehouse)
            w = f"на {warehouse}"
        else: 
            mask = (df["Название"] == name)
            warehouse = df1.iloc[0]["Складское помещение"]
            w = f"на {warehouse}"

        if df.loc[mask].empty:
            print(f"\n{RED}{name} {w} нет.{RESET}")
            log_action(f"Пользователь попытался заказать отсутствующий {name} {w}.")
            return df 

        c = df.loc[mask, "Количество"].iloc[0]
        if c < cnt:
            print(f"{RED}{name} не хватает {w}.{RESET} Доступное количество: {c}")
            log_action(f"Пользователь хотел заказать {name}, но {w} его не хватает.")
            return df

        df.loc[mask, "Количество"] -= cnt
        print(f"\n{GREEN}Заказ: {cnt} шт. {name} {w}.{RESET}")
        log_action(f"Пользователь заказал {cnt} шт. {name} {w}.")

    except Exception as e:
        print(f"\n{RED}Произошла ошибка при заказе товара.{RESET}")
        log_action("Произошла ошибка при заказе товара.")
    return df