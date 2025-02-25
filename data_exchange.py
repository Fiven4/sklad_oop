import json
from user import User
from admin import Admin
from artifact import Artifact

class DataExchange:
    @staticmethod
    def import_data(users: list, artifacts: list, admins: list):
        print("\n--- Импорт данных ---")
        filename = input("Введите имя файла для импорта: ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for user_data in data['users']:
                    user = User(user_data['username'], user_data['password'])
                    users.append(user)
                for admin_data in data['admins']:
                    admin = Admin(admin_data['username'], admin_data['password'])
                    admins.append(admin)
                for artifact_data in data['artifacts']:
                    artifact = Artifact(artifact_data['name'], artifact_data['value'])
                    artifacts.append(artifact)
                print("Данные успешно импортированы.")
        except FileNotFoundError:
            print("Ошибка: Файл не найден.")
        except json.JSONDecodeError:
            print("Ошибка: Некорректный формат JSON.")
        except Exception as e:
            print(f"Ошибка при импорте данных: {e}")

    @staticmethod
    def export_data(users: list, artifacts: list, admins: list):
        print("\n--- Экспорт данных ---")
        filename = input("Введите название файла для экспорта: ")
        data = {
            'users': [{'username': user.username, 'password': user.password} for user in users],
            'artifacts': [{'name': artifact.name, 'value': artifact.value} for artifact in artifacts],
            'admins': [{'username': admin.username, 'password': admin.password} for admin in admins],
        }
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                print("Данные успешно экспортированы!")
        except Exception as e:
            print(f"Ошибка при экспорте данных: {e}")
