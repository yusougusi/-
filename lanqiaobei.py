import json
def get_stord_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("name")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
def greet_user():
    username = get_stord_username()
    if username:
        print(username)
    else:
        username = get_new_username()
        print(username)
greet_user()