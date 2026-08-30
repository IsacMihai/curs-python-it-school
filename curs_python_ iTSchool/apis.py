'''API - REST APIs

API = Application Programming Interface

REST APIs = Representational State Transfer Application Programming Interface

- modalitate de comunicare intre diferite sisteme prin internet
- se foloseste protocolul HTTP
'''

'''
HTTP = HyperText Transfer Protocol
    - limbaj folosit de calculatoare pentru a comunica pe internet
    - se bazeaza pe principul REQUEST - RESPONSE
        Exemplu: Cand deschidem o pagina web, calculatorul nostru trimite un REQUEST folosind HTTP catre server,
                 iar serverul trimite inapoi un raspuns (text, imagini, video pe care le vedem)

    Exemplu:
    GET /index.html HTTP/1.1
    Host: www.example.com

    HTTP/1.1 200 OK
    Content-Type: text/html

Analogie referitoare la REST APIs:
Cand mergem la un restaurant (CLIENT) comandam mancare de la ospatar (API) care plaseaza comanda
la bucatarie (SERVER), iar apoi de la bucatarie aduce inapoi mancarea (DATA).
'''

'''
Concepte cheie:
    CLIENT       = Sistemul care trimite requestul (browserul nostru de web sau aplicatia web)
    SERVER       = Sistemul care proceseaza requestul si trimite inapoi datele
    RESOURCE     = Orice tip de data
    ENDPOINT     = O cale (path) URL folosit pentru a accesa o resursa
    HTTP Methods = Actiuni pe care le putem face cu o resursa
'''

'''
Metodele HTTP principale in REST:
    GET    - Citeste date            -> Exemplu: GET    URL/users   => ne returneaza toti userii
    POST   - Creeaza date            -> Exemplu: POST   URL/users   => creeaza un nou user
    PUT    - Modifica date existente -> Exemplu: PUT    URL/users/5 => modifica userul cu id-ul 5
    DELETE - Sterge date             -> Exemplu: DELETE URL/users/5 => sterge userul cu id-ul 5
'''

'''
Exemplu de REST API Endpoint pentru un blog:
GET    www.blog.com/posts   -> returneaza o lista cu articolele postate pe blog
GET    www.blog.com/posts/1 -> returneaza articolul cu ID 1
POST   www.blog.com/posts   -> creeaza un nou articol
PUT    www.blog.com/posts/1 -> face update la articolul cu ID 1
DELETE www.blog.com/posts/1 -> sterge articolul cu ID 1
'''

# # pip install requests
import requests
# # url = 'https://restcountries.com/v3.1/name/romania?fields=capital,region'
# url = 'https://restcountries.com/v3.1/name/romania'
# response = requests.get(url)
# json_response = response.json()
# # print(json_response[0]['capital'][0])
# # print(json_response[0]['region'])
# # population, currencies
# print(json_response[0]['population'])
# print(json_response[0]['currencies'])

base_url = 'http://127.0.0.1:5000'

# reponse = requests.get(base_url)
# json_response = reponse.json()
# print(json_response)

# response = requests.get(f'{base_url}/students')
# json_response = response.json()
# print(json_response)

# for student in json_response:
#     if student['math'] > 8:
#         print(student)

# find_cnp = '123451'
# response = requests.get(f'{base_url}/students/{find_cnp}')
# json_response = response.json()
# print(json_response)

# data = {
#     'cnp': 100100,
#     'firstname': 'Gogu',
#     'lastname': 'Marinescu',
#     'rom': 5,
#     'math': 5,
#     'engl': 7
# }
# response = requests.post(f'{base_url}/students', json=data)
# print(response.json())

# data = {
#     'cnp': 100100,
#     'firstname': 'Gogu',
#     'lastname': 'Marinescu',
#     'rom': 10,
#     'math': 5,
#     'engl': 7
# }
# response = requests.put(f'{base_url}/students', json=data)
# print(response.json())

# response = requests.delete(f'{base_url}/students/100100')
# print(response.json())
