import json
profile = {}
profile["Имя"] = "Алексей"
profile["Группа"] = "КБ-101"
profile["Навыки"] = ["Python", "Excel"]
profile["Уведомления"] = True
f = open("participant.json", "w", encoding="UTF-8")
json.dump(profile, f, ensure_ascii=False, indent=2)  # записываем профиль
f.close()
f = open("participant.json", "r", encoding="UTF-8")
data = json.load(f)  # читаем профиль
f.close()
data["Навыки"].append("CSV")  # добавляем навык
data["Уведомления"] = False  # выключаем уведомления
f = open("participant.json", "w", encoding="UTF-8")
json.dump(data, f, ensure_ascii=False, indent=2)  # сохраняем изменения
f.close()
f = open("participant.json", "r", encoding="UTF-8")
data = json.load(f)  # читаем заново
f.close()
print(data)  # выводим результат
