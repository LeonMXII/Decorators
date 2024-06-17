import os
from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        text = old_function(*args, **kwargs)
        time = datetime.now()
        with open("data.log", "a", encoding="utf-8") as file:
            file.write(f" {time} | {old_function.__name__} | {args} | {kwargs} | {text}\n")
        return text
    return new_function
@logger
def check_month(month: int):
    if month == 1 or month == 2 or month == 12:
        season = "Зима"
    elif month == 3 or month == 4 or month == 5:
        season = "Весна"
    elif month == 6 or month == 7 or month == 8:
        season = "Лето"
    elif month == 9 or month == 10 or month == 11:
        season = "Осень"
    else:
        season = "Некорректный номер месяца"
    return season


if __name__ == '__main__':
    season = check_month(1)
    assert season == 'Зима', "Ответ должен быть Зима"
    print(f"1 месяц время года: {season}")
    season = check_month(4)
    assert season == 'Весна', "Ответ должен быть Весна"
    print(f"4 месяц время года: {season}")
    season = check_month(18)
    assert season == "Некорректный номер месяца", "Ответ должен быть 'Некорректный номер месяца'"
    print(f"18 месяц: {season}")



