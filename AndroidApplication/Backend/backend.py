import Backend.local_backend as l_backend
import global_settings


def LoginUser(login, password):
    # Пока будем использовать json
    # Потом подключим БД и будем с ней работать через API
    return l_backend.login_user_with_json(login, password)


def RegistrationUser(login, password):
    # Пока будем использовать json
    # Потом подключим БД и будем с ней работать через API
    return l_backend.registration_with_json(login, password)