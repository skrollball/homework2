f = open("diary.txt", "w", encoding="UTF-8")#Создаем файл и записываем три исходные строки по очереди
f.write("Сегодня мы работали с файлами Python.\n")
f.write("Научились сохранять текст.\n")
f.write("Узнали, как читать данные обратно.\n")
f.close()
f = open("diary.txt", "r+", encoding="UTF-8")# Добавляем четвертую запись в конец через режим 'r+'
f.read()
f.write("Следующее занятие – CSV и JSON.\n")
f.close()
f = open("diary.txt", "r", encoding="UTF-8")# Читаем файл целиком, выводим текст и считаем строки
text = f.read()
print(text.strip())
print("Количество записей:", len(text.strip().split("\n")))
f.close()
