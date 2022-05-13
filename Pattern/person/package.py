class Package:
    def __init__(self):
        self.thisPack = {}

    def info(self):
        print("Ваша сумка: ")
        if self.thisPack == {}:
            print('- Ничего нет')
        for element in self.thisPack:
            print(f"\t- {element}: {self.thisPack[element]}")