import random

while True:
    print("\n================ МЕНЮ ЗАВДАНЬ ================")
    print("1. Привітання (Ім'я та вік)")
    print("2. Перевірка віку (Вхід дозволено/заборонено)")
    print("3. Гра 'Вгадай число'")
    print("4. Виведення діапазону чисел (З і ПО)")
    print("5. Парні числа у зворотному порядку від n до 1")
    print("6. Обчислення факторіалу (!n)")
    print("7. Визначення оцінки за балами")
    print("8. Калькулятор (a, b та дія)")
    print("0. Вихід із програми")
    print("==============================================")
    
    choice = input("Оберіть номер завдання для запуску (0-8): ").strip()
    
    if choice == "0":
        print("Дякую за використання програми! Бувай!")
        break
        
    elif choice == "1":
        print("\n--- Запуск Завдання 1 ---")
        name = input("Введіть ваше ім'я: ").strip()
        age = input("Введіть ваш вік: ").strip()
        print(f"Привіт {name}, тобі {age}!")
        
    elif choice == "2":
        print("\n--- Запуск Завдання 2 ---")
        age = int(input("Введіть ваш вік: "))
        if age >= 18:
            print("Вхід дозволено!")
        else:
            print("Вхід заборонено!")
            
    elif choice == "3":
        print("\n--- Запуск Завдання 3 ---")
        secret_number = random.randint(1, 10)
        attempts = 3
        print("Комп'ютер загадав число від 1 до 10. У вас є 3 спроби.")
        
        for attempt in range(attempts):
            guess = int(input(f"Спроба {attempt + 1}. Введіть число: "))
            if guess == secret_number:
                print("Вітаємо! Ви вгадали число!")
                break
            elif guess > secret_number:
                print("Менше")
            else:
                print("Більше")
        else:
            print(f"Ви вичерпали спроби. Загадане число було: {secret_number}")
            
    elif choice == "4":
        print("\n--- Запуск Завдання 4 ---")
        start = int(input("Введіть число З якого починати: "))
        end = int(input("Введіть число ПО яке виводити: "))
        for number in range(start, end + 1):
            print(number, end=" ")
        print()
        
    elif choice == "5":
        print("\n--- Запуск Завдання 5 ---")
        n = int(input("Введіть число n: "))
        for number in range(n, 0, -1):
            if number % 2 == 0:
                print(number, end=" ")
        print()
        
    elif choice == "6":
        print("\n--- Запуск Завдання 6 ---")
        n = int(input("Введіть число для факторіалу: "))
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Факторіал числа {n} дорівнює: {factorial}")
        
    elif choice == "7":
        print("\n--- Запуск Завдання 7 ---")
        score = int(input("Введіть кількість отриманих балів: "))
        if 0 <= score <= 49:
            print("незадовільно")
        elif 50 <= score <= 69:
            print("задовільно")
        elif 70 <= score <= 89:
            print("добре")
        elif 90 <= score <= 100:
            print("відмінно")
        else:
            print("Некоректна кількість балів.")
            
    elif choice == "8":
        print("\n--- Запуск Завдання 8 ---")
        a = float(input("Введіть перше число (a): "))
        b = float(input("Введіть друге число (b): "))
        operation = input("Введіть дію (+, -, *, /): ").strip()
        if operation == "+":
            print(f"Результат: {a + b}")
        elif operation == "-":
            print(f"Результат: {a - b}")
        elif operation == "*":
            print(f"Результат: {a * b}")
        elif operation == "/":
            if b == 0:
                print("Ділення на нуль")
            else:
                print(f"Результат: {a / b}")
        else:
            print("Невідома операція.")
            
    else:
        print("Неправильний вибір! Будь ласка, введіть цифру від 0 до 8.")