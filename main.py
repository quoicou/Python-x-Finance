# coding=utf8

"""
AUTRE MANIERE AVEC BEAUTIFUL SOUP
def scrapping():
    url = 'https://tools.morningstar.fr/fr/stockreport/default.aspx?tab=10&vw=is&SecurityToken=0P00009WL3%5D3%5D0%5DE0WWE%24%24ALL&Id=0P00009WL3&ClientFund=0&CurrencyId=EUR'
    requete = requests.get(url).text
    soup = BeautifulSoup(requete, 'html.parser')
    tableau = soup.find('table',{'class':"right years5"})

    df = pd.read_html(str(tableau))
    # convert list to dataframe
    df = pd.DataFrame(df[0])
    df = df.values.tolist()

    print(df)
    return df
"""

import unidecode
import requests
import pandas as pd
import datetime

def url():
    lien = input("Rentrez l'url de l'action que vous souhaitez analyser\nChoix : ")

    return lien

def annee_actuelle():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    annee = date.year

    return annee

def change_virgule_espace_int(valeur):
    valeur = int(float(unidecode.unidecode(valeur).replace(",", ".").replace(" ", "")))

    return valeur

def scrapping_compte_resultat():
    #url = 'https://tools.morningstar.fr/fr/stockreport/default.aspx?tab=10&vw=is&SecurityToken=0P00009WL3%5D3%5D0%5DE0WWE%24%24ALL&Id=0P00009WL3&ClientFund=0&CurrencyId=EUR'
    #requete = requests.get(url).text
    #dataframe = pd.read_html(requete)

    #values = dataframe[0].values.tolist()
    liste_compte_resultat = [["Chiffre d'affaires", '46\xa0826,00', '53\xa0670,00', '44\xa0650,00', '64\xa0215,00', '79\xa0184,00'], ['Coût des recettes', '15\xa0625,00', '18\xa0123,00', '15\xa0871,00', '20\xa0355,00', '24\xa0988,00'], ["Résultat brut d'exploitation", '31\xa0201,00', '35\xa0547,00', '28\xa0779,00', '43\xa0860,00', '54\xa0196,00'], ["Charges d'exploitation", "Charges d'exploitation", "Charges d'exploitation", "Charges d'exploitation", "Charges d'exploitation", "Charges d'exploitation"], ['Recherche et développement', '-', '-', '-', '-', '-'], ['Ventes, général et administratif', '21\xa0221,00', '24\xa0071,00', '20\xa0433,00', '26\xa0722,00', '33\xa0178,00'], ['Frais de personnel', '-', '-', '-', '-', '-'], ['Dépréciation et amortissement', '-', '-', '-', '-', '-'], ["Autres charges d'exploitation", '-500', '10400', '3500', '1600', '300'], ["Total Charges d'exploitation", '21\xa0216,00', '24\xa0175,00', '20\xa0468,00', '26\xa0738,00', '33\xa0181,00'], ["Résultat d'exploitation avant intérêts et impôts", '9\xa0985,00', '11\xa0372,00', '8\xa0311,00', '17\xa0122,00', '21\xa0015,00'], ['Résultat hors exploitation', '-49600', '-65900', '-94800', '8700', '-90100'], ['Bénéfice avant impôts sur le revenu', '9\xa0489,00', '10\xa0713,00', '7\xa0363,00', '17\xa0209,00', '20\xa0114,00'], ['Provision pour impôts sur le revenu', '2\xa0499,00', '2\xa0932,00', '2\xa0409,00', '4\xa0510,00', '5\xa0362,00'], ['Résultat net des activités continues', '6\xa0990,00', '7\xa0782,00', '4\xa0955,00', '12\xa0698,00', '14\xa0751,00'], ['Résultat net', '6\xa0354,00', '7\xa0171,00', '4\xa0702,00', '12\xa0036,00', '14\xa0084,00'], ['Bénéfice net attribuable aux actionnaires ordinaires', '6\xa0354,00', '7\xa0171,00', '4\xa0702,00', '12\xa0036,00', '14\xa0084,00'], ['Bénéfices par action', 'Bénéfices par action', 'Bénéfices par action', 'Bénéfices par action', 'Bénéfices par action', 'Bénéfices par action'], ['Non dilué', '1264', '1425', '933', '2390', '2805'], ['Dilué', '1261', '1423', '932', '2389', '2803']]

    convert_to_int(liste_compte_resultat)

    return liste_compte_resultat

