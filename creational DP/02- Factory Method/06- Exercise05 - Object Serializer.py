import json
from xml.etree.ElementTree import Element, SubElement, tostring

from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Serializer(ABC):

    @abstractmethod
    def serialize(self, person):
        pass 

class JsonSerializer(Serializer):
    def serialize(self, person):
        return json.dumps({"name": person.name, "age": person.age, "gender": person.gender})

class XmlSerializer(Serializer):
    def serialize(self, person):
        person_element = Element("person")
        name = SubElement(person_element, "name")
        name.text = person.name
        age = SubElement(person_element, "age")
        age.text = str(person.age)
        gender = SubElement(person_element, "gender")
        gender.text = person.gender
        return tostring(person_element, encoding="unicode")

class DictSerializer(Serializer):
    def serialize(self, person):
        return dict(name=person.name, age = person.age, gender = person.gender)


class SerializerFactory:

    @staticmethod 
    def create_serializer():
        serializers = dict(xml =XmlSerializer, json = JsonSerializer, dictionary = DictSerializer)

        while True:
            serializer_type = input("Serialize this Person Object: choose either json, xml or dictionary: ")

            if serializer_type in serializers:
                return serializers[serializer_type]()
            print('INVALID ENTRY: Enter either  json, xml or dictionary')

if __name__ == "__main__":
    person = Person("John Doe", 30, "Male")
    serializer = SerializerFactory.create_serializer()
    print(serializer.serialize(person))
