from data_init import df
from product_ops import show_data, add_product, remove_product, update_cnt, update_price,  order_product
from filter import fltr_category, fltr_warehouse, min_max_price_warehouse, show_category, filter_price
from analytics import total_sum, avr_price, top5_expensive, cnt_category, cnt_warehouse
from visualization import plot_warehouse_cnt, plot_total_t, plot_warehouse_price, plot_category
from export import export_csv
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Меню основных действий
def functionality_menu(df):
    while True:
        print(f"""
{GREEN}Функциональность:{RESET}
1. Показать товары
2. Добавить товар
3. Удалить товар
4. Изменить количество товара на всех или на одном складе
5. Изменить цену товара на всех или на одном складе
6. Заказать один или несколько товаров
{RED}0. Назад в главное меню{RESET}
""")
        choice = input("Выбор: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            show_data(df)
        elif choice == "2":
            df = add_product(df)
        elif choice == "3":
            df = remove_product(df)
        elif choice == "4":
            df = update_cnt(df)
        elif choice == "5":
            df = update_price(df)
        elif choice == "6":
            df = order_product(df)
        else:
            print(f"\n{RED}Некорректный ввод.{RESET}")
    return df

# Меню фильтрации
def filter_menu(df):
    while True:
        print(f"""
{GREEN}Фильтрация:{RESET}
1. Фильтрация товаров по категории
2. Фильтрация товаров по складу
3. Вывод товаров, цена которых больше и меньше всего на конкретном складе
4. Вывод всех товаров определённой категории
5. Фильтрация данных по цене в заданном диапазоне
{RED}0. Назад в главное меню{RESET}
""")
        choice = input("Выбор: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            fltr_category(df)
        elif choice == "2":
            fltr_warehouse(df)
        elif choice == "3":
            min_max_price_warehouse(df)
        elif choice == "4":
            show_category(df)
        elif choice == "5":
            filter_price(df)
        else:
            print(f"\n{RED}Некорректный ввод.{RESET}")
    return df

# Меню аналитики
def analytics_menu(df):
    while True:
        print(f"""
{GREEN}Аналитика:{RESET}
1. Общая стоимость всех товаров
2. Средняя цена по категориям
3. Топ-5 самых дорогих позиций
4. Число товаров одной категориям
5. Число товаров на одном складе
{RED}0. Назад в главное меню{RESET}
""")
        choice = input("Выбор: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            total_sum(df)
        elif choice == "2":
            avr_price(df)
        elif choice == "3":
            top5_expensive(df)
        elif choice == "4":
            cnt_category(df)
        elif choice == "5":
            cnt_warehouse(df)
        else:
            print(f"\n{RED}Некорректный ввод.{RESET}")
    return df

# Меню визуализации
def visualization_menu(df):
    while True:
        print(f"""
{GREEN}Визуализация:{RESET}
1. Диаграмма заполненности складов
2. График числа товаров (сумма со всех складов)
3. График стоимости товаров на конкретном складе
4. Круговая диаграмма: доля категорий в общей стоимости всех товаров
{RED}0. Назад в главное меню{RESET}
""")
        choice = input("Выбор: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            plot_warehouse_cnt(df)
        elif choice == "2":
            plot_total_t(df)
        elif choice == "3":
            plot_warehouse_price(df)
        elif choice == "4":
            plot_category(df)
        else:
            print(f"\n{RED}Некорректный ввод.{RESET}")
    return df

# Главное меню
def menu(df):
    while True:
        print(f"""
{GREEN}Меню:{RESET}
1. Основные действия
2. Фильтрация              
3. Аналитика
4. Визуализация
5. Сохранение данных в CSV
{RED}0. Выход{RESET}
""")
        choice = input("Выбор: ").strip()

        if choice == "0":
            print("\nВыход из программы.")
            break
        elif choice == "1":
            df = functionality_menu(df)
        elif choice == "2":
            df = filter_menu(df)
        elif choice == "3":
            df = analytics_menu(df)
        elif choice == "4":
            df = visualization_menu(df)
        elif choice == "5":
            export_csv(df)
        else:
            print(f"\n{RED}Некорректный ввод.{RESET}")
    return df

# Запуск
print("\nСПИСОК СКЛАДА")
menu(df)