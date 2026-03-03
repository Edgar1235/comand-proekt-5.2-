# main.py (Версія Сторони А - на списках)
contacts = []

def add_contact():
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер: ")
    contacts.append(f"{name}: {phone}")
    print("Контакт додано!")

def show_contacts():
    print("\n--- Список контактів ---")
    if not contacts:
        print("Порожньо")
    for c in contacts:
        print(c)

while True:
    print("\n1. Додати | 2. Переглянути | 3. Вихід")
    choice = input("> ")
    if choice == "1": add_contact()
    elif choice == "2": show_contacts()
    elif choice == "3": break