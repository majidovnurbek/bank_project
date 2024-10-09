users = {
    "fullname": "a",
    "username": "a1",
    "password": 4444,
    "id": 0

}

auth = """
1. login
2. register
->
"""
while True:
    user = int(input(auth))
    if user == 1:
        ids = input("id: ")
        if ids == users.values():
            print(users)
            username = input("username: ")
            password = int(input("password: "))
            if username == users["username"] and password == users["password"]:
                print('succesfully')
            else:
                print("username or password incorrect")

        else:
            print(f"Not Found -> {ids}")
    elif user == 2:
        a = int(input("please inter your ID:"))
        users["id"] = a
        d = input("inter your fullname:")
        users["fullname"] = d
        b = input("inter your username:")
        users["username"] = b
        c = input('inter your password')
        users['password'] = c
