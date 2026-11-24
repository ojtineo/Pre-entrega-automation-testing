import requests

def test_obtener_usuario(base_url,headers):
    url = f"{base_url}/users/7"

    response = requests.get(url,headers=headers)

    # Niveles de validación
    # Nivel 1: Status code
    codigo = response.status_code
    #print(codigo)
    assert codigo == 200

    # Nivel 2: Headers
    assert "application/json" in response.headers["Content-Type"]
    
    # Nivel 3: Escritura
    data = response.json()
    #print(data)
    assert isinstance(data,dict) #Validar que el contenido sea un diccionario
    assert "data" in data
    assert isinstance(data["data"],dict)

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # Nivel 4: Contenido
    assert data["data"]["id"]  == 7
    assert data["data"]["email"] == "michael.lawson@reqres.in"

    # NIvel 5: Tiempo de respuesta
    assert response.elapsed.total_seconds() <2

#test_obtener_usuario()

def test_crear_usuario(base_url,headers):
    url = f"{base_url}/users/"
    
    usuario = {
        "email":"ojtineo@gmail.com",
        "first_name":"Osmar",
        "last_name":"Tineo",
        "job":"alumno"
    }

    response = requests.post(url,headers=headers,json=usuario)

    #print(response.json())

    # Nivel 1
    assert response.status_code == 201

    # Nivel 2
    assert "application/json" in response.headers["Content-Type"]

    # Nivel 3
    data = response.json()
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "id" in data

    # Nivel 4
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]
    assert data["last_name"] == usuario["last_name"]

    # Nivel 5
    assert response.elapsed.total_seconds() <2

def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users7"

    response = requests.delete(url,headers=headers)

    # Nivel 1 Status Code
    assert response.status_code ==204

    # Novel 2 Headers
    assert "Content-Type" not in response.headers

    # Nivel 3 y 4 Estructura y Contenido
    assert response.content == b""
    #assert len(response.content) == 0 otra opción para validar

    # NIvel 5 Tiempo de Respuesta
    assert response.elapsed.total_seconds() <2


    """
    {
        "data":{
            "id":3,
            "email":"ojtineo@gmail.com",
            "nombre":"Osmar",
            "apellido":"Tineo"
        },
        "support":{

        }
    }
    """