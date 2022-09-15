import requests

class Get_page():
    """Ссылка на которую будет идти запрос"""
    url = "https://reqres.in/api/users"

    def get_users_page2(self):
        """Подаем запрос"""
        response = requests.get(self.url + "?page=2")
        """Проверям статус ответа"""
        assert response.status_code == 200
        print(response)
        data_page2 = [{'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson',
                       'avatar': 'https://reqres.in/img/faces/7-image.jpg'},
                      {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson',
                       'avatar': 'https://reqres.in/img/faces/8-image.jpg'},
                      {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke',
                       'avatar': 'https://reqres.in/img/faces/9-image.jpg'},
                      {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields',
                       'avatar': 'https://reqres.in/img/faces/10-image.jpg'},
                      {'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards',
                       'avatar': 'https://reqres.in/img/faces/11-image.jpg'},
                      {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell',
                       'avatar': 'https://reqres.in/img/faces/12-image.jpg'}]
        """Использем разные типы проверок полученных данных"""
        assert response.json().get('data') == data_page2
        print("Полученные данные верны")
        assert response.json().get('total_pages') is not None
        print("Общее количество страниц не равны None")
        assert response.json().get('page') == 2
        print("Открыта страница номер: " + str(response.json().get('page')))
        assert type(response.json().get('total')) == int
        print("total имеет тип данных int")
        assert 'email' in response.json().get('data')[1]
        assert '@' in response.json().get('data')[1]['email']
        print("email валиден")
        print("Test 'GET' passed")


