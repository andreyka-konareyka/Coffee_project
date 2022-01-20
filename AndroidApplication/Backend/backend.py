import Backend.local_backend as l_backend
import global_settings
import hashlib
import random
try:
    import requests
except:
    pass


def LoginUser(login, password):
    hash_password = hashlib.sha1(password.encode('utf-8'))
    hexdigest_password = hash_password.hexdigest()

    my_url = 'http://' + global_settings.host + ':8080/user'
    my_params = {
        "number": login,
        "password": hexdigest_password
    }
    try:
        data = requests.get(url=my_url, params=my_params)

        if data.status_code != 200 or data.text == 'false':
            # попытка локальной авторизации
            result = l_backend.login_user_with_json(login, password)
            if result is True:
                global_settings.SetCurrentUser(login)
                return True
            return False

        elif data.text == 'true':
            global_settings.SetCurrentUser(login)
            return True
        else:
            return False
    except:
        return l_backend.login_user_with_json(login, password)


def RegistrationUser(login, password):
    headers = {
        'Content-Type': 'application/json'
    }
    hash_password = hashlib.sha1(password.encode('utf-8'))
    hexdigest_password = hash_password.hexdigest()

    my_url = 'http://' + global_settings.host + ':8080/user'
    json_raw = {
        "number": login,
        "password": hexdigest_password
    }

    try:
        data = requests.post(url=my_url, headers=headers, json=json_raw)
        if data.status_code == 200:
            return True
        return False
    except:
        return l_backend.registration_with_json(login, password)


def GetListProducts():
    my_url = 'http://' + global_settings.host + ':8080/product'
    try:
        data = requests.get(url=my_url)
        if data.status_code == 200:
            product_list = data.json()
            for product in product_list:
                product['title'] = product['name']
            return product_list
        else:
            return l_backend.get_list_products_from_json()
    except:
        return l_backend.get_list_products_from_json()


def SendOrder():
    cart = global_settings.Products_in_Cart
    try:
        data = requests.get(url='http://' + global_settings.host + ':8080/user', params={"number": global_settings.CurrentUser})

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
        try:
            data = requests.post(url='http://' + global_settings.host + ':8080/order', headers={ 'Content-Type': 'application/json' }, json=json_)
            return order_id
        except:
            return l_backend.send_order()
    except:
        return l_backend.send_order()