def scrapping_bilan():
    #url = 'https://tools.morningstar.fr/fr/stockreport/default.aspx?tab=10&vw=bs&SecurityToken=0P00009WL3%5D3%5D0%5DE0WWE%24%24ALL&Id=0P00009WL3&ClientFund=0&CurrencyId=EUR'
    #requete = requests.get(url).text
    #dataframe = pd.read_html(requete)

    #liste_bilan = dataframe[0].values.tolist()

    liste_bilan = [['Actif', 'Actif', 'Actif', 'Actif', 'Actif', 'Actif'],
     ['Actif courant', 'Actif courant', 'Actif courant', 'Actif courant', 'Actif courant', 'Actif courant'],     ['Liquidités, quasi-liquidités et placements à court terme', 'Liquidités, quasi-liquidités et placements à court terme', 'Liquidités, quasi-liquidités et placements à court terme', 'Liquidités, quasi-liquidités et placements à court terme',
      'Liquidités, quasi-liquidités et placements à court terme', 'Liquidités, quasi-liquidités et placements à court terme'],     ['Trésorerie', '4\xa0610,00', '5\xa0673,00', '19\xa0963,00', '8\xa0021,00', '7\xa0300,00'],
     ['Placements à court terme', '66600', '73300', '75200', '2\xa0544,00', '3\xa0552,00'],     ['Total trésorerie, quasi-trésorerie et placements à court terme', '5\xa0276,00', '6\xa0406,00', '20\xa0715,00', '10\xa0565,00', '10\xa0852,00'],
     ['Créances clients', '3\xa0222,00', '3\xa0450,00', '2\xa0756,00', '3\xa0787,00', '4\xa0258,00'],     ['Stock', '12\xa0485,00', '13\xa0717,00', '13\xa0015,00', '16\xa0548,00', '20\xa0319,00'],     ['Autres actifs circulants', '2\xa0568,00', '2\xa0937,00', '3\xa0487,00', '3\xa0401,00', '4\xa0311,00'],
     ['Total actifs circulants', '23\xa0551,00', '26\xa0510,00', '39\xa0973,00', '34\xa0301,00', '39\xa0740,00'],     ['Actif non-courant', 'Actif non-courant', 'Actif non-courant', 'Actif non-courant', 'Actif non-courant', 'Actif non-courant'],
     ['Hors biens, installations et équipements', '14\xa0510,00', '30\xa0260,00', '30\xa0118,00', '33\xa0270,00',      '36\xa0950,00'], ['Fonds et autres placements', '-', '-', '-', '-', '-'],     ['Immobilisations incorporelles', '30\xa0981,00', '33\xa0609,00', '33\xa0368,00', '50\xa0762,00', '50\xa0497,00'],
     ['Impôts sur le revenu différés Passif', '1\xa0932,00', '2\xa0274,00', '2\xa0325,00', '3\xa0156,00', '3\xa0661,00'],
     ['Autres actifs à long terme', '3\xa0326,00', '3\xa0854,00', '2\xa0887,00', '3\xa0822,00', '3\xa0798,00'],     ['Total actifs non courants', '50\xa0749,00', '69\xa0997,00', '68\xa0698,00', '91\xa0010,00', '94\xa0906,00'],
     ["Total de l'actif", '74\xa0300,00', '96\xa0507,00', '108\xa0671,00', '125\xa0311,00', '134\xa0646,00'],     ['Passif et Capitaux propres', 'Passif et Capitaux propres', 'Passif et Capitaux propres', 'Passif et Capitaux propres', 'Passif et Capitaux propres', 'Passif et Capitaux propres'],
     ['Passif', 'Passif', 'Passif', 'Passif', 'Passif', 'Passif'],     ['Passif courant', 'Passif courant', 'Passif courant', 'Passif courant', 'Passif courant', 'Passif courant'],
     ['Dettes fournisseurs', '5\xa0314,00', '5\xa0814,00', '5\xa0098,00', '7\xa0086,00', '8\xa0788,00'],     ['Impôts à payer', '1\xa0223,00', '72200', '72100', '2\xa0368,00', '2\xa0472,00'],
     ['Dette courante', '5\xa0001,00', '7\xa0611,00', '10\xa0638,00', '8\xa0076,00', '9\xa0359,00'],     ['Autres passifs courants', '5\xa0295,00', '8\xa0476,00', '8\xa0861,00', '10\xa0459,00', '10\xa0924,00'],
     ['Total des passifs circulant', '16\xa0833,00', '22\xa0623,00', '25\xa0318,00', '27\xa0989,00', '31\xa0543,00'],     ['Passifs non-circulant', 'Passifs non-circulant', 'Passifs non-circulant', 'Passifs non-circulant', 'Passifs non-circulant', 'Passifs non-circulant'],
     ['Impôts différés passifs', '5\xa0036,00', '5\xa0498,00', '5\xa0481,00', '6\xa0704,00', '6\xa0952,00'],     ['Dettes à long terme', '5\xa0690,00', '5\xa0101,00', '14\xa0065,00', '12\xa0165,00', '10\xa0379,00'],
     ['Autres passifs à long terme', '-', '-', '-', '-', '-'], ['Total passif non-circulant', '-', '-', '-', '-', '-'],     ['Total du passif', '-', '-', '-', '-', '-'],     ['Capitaux propres', 'Capitaux propres', 'Capitaux propres', 'Capitaux propres', 'Capitaux propres', 'Capitaux propres'], ['Actions ordinaires', '15200', '15200', '15200', '15200', '15100'],
     ['Primes liées au capital', '2\xa0298,00', '2\xa0319,00', '2\xa0225,00', '2\xa0225,00', '1\xa0289,00'],     ['Autres réserves', '23\xa0035,00', '33\xa0379,00', '-1\xa0206,00', '1\xa0088,00', '39\xa0593,00'],
     ['Bénéfices non répartis', '6\xa0354,00', '-', '35\xa0363,00', '43\xa0399,00', '14\xa0084,00'],     ['Intérêts Minorité', '1\xa0664,00', '1\xa0779,00', '1\xa0417,00', '1\xa0790,00', '1\xa0493,00'],
     ['Total des capitaux propres', '32\xa0293,00', '36\xa0586,00', '37\xa0412,00', '47\xa0119,00', '55\xa0111,00'],     ['Total du passif et des capitaux propres', '74\xa0300,00', '96\xa0507,00', '108\xa0671,00', '125\xa0311,00', '134\xa0646,00']]

    convert_to_int(liste_bilan)

    return liste_bilan

