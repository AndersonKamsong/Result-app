import json
import requests

from .constants import SERVER_URL

class Course:
    ROUTER = "/api/subject/"

    def __init__(self, id=None, title=None, teacher_id=None):
        self.id = id
        self.title = title
        self.teacher_id = teacher_id

    def save(self):
        if (self.id):
            # ENDPOINT = "updateTeache/"
            url = f"{SERVER_URL}{__class__.ROUTER}{ENDPOINT}{self.id}"
            method = "PUT"
        else:
            payload = {
                'id': self.id,
                'title': self.title,
                'teacher_id': self.teacher_id}
            headers = {}
            ENDPOINT = "createSubject"
            url = f"{SERVER_URL}{__class__.ROUTER}{ENDPOINT}"
            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)

    def read(id=None):
        ENDPOINT= "getAllSubject"
        url = f"{SERVER_URL}{__class__.ROUTER}{ENDPOINT}"
        payload={}
        headers = {}
        
        response = requests.request("GET", url, headers=headers, data=payload)
        
        print(response.text)
    def delete(self):
        ENDPOINT="deleteSubject/"
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception:
            raise exception