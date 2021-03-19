# utils
from utils import get
from utils import post

# typing
from typing import List

import requests
import json


class Dog(object):

    def __init__(self, id: int, name: str, breed: int):
        self.id = id
        self.name = name
        self.breed = breed


class Breed(object):

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.dogs: List[Dog] = []

    def add_dog(self, dog: Dog):
        self.dogs.append(dog)

    def dogs_count(self) -> int:
        return len(self.dogs)


class DogHouse(object):

    def __init__(self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []

    def get_data(self, token: str):
        data_breeds = get('http://dogs.magnet.cl/api/v1/breeds/',token=token)
        self.data_breeds = data_breeds
        for i in data_breeds['results']:
            
            Breed(i['id'],i['name'])
            self.breeds.append(i)

        data_dogs = get('http://dogs.magnet.cl/api/v1/dogs/',token=token)
        self.data_dogs = data_dogs
        for i in data_dogs['results']:
            
            Dog(i['id'],i['name'],i['breed'])
            self.dogs.append(i)
        return self.dogs and self.breeds and self.data_dogs and self.data_breeds
        

    def get_total_breeds(self) -> int:
        total = 0
        for i in self.breeds:
            total +=1
        return total


    def get_total_dogs(self) -> int:
        total = 0
        for i in self.dogs:
            total +=1
        return total


    def get_common_breed(self) -> Breed:
        diccionario_conteo = {}
        for i in self.data_dogs['results']:
            clave = str(i['breed'])
            if not clave in diccionario_conteo:
                diccionario_conteo[clave] = 1
            else:
                diccionario_conteo[clave] += 1
        frecuencia_mayor = 0
        for numero in diccionario_conteo:
            if diccionario_conteo[numero] > frecuencia_mayor:
                numero_mas_repetido = numero
                frecuencia_mayor = diccionario_conteo[numero]
        conteo = diccionario_conteo[str(numero_mas_repetido)]
        for nombre in self.data_breeds['results']:
            if int(numero_mas_repetido) == nombre['id']: 
                class PopularBreed():
                    id = nombre['id']
                    name = nombre['name']
        return PopularBreed()


    def get_common_dog_name(self) -> str:
        diccionario_conteo = {}
        for i in self.data_dogs['results']:
            clave = str(i['name'])
            if not clave in diccionario_conteo:
                diccionario_conteo[clave] = 1
            else:
                diccionario_conteo[clave] += 1
        frecuencia_mayor = 0
        
        for numero in diccionario_conteo:
            if diccionario_conteo[numero] > frecuencia_mayor:
                numero_mas_repetido = numero
                frecuencia_mayor = diccionario_conteo[numero]
        conteo = diccionario_conteo[str(numero_mas_repetido)]

        return numero_mas_repetido
                     
        raise NotImplementedError

    def send_data(self, data: dict, token: str):
        r = post('http://dogs.magnet.cl/api/v1/',data=data, token = token)