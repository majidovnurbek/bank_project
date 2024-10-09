parts = """
1-open accaunt
2-deposit accaunt
3-withdraw accaunt
4-display accaunt
5-history
6-transfer
"""
jack = {
    "fullname": "jack Bob",
    "username": "jack",
    "password": 1212,
    "balance": 0,
    "staff": True,
}

history = []

accaunts = {
    "fullname": "a",
    "address": "b",
    "type_accaunt": "d",
    "deposit": 0,
}

while 1:
    print(parts)
    open_accaunt = int(input('inter:'))
    if open_accaunt == 1:
        full = input("inter your fullname:")
        accaunts["fullname"] = full
        addr = input("enter your address:")
        accaunts["address"] = addr
        type_acc = input("what type of accaunt: saving(S) or current(C):")
        accaunts["type_accaunt"] = type_acc
        depo = int(input("how much money you want to deposit:"))
        accaunts["deposit"] = depo
        print("accaunt created succesfully✅")
    elif open_accaunt == 2:
        money_deposit = int(input("how much money you want deposit:"))
        accaunts["deposit"] += money_deposit
        history.append(f"+{money_deposit} pulga to'ldirildi")
        a = "deposit"
        print(f"avaible balance:{accaunts.get(a)}")

    elif open_accaunt == 3:
        money_withdraw = int(input("how much money you want to withdraw:"))
        accaunts["deposit"] -= money_withdraw
        history.append(f"-{money_withdraw}pul yechildi")
        b = "deposit"
        print(f"Avaible balance:{accaunts.get(b)}")
    elif open_accaunt == 4:
        for x in accaunts.items():
            print(*x)

    elif open_accaunt == 6:
        m = int(input("how how momey you want to transfer:"))
        if accaunts["deposit"] > m:
            a = accaunts["deposit"] - m
            accaunts["deposit"] -= m
            print(f"your balance:{a}")
            jack["balance"] += m
            e = f"from your balance to jack->{m} pul o'tqazildi."
            print(e)
            history.append(f"{e}")
        else:
            print("you don't have enough money")
    elif open_accaunt == 5:
        for x in history:
            print(x)
