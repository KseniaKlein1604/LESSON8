import requests

class ProjectApi:
    BASE_URL = "https://your-yougile-api-url.com/api-v2/projects"
    HEADERS = {
        "Authorization": "Bearer your_token",
        "Content-Type": "application/json"
    }

    @classmethod
    def create_project(cls, name, description):
        payload = {
            "name": name,
            "description": description
        }
        response = requests.post(cls.BASE_URL, json=payload, headers=cls.HEADERS)
        return response

    @classmethod
    def update_project(cls, project_id, name):
        payload = {
            "name": name
        }
        response = requests.put(f"{cls.BASE_URL}/{project_id}", json=payload, headers=cls.HEADERS)
        return response

    @classmethod
    def get_project(cls, project_id):
        response = requests.get(f"{cls.BASE_URL}/{project_id}", headers=cls.HEADERS)
        return response