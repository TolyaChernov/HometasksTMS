# !/bin/bash
# !/usr/bin/python3

date_b = input("Введите дату рождения в формате \"дд/мм/гггг\": ")

assert len(date_b) == 10 and date_b[0:2].isdigit() and date_b[2] == date_b[5] == "/" and date_b[
                                                                                         3:5].isdigit() and date_b[
                                                                                                            6:].isdigit(), "Проверьте форматт ввода"

day_b = date_b[0:2] if date_b[0] != 0 else date_b[1]
month_b = date_b[3:5] if date_b[3] != 0 else date_b[4]
year_b = date_b[6:]

assert int(day_b) <= 30, "В месяце 30 дней"
assert int(month_b) <= 12, "В году 12 месяцев"

days_b = int(year_b) * 365 + int(month_b) * 12 + int(day_b)

date_p = input("Введите дату в формате \"дд/мм/гггг\": ")

assert len(date_p) == 10 and date_p[0:2].isdigit() and date_p[2] == date_p[5] == "/" and date_p[
                                                                                         3:5].isdigit() and date_p[
                                                                                                            6:].isdigit(), "Проверьте форматт ввода"

day_p = date_p[0:2] if date_p[0] != 0 else date_p[1]
month_p = date_p[3:5] if date_p[3] != 0 else date_p[4]
year_p = date_p[6:]

assert int(day_p) <= 30, "В месяце 30 дней"
assert int(month_p) <= 12, "В году 12 месяцев"

days_p = int(year_p) * 365 + int(month_p) * 12 + int(day_p)

assert days_p > days_b, "Дата рождения должна быть меньше"
days = days_p - days_b

year_rez = days // 365
days_rez = days % 365

print(f"На введенную дату {year_rez} полных лет и {days_rez} дней")
