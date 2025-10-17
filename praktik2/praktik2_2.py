"""Декоратор доступа."""


def require_role(allowed_roles):
    """Декоратор доступа"""
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            # Проверяем роль пользователя
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None
        return wrapper
    return decorator

# Пример использования декоратора с параметрами


@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Успешно удалено"


@require_role(["admin", "manager"])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки обновлены"


@require_role(["user", "manager", "admin"])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные загружены"


# Создаем пользователей с разными ролями
users = [
    {"name": "Алексей", "role": "admin"},
    {"name": "Мария", "role": "manager"},
    {"name": "Иван", "role": "user"},
    {"name": "Ольга", "role": "guest"}
]

# Тестируем доступ для разных пользователей
print("=== Тестирование декоратора доступа ===")

for user in users:
    print(f"\n--- Тестирование для пользователя: \
          {user['name']} (роль: {user['role']}) ---")
    # Пытаемся выполнить разные операции
    delete_database(user)
    edit_settings(user)
    view_data(user)
