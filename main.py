from artifact import Artifact
from user import User
from admin import Admin
from menu import Menu

artifacts = [
    Artifact("Скифское золото", 250000),
    Artifact("Японская ваза", 300000),
    Artifact("Картина Айвазовского", 4500000)
]
users = []
admins = []
def main():
    print("Добро пожаловать в систему управления музейным складом!")
    while True:
        print("\n--- Главное меню ---")
        action = input("Хотите создать новый логин и пароль (1) или войти под существующим (2)? Выход из программы(3): ").strip().upper()
        if action == "1":
            role_choice = input("Выберите роль (1 - пользователь, 2 - администратор): ").strip()
            if role_choice == "1":
                User.create_user(users)
            elif role_choice == "2":
                Admin.create_admin(admins)
            else:
                print("Неверный выбор роли.")
        elif action == "2":
            if not users and not admins:
                print("Нет зарегистрированных пользователей или администраторов.")
                continue
            username = input("Логин: ")
            password = input("Пароль: ")
            role = input("Введите роль (user/admin): ").strip().lower()

            if role == "user":
                for user in users:
                    if user.username == username and user.password == password:
                        Menu.user_menu(user, artifacts)
                        break
                else:
                    print("Неверный логин или пароль.")
            elif role == "admin":
                for admin in admins:
                    if admin.username == username and admin.password == password:
                        Menu.admin_menu(admin, artifacts, users, admins)
                        break
                else:
                    print("Неверный логин или пароль.")
            else:
                print("Неверная роль.")

        elif action == "3":
            print("Спасибо за использование программы!")
            return

        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
