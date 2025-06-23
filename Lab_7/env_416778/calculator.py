import numpy as np
import pandas as pd

def dodawanie(liczba1, liczba2):
    return np.add(liczba1, liczba2)

def odejmowanie(liczba1, liczba2):
    return np.subtract(liczba1, liczba2)

def mnozenie(liczba1, liczba2):
    return np.multiply(liczba1, liczba2)

def dzielenie(liczba1, liczba2):
    if liczba2 != 0:
        return np.divide(liczba1, liczba2)
    else:
        return "Błąd: dzielenie przez zero!"


def znajdz_najwiecej(lista_liczb, kolumna='kolumna'):
    df = pd.DataFrame({kolumna: lista_liczb})
    return df[kolumna].max()

def policz_wystapienia(lista_liczb, kolumna='kolumna'):
    df = pd.DataFrame({kolumna: lista_liczb})
    return df[kolumna].value_counts().to_dict()
