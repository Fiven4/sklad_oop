from personal_data import Personality
from artifact import Artifact


class Admin(Personality):
    def __init__(self, username: str, password: str):
        super().__init__(username, password, role="admin")

    @staticmethod
    def create_admin(admins: list):
        print("\n--- Создание нового администратора ---")
        new_admin = input("Введите логин администратора: ")
        new_password = input("Введите пароль администратора: ")

        if not new_admin.strip() or not new_password.strip():
            print("Ошибка: Логин и пароль не могут быть пустыми.")
            return

        for admin in admins:
            if admin.username == new_admin and admin.role == "admin":
                print("Ошибка: Администратор с таким логином уже существует!")
                return

        save_new_admin = Admin(new_admin, new_password)
        admins.append(save_new_admin)
        print(f"Администратор '{new_admin}' успешно создан!")

    def add_artifact(self, artifacts: list[Artifact]):
        print("\n--- Добавление экспоната ---")
        name = input("Введите название экспоната: ")
        if not name.strip():
            print("Ошибка: Название экспоната не может быть пустым.")
            return

        while True:
            try:
                value = float(input("Введите оценочную стоимость экспоната: "))
                if value < 0:
                    raise ValueError("Стоимость не может быть отрицательной.")
                break
            except ValueError as e:
                print(f"Ошибка ввода: {e}. Пожалуйста, введите корректную стоимость.")

        artifacts.append(Artifact(name, value))
        print(f"Экспонат '{name}' добавлен!")

    def remove_artifact(self, artifacts: list[Artifact]):
        print("\n--- Удаление экспоната ---")
        name = input("Введите название экспоната для удаления: ")
        if not name.strip():
            print("Ошибка: Название экспоната не может быть пустым.")
            return

        for artifact in artifacts:
            if artifact.name.lower() == name.lower():
                artifacts.remove(artifact)
                print(f"Экспонат '{name}' удален!")
                return

        print(f"Экспонат '{name}' не найден.")

    def update_artifact(self, artifacts: list[Artifact]):
        print("\n--- Обновление экспоната ---")
        name = input("Введите название экспоната для обновления: ")
        if not name.strip():
            print("Ошибка: Название экспоната не может быть пустым.")
            return
        for artifact in artifacts:
            if artifact.name.lower() == name.lower():
                new_name = input(f"Введите новое название (текущее: {artifact.name}): ") or artifact.name

                while True:
                    try:
                        new_value = float(input(f"Введите новую стоимость (текущая: {artifact.value}): "))
                        if new_value < 0:
                            raise ValueError("Стоимость не может быть отрицательной.")
                        break
                    except ValueError as e:
                        print(f"Ошибка ввода: {e}. Пожалуйста, введите корректную стоимость.")

                artifact.name = new_name
                artifact.value = new_value

                print(f"Экспонат '{name}' успешно обновлен!")
                return
        print(f"Экспонат '{name}' не найден.")
    def sort_artifacts(self, artifacts: list[Artifact]):
        print("\n--- Сортировка экспонатов ---")
        sort_choice = input("Сортировать по (1 - имени, 2 - стоимости): ")
        if sort_choice == "1":
            sorted_artifacts = sorted(artifacts, key=lambda x: x.name)
        elif sort_choice == "2":
            sorted_artifacts = sorted(artifacts, key=lambda x: x.value)
        else:
            print("Неверный выбор сортировки.")
            return

        print("\n--- Экспонаты после сортировки ---")
        for artifact in sorted_artifacts:
            print(artifact)
    def filter_artifacts(self, artifacts: list[Artifact]):
        print("\n--- Фильтрация экспонатов по стоимости ---")
        try:
            min_value = float(input("Введите минимальную стоимость: "))
            max_value = float(input("Введите максимальную стоимость: "))

            filtered_artifacts = [artifact for artifact in artifacts if min_value <= artifact.value <= max_value]

            if filtered_artifacts:
                print("\n--- Отфильтрованные экспонаты ---")
                for artifact in filtered_artifacts:
                    print(artifact)
            else:
                print("Нет экспонатов в указанном диапазоне цен.")
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения для цен.")
    def view_users(self, users: list):
        print("\n--- Список пользователей ---")
        for user in users:
            if user.role == 'user':
                print(user.username)

