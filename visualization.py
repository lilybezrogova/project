import matplotlib.pyplot as plt
from logging_utils import log_action
from others import check_warehouse
from data_init import warehouses
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def plot_warehouse_cnt(df): # Диаграмма заполненности складов
    try:        
        df1 = df["Складское помещение"].value_counts()
        df1.plot(kind = "bar", color = "skyblue")
        plt.title("Заполненность складов")
        plt.ylabel("Количество товаров")
        plt.xlabel("Склад")
        file = "plot_warehouse.png"
        plt.savefig(file)
        plt.show()
        print(f"\n{GREEN}Диаграмма заполненности складов сохранена в файл {file}.{RESET}")
        log_action("Пользователь запросил диаграмму заполненности складов.")
    except Exception as e:
        print("Произошла ошибка при построении диаграммы складов.")
        log_action("Произошла ошибка при построении диаграммы складов.")

def plot_total_t(df): # График числа товаров (сумма со всех складов)
    try:
        df1 = df.groupby("Складское помещение")["Количество"].sum()
        df1.plot(kind = "bar", color = "lightgreen")
        plt.title("Сумма со всех складов")
        plt.ylabel("Количество")
        plt.xlabel("Склад")
        file = "plot_total_t.png"
        plt.savefig(file)
        plt.show()
        print(f"\n{GREEN}График числа товаров (сумма со всех складов) сохранен в файл {file}.{RESET}")
        log_action("Пользователь просмотрел график числа товаров (сумма со всех складов).")
    except Exception as e:
        print("Произошла ошибка при построении графика числа товаров (сумма со всех складов).")
        log_action("Произошла ошибка при построении графика числа товаров (сумма со всех складов).")

def plot_warehouse_price(df): # График стоимости товаров на конкретном складе
    try:
        warehouse = check_warehouse(warehouses)
        if warehouse is None:
            return df
        df1 = df[df["Складское помещение"] == warehouse].copy()  
        df1["Стоимость"] = df1["Количество"] * df1["Цена за единицу"]
        df1.plot(x = "Название", y = "Стоимость", kind = "bar", legend = False)
        plt.title(f"Стоимость товаров на {warehouse}")
        plt.ylabel("Стоимость")
        plt.xlabel("Товар")
        file = f"plot_warehouse_price_{warehouse}.png"
        plt.savefig(file)
        plt.show()
        print(f"{GREEN}График стоимости товаров на конкретном складе сохранен в файл {file}.{RESET}")
        log_action(f"Пользователь просмотрел график стоимости товаров на {warehouse}.")
    except Exception as e:
        print(f"Произошла ошибка при построении графика стоимости товаров на {warehouse}.")
        log_action(f"Произошла ошибка при построении графика стоимости товаров на {warehouse}.")

def plot_category(df): # Круговая диаграмма: доля категорий в общей стоимости всех товаров
    try:
        df1 = df.copy()
        df1["Стоимость"] = df1["Количество"] * df1["Цена за единицу"]
        df2 = df1.groupby("Категория")["Стоимость"].sum()
        df2.plot(kind = "pie", autopct = "%1.1f%%", startangle = 90)
        plt.title("Доля категорий в общей стоимости всех товаров")
        plt.ylabel("")
        file = "plot_category.png"
        plt.savefig(file)
        plt.show()
        print(f"\n{GREEN}Круговая диаграмма сохранена в файл {file}.{RESET}")
        log_action("Пользователь просмотрел круговую диаграмму: доля категорий в общей стоимости всех товаров.")
    except Exception as e:
        print("Произошла ошибка при построении круговой диаграммы: доля категорий в общей стоимости всех товаров.")
        log_action("Произошла ошибка при построении круговой диаграммы: доля категорий в общей стоимости всех товаров.")
