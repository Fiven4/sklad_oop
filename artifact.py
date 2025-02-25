class Artifact:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Название: {self.name}, Оценка: {self.value} руб."
