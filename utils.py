import collections
import charts
import read_anime

def get_rating_ani(datos):
    genero = input('Que genero estas interesado? =>')
    datos = list(filter(lambda item:item['Genre'] == genero, datos))
    animes = [item['Title'] for item in datos]
    ratings = [float(item['Popularity']) for item in datos]
    
    return animes, ratings