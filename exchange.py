import requests
import vikno

# url_nbu = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
#
# req_nbu = requests.get(url=url_nbu)
#
# price_usd = req_nbu.json()[24]["rate"]
price_usd = 37.6194


def backspace():
    vikno.pole_1.bind("<BackSpace>", lambda event: vikno.pole_2.delete(0, "end"))

    vikno.pole_2.bind("<BackSpace>", lambda event: vikno.pole_1.delete(0, "end"))


def trade():
    try:
        if vikno.pole_1.get() and vikno.pole_2.get():
            pass

        elif vikno.pole_1.get():
            usd_uah = float(vikno.pole_1.get()) * price_usd
            vikno.pole_2.insert(0, usd_uah)
            print(1)

        elif vikno.pole_2.get():
            usd_uah = float(vikno.pole_2.get()) / price_usd
            vikno.pole_1.insert(0, usd_uah)
            print(2)

    except ValueError:
        pass
