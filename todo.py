tasks = []

try:
    file = open("task.txt", "r", encoding="utf-8")
    for line in file:
        tasks.append(line.strip())
    file.close()
    print("Задачи успешно загружены из файла!")
except FileNotFoundError:
    pass

while True:
    print("\n--- МЕНЕДЖЕР ЗАДАЧ ---")
    print("1. Посмотреть задачи")
    print("2. Добавить задачу")
    print("3. Сохранить")
    print("4. Выйти")

    choice = input("Выбери пункт меню: ").strip()

    if choice == "1":
        print("Твои задачи:")
        print(tasks)

    elif choice == "2":
        new_task = input("Введите текст задачи: ")
        tasks.append(new_task)
        print("Задача добавлена!")

    elif choice == "3":
        file = open("tasks.txt", "w", encoding="utf-8")
        for task in tasks:
            file.write(task + "\n")
        file.close()
        print("Задачи созранены в файл task.txt!")

    elif choice == "4":
        print("До сивдания! Хорошего дня🌹")