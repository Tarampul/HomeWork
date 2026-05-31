import colorama

print("Результат функції dir(colorama):")
print(dir(colorama))
print("-" * 50)

colorama.init(autoreset=True)

print(colorama.Fore.RED + "Цей текст червоний")
print(colorama.Fore.GREEN + "Цей текст зелений")

print(colorama.Back.YELLOW + colorama.Fore.BLACK + "Чорний текст на жовтому тлі")

print(colorama.Style.BRIGHT + "Цей текст дуже яскравий")
print("Цей текст звичайний завдяки autoreset=True")