def convert_to_int(liste):
    for row in range(len(liste)):
        for elem in range(len(liste[row])):
            if str(liste[row][elem])[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                liste[row][elem] = change_virgule_espace_int(liste[row][elem])

    return liste_bilan

def bna(liste_compte_resultat):
    bna_annee_moins_5 = int(liste_compte_resultat[19][1])/100
    bna_annee_moins_4 = int(liste_compte_resultat[19][2])/100
    bna_annee_moins_3 = int(liste_compte_resultat[19][3])/100
    bna_annee_moins_2 = int(liste_compte_resultat[19][4])/100
    bna_annee_moins_1 = int(liste_compte_resultat[19][5])/100

    print(f"BNA {annee_actuelle()-5} = {bna_annee_moins_5}, BNA {annee_actuelle()-4} = {bna_annee_moins_4}, BNA {annee_actuelle()-3} = {bna_annee_moins_3}, BNA {annee_actuelle()-2} = {bna_annee_moins_2}, BNA {annee_actuelle()-1} = {bna_annee_moins_1}")

def gearing(liste_bilan): # à revoir calcul
    gearing_annee_moins_5 = round(liste_bilan[28][1]/(liste_bilan[38][1]+liste_bilan[28][1])*100, 2)
    gearing_annee_moins_4 = round(liste_bilan[28][2]/liste_bilan[38][2]*100, 2)
    gearing_annee_moins_3 = round(liste_bilan[28][3]/(liste_bilan[38][3]+(liste_bilan[28][3]))*100, 2)
    gearing_annee_moins_2 = round(liste_bilan[28][4]/liste_bilan[38][4]*100, 2)
    gearing_annee_moins_1 = round(liste_bilan[28][5]/liste_bilan[38][5]*100, 2)

    print(f"GEARING {annee_actuelle() - 5} = {gearing_annee_moins_5}, GEARING {annee_actuelle() - 4} = {gearing_annee_moins_4}, GEARING {annee_actuelle() - 3} = {gearing_annee_moins_3}, GEARING {annee_actuelle() - 2} = {gearing_annee_moins_2}, GEARING {annee_actuelle() - 1} = {gearing_annee_moins_1}")

def bfr(liste_bilan):
    bfr_annee_moins_5 = liste_bilan[9][1] - liste_bilan[25][1]
    bfr_annee_moins_4 = liste_bilan[9][2] - liste_bilan[25][2]
    bfr_annee_moins_3 = liste_bilan[9][3] - liste_bilan[25][3]
    bfr_annee_moins_2 = liste_bilan[9][4] - liste_bilan[25][4]
    bfr_annee_moins_1 = liste_bilan[9][5] - liste_bilan[25][5]

    print(f"BFR {annee_actuelle() - 5} = {bfr_annee_moins_5}, BFR {annee_actuelle() - 4} = {bfr_annee_moins_4}, BFR {annee_actuelle() - 3} = {bfr_annee_moins_3}, BFR {annee_actuelle() - 2} = {bfr_annee_moins_2}, BFR {annee_actuelle() - 1} = {bfr_annee_moins_1}")

def roe(liste_bilan, liste_compte_resultat):
    roe_annee_moins_5 = round(liste_compte_resultat[15][1] / liste_bilan[38][1] * 100, 2)
    roe_annee_moins_4 = round(liste_compte_resultat[15][2] / liste_bilan[38][2] * 100, 2)
    roe_annee_moins_3 = round(liste_compte_resultat[15][3] / liste_bilan[38][3] * 100, 2)
    roe_annee_moins_2 = round(liste_compte_resultat[15][4] / liste_bilan[38][4] * 100, 2)
    roe_annee_moins_1 = round(liste_compte_resultat[15][5] / liste_bilan[38][5] * 100, 2)

    print(f"ROE {annee_actuelle() - 5} = {roe_annee_moins_5}, ROE {annee_actuelle() - 4} = {roe_annee_moins_4}, ROE {annee_actuelle() - 3} = {roe_annee_moins_3}, ROE {annee_actuelle() - 2} = {roe_annee_moins_2}, ROE {annee_actuelle() - 1} = {roe_annee_moins_1}")

if __name__ == '__main__':
    #lien = url()
    liste_compte_resultat = scrapping_compte_resultat()
    liste_bilan = scrapping_bilan()
    bna(liste_compte_resultat)
    gearing(liste_bilan)
    bfr(liste_bilan)
    roe(liste_bilan, liste_compte_resultat)

