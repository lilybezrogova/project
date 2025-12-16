from logging_utils import log_action
from others import confirm_operation, check_cancel
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def export_csv(df):
    print(f"\n{GREEN}Экспорт данных в CSV\n{RESET}")

    cnt = 0
    file = ""

    while cnt < 2:
        file = input("Введите имя файла для сохранения или 0 для отмены: ").strip()
        if check_cancel(file) is True:
            return df
        if file:
            break
        else:
            cnt += 1
            print(f"{RED}Некорректный ввод (попытка {cnt} из 2).{RESET}\n")

    if file == "":
        file = "f1.csv"
        print(f"{RED}Превышено количество попыток.{RESET} Используется имя файла по умолчанию: f1.csv")

    if file[-4:] != ".csv":
        file += ".csv"

    if confirm_operation() is False:
        return df

    try:
        df.to_csv(file, index = False, encoding = "utf-8")
        print(f"{GREEN}Данные сохранены в файл {file}.{RESET}")
        log_action(f"Пользователь экспортировал данные в файл {file}.")
    except Exception:
        print("Произошла ошибка при сохранении данных в CSV.")
        log_action("Произошла ошибка при сохранении данных в CSV.")
    return df
