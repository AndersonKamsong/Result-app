import json
import requests

from .constants import SERVER_URL

class Teacher:
    ROUTER = "/api/teacher/"

    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        if (self.id):
            ENDPOINT = "updateTeacher/"
            url = f"{SERVER_URL}{__class__.ROUTER}{ENDPOINT}{self.id}"
            method = "PUT"
        else:
            payload = {
                'name': self.name,
                'email': self.email,
                'password': self.password}
            headers = {}
            ENDPOINT = "createTeacher"
            url = f"{SERVER_URL}{__class__.ROUTER}{ENDPOINT}"
            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)

    def read(id=None):
        ENDPOINT= "getAllTeacher"
        url = f"{SERVER_URL}{__class__.ROUTER}{ENDPOINT}"
        payload={}
        headers = {}
        
        response = requests.request("GET", url, headers=headers, data=payload)
        
        print(response.text)
    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception:
            raise exception