import Backend.local_backend as l_backend
import global_settings
import requests
import hashlib
import random


def LoginUser(login, password):
    hash_password = hashlib.sha1(password.encode('utf-8'))
    data = requests.get(url='http://localhost:8080/user', params={"number": login, "password": hash_password.hexdigest()})
    # print(data.text)

    if data.status_code == 500:
        return False
    if data.text == 'true':
        global_settings.SetCurrentUser(login)
        return True
    else:
        return False

    # Старый код
    # До подключения API
    # return l_backend.login_user_with_json(login, password)


def RegistrationUser(login, password):
    headers = {'Content-Type': 'application/json'}
    hash_password = hashlib.sha1(password.encode('utf-8'))
    json_raw = {
        "number": login,
        "password": hash_password.hexdigest()
    }

    data = requests.post(url='http://localhost:8080/user', headers=headers, json=json_raw)
    print(data.text)
    return True

    # Старый код
    # До подключения API
    # return l_backend.registration_with_json(login, password)


def GetListProducts():
    data = requests.get(url='http://localhost:8080/product')
    raw_json_list = data.json()
    result = []
    for product in raw_json_list:
        result.append(product)
        result[-1]['title'] = product['name']

    return result

    # Старый код
    # До подключения API
    #return l_backend.get_list_products_from_json()


def SendOrder():
    cart = global_settings.Products_in_Cart
    data = requests.get(url='http://localhost:8080/user', params={"number": global_settings.CurrentUser})

    user_id = data.json()["id"]
    order_id = str(user_id) + str(random.randint(1000, 9999))
    cart_str = ""

    for product in cart[:-1]:
        cart_str += product["title"] + ' ({0}), '.format(product['count'])
    cart_str += cart[-1]["title"] + ' ({0})'.format(cart[-1]['count'])

    json_ = {
        "id": user_id,
        "billId": order_id,
        "products": cart_str
    }
    data = requests.post(url='http://localhost:8080/order', headers={ 'Content-Type': 'application/json' }, json=json_)
    print(data.text)
    return order_id

    # Старый код
    # До подключения API
    # return l_backend.send_order()