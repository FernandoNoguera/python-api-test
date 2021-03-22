# utils
from utils import get
from utils import post

# typing
from typing import List

import requests
import json


class Dog(object):
    """
    Dog object that is composed of the id, name and breed of the dog

    To initialize:
    :param id: dog id
    :param name: dog name
    :param breed: dog breed id

    USAGE:
        >>> dog = Dog(id=1, name='Bobby', breed=1)
    """
    def __init__(self, id: int, name: str, breed: int):
        self.id = id
        self.name = name
        self.breed = breed


class Breed(object):
    """
    Breed object that is composed of the id and the name of the breed.

    To initialize:
    :param id: breed id
    :param name: breed name

    Also, breed has a list of dogs for development purposes
    :field dogs: breed dog list

    USAGE:
        >>> breed = Breed(id=1, name='Kiltro')
        >>> dog = Dog(id=1, name='Cachupin', breed=breed.id)
        >>> breed.add_dog(dog)
        >>> breed.dogs_count()
        1
    """
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.dogs: List[Dog] = []

    def add_dog(self, dog: Dog):
        self.dogs.append(dog)

    def dogs_count(self) -> int:
        return len(self.dogs)


class DogHouse(object):
    """
    Doghouse object that manipulates information on breeds and dogs.
    We expect you implement all the methods that are not implemented
    so that the flow works correctly


    DogHouse has a list of breeds and a list of dogs.
    :field breeds: breed list
    :field dogs: dog list

    USAGE:
        >>> dog_house = DogHouse()
        >>> dog_house.get_data(token='some_token')
        >>> total_dogs = dog_house.get_total_dogs()
        >>> common_breed = dog_house.get_common_breed()
        >>> common_dog_name = dog_house.get_common_dog_name()
        >>> total_breeds = dog_house.get_total_breeds()
        >>> data = {  # add some data
        ...     'total_dogs': total_dogs,
        ...     'total_breeds': total_breeds,
        ...     'common_breed': common_breed.name,
        ...     'common_dog_name': common_dog_name,
        ... }
        >>> token = 'some token'
        >>> dog_house.send_data(data=data, token=token)
    """
    def __init__(self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []

    def get_data(self, token: str):

        data_dogs = get('http://dogs.magnet.cl/api/v1/dogs/',token=token)
        data_breeds = get('http://dogs.magnet.cl/api/v1/breeds/',token=token)

        for i in data_breeds['results']:
            breed = Breed(i['id'],i['name'])
            self.breeds.append(breed)

        for i in data_dogs['results']:
            dog = Dog(i['id'],i['name'],i['breed'])
            self.dogs.append(dog)

        for i in self.dogs:
            breed.add_dog(i)
            breed.dogs_count()
        
        return self.breeds, self.dogs

        """
        You must get breeds and dogs data from our API: http://dogs.magnet.cl

        We recommend using the Dog and Breed classes to store
        the information, also consider the dogs and breeds fields
        of the DogHouse class to perform data manipulation.
        """
        
        #raise NotImplementedError

    def get_total_breeds(self) -> int:
        total_breeds = len(self.breeds)
        return total_breeds

        """
        Returns the amount of different breeds in the doghouse
        """
        #raise NotImplementedError

    def get_total_dogs(self) -> int: 
        total_dogs = len(self.dogs)
        return total_dogs

        """
        Returns the amount of dogs in the doghouse
        """
        #raise NotImplementedError

    def get_common_breed(self) -> Breed:
        dict_count = {}
        for i in self.dogs: 
            key = str(i.breed)
            if not key in dict_count:
                dict_count[key] = 1
            else:
                dict_count[key] += 1
        frecuency = 0
        for number in dict_count:
            if dict_count[number] > frecuency:
                the_most_repeated_numbr = number
                frecuency = dict_count[number]
        count = dict_count[str(the_most_repeated_numbr)]
        #print(
        #        f"El número que más se repite es {the_most_repeated_numbr} (encontrado {count} ocasiones)"
        #        )
        for i in self.breeds:
            if int(the_most_repeated_numbr) == i.id:                
                return i

                
                     
        """
        Returns the most common breed in the doghouse
        """
        raise NotImplementedError

    def get_common_dog_name(self) -> str:
        dict_count = {}
        for i in self.dogs:
            key = str(i.name)
            if not key in dict_count:
                dict_count[key] = 1
            else:
                dict_count[key] += 1
        frecuency = 0
        
        for number in dict_count:
            if dict_count[number] > frecuency:
                the_most_repeated_numbr = number
                frecuency = dict_count[number]
        count = dict_count[str(the_most_repeated_numbr)]
        #print(
        #        f"El nombre que más se repite es {the_most_repeated_numbr} (encontrado {count} ocasiones)"
        #        )

        return the_most_repeated_numbr 
        
        
        
        
                     

        """
        Returns the most common dog name in the doghouse
        """
        raise NotImplementedError

    def send_data(self, data: dict, token: str):
        r = post('http://dogs.magnet.cl/api/v1/',data=data, token = token)
        

        """
        You must send the answers obtained from the implemented
        methods, the parameters are defined in the documentation.

        Important!! We don't tell you if the answer is correct
        """
        #raise NotImplementedError
