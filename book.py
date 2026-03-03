# Замість списку створюємо словник
contacts = {}

def add_contact():
    name = input("Введіть ПІБ: ")
    phone = input("Введіть номер: ")
    contacts[name] = phone  # Зберігаємо за ключем ПІБ
    print("Контакт додано!")

def show_contacts():
    print("\nСписок контактів:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Додаємо нову функцію видалення
def delete_contact():
    name = input("Введіть ПІБ для видалення: ")
    if name in contacts:
        del contacts[name]
        print("Контакт видалено!")
    else:
        print("Такого контакту не існує.")

# Тут має бути твій цикл while, який викликає ці функції
