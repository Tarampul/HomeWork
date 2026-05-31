class Programmer:
    def __init__(self, language):
        self.programming_language = language

    def write_code(self):
        return f"Пише код на {self.programming_language}."


class Designer:
    def __init__(self, software):
        self.design_software = software

    def create_assets(self):
        return f"Малює графіку та анімації у {self.design_software}."


class GameDeveloper(Programmer, Designer):
    def __init__(self, name, language, software, game_engine):
        Programmer.__init__(self, language)
        Designer.__init__(self, software)
        self.developer_name = name
        self.engine = game_engine

    def develop_game(self):
        print(f"Розробник {self.developer_name} створює гру на рушії {self.engine}:")
        print(f"- {self.write_code()}")
        print(f"- {self.create_assets()}")


if __name__ == "__main__":
    dev = GameDeveloper("Тарас", "Python", "Figma", "Roblox Studio")
    
    dev.develop_game()
    
    print("\nПеревірка доступу до ексклюзивних атрибутів:")
    print(f"Мова: {dev.programming_language}")
    print(f"Софт: {dev.design_software}")