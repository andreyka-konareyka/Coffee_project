import json
import hashlib


def login_user_with_json(login, password):
    json_file = open('users.json', 'r')
    json_str = ''
    for line in json_file:
        json_str += line

    json_file.close()

    data = json.loads(json_str)
    for Dict in data["users"]:
        if login == Dict["number"]:
            hash_object = hashlib.sha1(password.encode('utf-8'))
            hash_dig = hash_object.hexdigest()
            if hash_dig == Dict["password"]:
                return True

    return False


def registration_with_json(login, password):
    json_file = open('users.json', 'r')
    json_str = ''
    for line in json_file:
        json_str += line

    json_file.close()

    data = json.loads(json_str)
    for Dict in data["users"]:
        if login == Dict["number"]:
            # Пользователь существует
            return False

    hash_password = hashlib.sha1(password.encode('utf-8'))
    new_user = {
        "number": login,
        "password": hash_password.hexdigest()
    }

    data["users"].append(new_user)
    with open('users.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

    return True


def get_list_products_from_json():
    json_str = ''
    with open('products.json', 'r') as file:
        for line in file:
            json_str += line

    data = json.loads(json_str)
    return data["products"]
