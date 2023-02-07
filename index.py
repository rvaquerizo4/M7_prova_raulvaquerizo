import pandas as pd

def exercici():
    df = pd.read_csv("Llistat.csv", usecols=['NAME', 'NOTES'])
    filtro = (df['NAME'] == 'Abril') | (df['NAME'] == 'Andres') | (df['NAME'] == 'Bruno') | (df['NAME'] == 'Ivan') | (df['NAME'] == 'Kevin') | (df['NAME'] == 'Marta') | (df['NAME'] == 'Raúl') | (df['NAME'] == 'Roger') | (df['NAME'] == 'Samuel') | (df['NAME'] == 'Sara') | (df['NAME'] == 'Xavier')
    lista= df[filtro]
    listaAgrupada = lista.groupby(by='NAME').mean()
    print(listaAgrupada)
    return listaAgrupada;

def exercici2():
    df = pd.read_csv("Llistat.csv", usecols=['NAME', 'GROUP', 'ABSENCES', 'MODULE'])
    filtro = (df['NAME'] == 'Andres') | (df['NAME'] == 'Bruno') | (df['NAME'] == 'Ivan') | (df['NAME'] == 'Kevin') | (
                df['NAME'] == 'Raúl') | (df['NAME'] == 'Roger')
    lista = df[filtro]
    filtro2 = (lista['MODULE'] == 'M07') | (lista['MODULE'] == 'M08')
    lista2 = lista[filtro2]
    listaAgrupada = lista2.groupby(['NAME']).mean()
    print(listaAgrupada)
    return listaAgrupada;

exercici();
exercici2();
