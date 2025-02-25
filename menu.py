from user import User
from admin import Admin
from artifact import Artifact
from data_exchange import DataExchange

class Menu:
    @staticmethod
    def user_menu(user: User, artifacts: list[Artifact]):
        while True:
            print(f"\n--- Пользовательское меню: {user.username} ---")
            print("1. Просмотреть доступные экспонаты")
            print("2. Просмотреть историю просмотров")
            print("3. Обновить профиль")
            print("4. Просмотреть экспонат")
            print("5. Выйти")
            choice = input("Выберите действие: ")
            if choice == "1":
                User.view_artifacts(artifacts)
            elif choice == "2":
                user.view_history()
            elif choice == "3":
                user.update_profile()
            elif choice == "4":
                user.view_artifact(artifacts)
            elif choice == "5":
                break
            else:
                print("Неверный выбор, попробуйте снова.")
    @staticmethod
    def admin_menu(admin: Admin, artifacts: list[Artifact], users: list[User], admins: list[Admin]):
        while True:
            print(f"\n--- Меню администратора: {admin.username} ---")
            print("1. Добавить экспонат")
            print("2. Удалить экспонат")
            print("3. Обновить экспонат")
            print("4. Просмотреть всех пользователей")
            print("5. Создать нового администратора")
            print("6. Сортировать экспонаты")
            print("7. Фильтровать экспонаты по стоимости")
            print("8. Экспортировать данные")
            print("9. Импортировать данные")
            print("10. Выйти")
            choice = input("Выберите действие: ")
            if choice == "1":
                admin.add_artifact(artifacts)
            elif choice == "2":
                admin.remove_artifact(artifacts)
            elif choice == "3":
                admin.update_artifact(artifacts)
            elif choice == "4":
                admin.view_users(users)
            elif choice == "5":
                Admin.create_admin(admins)
            elif choice == "6":
                admin.sort_artifacts(artifacts)
            elif choice == "7":
                admin.filter_artifacts(artifacts)
            elif choice == "8":
                DataExchange.export_data(users, artifacts, admins)
            elif choice == "9":
                DataExchange.import_data(users, artifacts, admins)
            elif choice == "10":
                break
            else:
                print("Неверный выбор, попробуйте снова.")
