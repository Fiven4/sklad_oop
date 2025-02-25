from personal_data import Personality
from artifact import Artifact

class User(Personality):
    def __init__(self, username: str, password: str):
        super().__init__(username, password, role="user")
        self._history = []

    @property
    def history(self):
        return self._history
    @staticmethod
    def create_user(users: list):
        print("\n--- Создание нового пользователя ---")
        new_username = input("Введите логин: ")
        new_password = input("Введите пароль: ")
        if not new_username.strip() or not new_password.strip():
            print("Ошибка: Логин и пароль не могут быть пустыми.")
            return
        for user in users:
            if user.username == new_username and user.role == "user":
                print("Ошибка: Пользователь с таким логином уже существует!")
                return
        new_user = User(new_username, new_password)
        users.append(new_user)
        print(f"Пользователь '{new_username}' успешно создан!")
    @staticmethod
    def view_artifacts(artifacts: list[Artifact]):
        print("\n--- Доступные экспонаты ---")
        if not artifacts:
            print("В данный момент экспонатов нет.")
            return
        for artifact in artifacts:
            print(artifact)
        print("-" * 30)
    def view_history(self):
        print("\n--- История просмотров ---")
        if not self._history:
            print("Вы еще не просматривали экспонаты.")
            return
        for item in self._history:
            print(item)
        print("-" * 30)
    def update_profile(self):
        print("\n--- Обновление профиля ---")
        new_password = input("Введите новый пароль: ")
        if new_password.strip():
            self.password = new_password
            print("Пароль успешно обновлен.")
        else:
            print("Ошибка: Пароль не может быть пустым.")
    def view_artifact(self, artifacts: list[Artifact]):
        artifact_name = input("Введите название экспоната для просмотра: ")
        for artifact in artifacts:
            if artifact.name.lower() == artifact_name.lower():
                self._history.append(artifact.name)
                print(artifact)
                print(f"Вы просмотрели экспонат '{artifact.name}'.")
                return
        print("Экспонат не найден.")
