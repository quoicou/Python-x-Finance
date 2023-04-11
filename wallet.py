import unidecode
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

def start():
    choix = 0

    while choix not in [1, 2, 3]:

        choix = int(input("Que souhaitez-vous ?\n1) Consulter action\n2) Comparer wallet\n3) Ajouter une action au wallet\nChoix : "))

        if choix == 1:
            return choix

        elif choix == 2:
            return choix

        elif choix == 3:
            return choix

def isin(choix):
    if choix == 1:
        code_isin = input("Rentrez le code ISIN de l'action que vous souhaitez consulter\nChoix : ")

    if choix == 3:
        code_isin = input("Rentrez le code ISIN de l'action que vous souhaitez ajouter\nChoix : ")

    return code_isin

def url(code_isin):
    query = f"site:tradingsat.com {code_isin} inurl:societe.html"
    url = f"https://www.google.com/search?q={query}"
    url_recup = ""

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all('a')

    for result in results:
        try:
            lien = result.get("href")
            if f"{code_isin}/societe.html" in lien:
                url_recup = lien
        except:
            pass

    return url_recup

def scrapping(url_recup):
    response = requests.get(url_recup)

    soup = BeautifulSoup(response.text, 'html.parser')

    infos_action = soup.find('div', class_='quote-header-id')
    nom = infos_action.find('h1').text
    price = soup.find('span', class_='price').text
    price = float(price.replace('€', '').replace(',', '.').strip())
    variation = soup.find('span', class_='variation').text

    print(f"Nom de l'action : {nom}")
    print(f'Prix actuel : {price}')
    print(f'Variation de prix : {variation}')

    return nom, price

def write(nom_action, price, code_isin, url_recup):
    nb_action = int(input("Combien d'action souhaitez-vous acheter ?\nChoix : "))

    prix_total = round(price * nb_action, 4)

    print(f"Vous avez acheté pour {prix_total} € d'action ")

    filename = "C://Users//fabi1//Documents//PYTHONxFinance//wallet.txt"
    with open(filename, "a") as f:
        f.write(f"\n[[{code_isin}][{nom_action}][{price}][{nb_action}][{datetime.datetime.now()}][{url_recup}]]")

def read():
    today_price, _ = scrapping()
    filename = "wallet.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
        last_price_line = lines[0]
        last_price = float(last_price_line.split(":")[1].strip().replace("€", ""))
        variation = today_price - last_price
        return variation

if __name__ == '__main__':
    choix = start()

    if choix == 1:
        code_isin = isin(choix)
        url_recup = url(code_isin)
        scrapping(url_recup)

    elif choix == 2:
        read()

    elif choix == 3:
        code_isin = isin(choix)
        url_recup = url(code_isin)
        nom_action, price = scrapping(url_recup)
        write(nom_action, price, code_isin, url_recup)



