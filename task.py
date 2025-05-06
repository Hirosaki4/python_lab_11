# Лабораторна робота №11. Телефонна книга з розширеним функціоналом

# Створення базових даних — список словників
phone_book = [
    {"ім'я": "Олег", "прізвище": "Коваль", "телефон": "0671234567", "місто": "Київ"},
    {"ім'я": "Ірина", "прізвище": "Шевченко", "телефон": "0957654321", "місто": "Львів"},
    {"ім'я": "Андрій", "прізвище": "Мельник", "телефон": "0634567890", "місто": "Одеса"},
    {"ім'я": "Світлана", "прізвище": "Бондар", "телефон": "0501122334", "місто": "Київ"},
    {"ім'я": "Оксана", "прізвище": "Сидоренко", "телефон": "0939988776", "місто": "Харків"},
]

# Виведення таблиці
def print_contacts(contacts):
    print("{:<10} {:<15} {:<12} {:<10}".format("Ім'я", "Прізвище", "Телефон", "Місто"))
    print("-" * 50)
    for contact in contacts:
        print("{:<10} {:<15} {:<12} {:<10}".format(
            contact["ім'я"], contact["прізвище"], contact["телефон"], contact["місто"]
        ))
    print()

# Пошук контактів
def search_contacts(key):
    query = input(f"Введіть {key}: ").strip()
    if not query:
        print("Порожній ввід. Спробуйте ще раз.")
        return
    results = [c for c in phone_book if c[key].lower() == query.lower()]
    if results:
        print_contacts(results)
    else:
        print("Контакти не знайдено.")

# Оновлення або видалення
def update_or_delete():
    phone = input("Введіть телефон контакту для редагування або видалення: ").strip()
    contact = next((c for c in phone_book if c["телефон"] == phone), None)
    if not contact:
        print("Контакт не знайдено.")
        return

    action = input("Бажаєте оновити (о) чи видалити (в) контакт? ").lower()
    if action == "о":
        for key in ["ім'я", "прізвище", "місто"]:
            new_value = input(f"Нове значення для {key} (залиште порожнім, щоб не змінювати): ").strip()
            if new_value:
                contact[key] = new_value
        print("Контакт оновлено.")
    elif action == "в":
        confirm = input("Ви дійсно хочете видалити контакт? (так/ні): ").lower()
        if confirm == "так":
            phone_book.remove(contact)
            print("Контакт видалено.")
        else:
            print("Видалення скасовано.")

# Аналітика
def analytics():
    cities = {c["місто"] for c in phone_book}
    print("Унікальні міста:", ", ".join(cities))
    city_counts = {}
    for c in phone_book:
        city_counts[c["місто"]] = city_counts.get(c["місто"], 0) + 1
    for city, count in city_counts.items():
        print(f"{city}: {count} контакт(ів)")
    max_city = max(city_counts, key=city_counts.get)
    print(f"Місто з найбільшою кількістю контактів: {max_city}")

# Головне меню
def main():
    while True:
        print("\n1. Показати всі контакти")
        print("2. Пошук за іменем")
        print("3. Пошук за прізвищем")
        print("4. Пошук за містом")
        print("5. Оновити або видалити контакт")
        print("6. Аналітика")
        print("0. Вихід")

        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            print_contacts(phone_book)
        elif choice == "2":
            search_contacts("ім'я")
        elif choice == "3":
            search_contacts("прізвище")
        elif choice == "4":
            search_contacts("місто")
        elif choice == "5":
            update_or_delete()
        elif choice == "6":
            analytics()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
