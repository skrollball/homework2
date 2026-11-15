import csv
f = open("purchases.csv", "w", encoding="UTF-8", newline="")
w = csv.writer(f, delimiter=",")
w.writerow(["Товар", "Цена за штуку", "Количество"])
w.writerow(["Тетрадь", "2.50", "4"])
w.writerow(["Ручка", "1.20", "3"])
w.writerow(["Папка", "4.00", "2"])
w.writerow(["Маркер", "3.30", "1"])
f.close()
f = open("purchases.csv", "r", encoding="UTF-8")  # открываем файл для чтения
rows = list(csv.reader(f, delimiter=","))  # читаем таблицу в список
f.close()  # закрываем файл
total = 0  # счетчик общей суммы
for r in rows[1:]:  # перебираем строки без шапки
    cost = float(r[1]) * int(r[2])  # умножаем цену на количество
    total = total + cost  # прибавляем к общей сумме
    print(r[0], r[1], r[2], cost)  # выводим товар и стоимость
print("Итого:", total)  # выводим итоговую сумму
