import pandas as pd
import matplotlib.pyplot as plt

def archivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\local-comercial-farmacias.csv")
    df = datos[[id, "title", "tipoActividadEconomica", "codigoCNAE", "streetAddress", "postalCode", "xETRS89", "yETRS89", "latitud", "longitud", "municipioId", "municipioTitle", "barrio", "distrito", "idAyuntamiento", "idComunidad", "nombreTitular"]]

    df = datos.rename(columns={

    })