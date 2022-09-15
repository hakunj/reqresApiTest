import requests


class Post_page():
    url = "https://reqres.in/api/users"

    # body_example = {"name": "Morpheus", "job": "leader"}

    def post_user(self, body):
        response = requests.post(self.url, json=body)
        print(response)
        assert response.status_code == 201
        print("Код - " + str(response.status_code))
        assert response.json().get('name') == "Morpheus"
        print("Имя нового пользователя - " + response.json().get('name'))
        assert response.json().get('job') == "leader"
        print("Должность нового пользователя - " + response.json().get('job'))
        print("Test POST passed.")

