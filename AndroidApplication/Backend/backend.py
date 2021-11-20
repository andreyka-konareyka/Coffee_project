import local_backend
import global_settings


def LoginUser(login, password):
    # Пока будем использовать json
    # Потом подключим БД и будем с ней работать через API
    return local_backend.login_user_with_json(login, password)