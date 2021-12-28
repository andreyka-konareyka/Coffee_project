import json
import hashlib

import global_settings


def login_user_with_json(login, password):
    json_file = open('users.json', 'r', encoding='utf-8')
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
    json_file = open('users.json', 'r', encoding='utf-8')
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
    with open('users.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

    return True


def get_list_products_from_json():
    json_str = ''
    with open('products.json', 'r', encoding='utf-8') as file:
        for line in file:
            json_str += line

    data = json.loads(json_str)
    return data["products"]


def get_cart_items_from_json():
    json_str = ''
    with open('cart_items.json', 'r', encoding='utf-8') as file:
        for line in file:
            json_str += line

    data = json.loads(json_str)
    return data["cart_items"]


def add_cart_items_in_json(dictionary):
    current_items = get_cart_items_from_json()

    is_OK = False
    for item in current_items:
        if item["id"] == dictionary["id"]:
            item["count"] += 1
            is_OK = True
            break
    if not is_OK:
        dictionary["count"] = 1
        current_items.append(dictionary)

    data = {"cart_items": current_items}
    with open('cart_items.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)


def remove_from_cart_items_in_json(dict):
    current_items = get_cart_items_from_json()

    for item in current_items:
        if item["id"] == dict["id"]:
            item["count"] -= 1
            if item["count"] == 0:
                current_items.remove(item)
            break

    data = {"cart_items": current_items}
    with open('cart_items.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)
