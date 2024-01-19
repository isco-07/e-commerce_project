class NewObjectError(Exception):
    def __init__(self):
        self.message = "Невозможно добавить товар с нулевым количеством"

    def __str__(self):
        return self.message
