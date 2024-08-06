# Tach Challenge

## Descripción
Este proyecto consiste en dos microservicios desarrollados con Python y Sanic para la gestión de cuentas y transacciones. Los microservicios se despliegan utilizando Docker y Docker Compose, y utilizan MongoDB como base de datos.

## Microservicios
- Accounts Service: Maneja la creación y gestión de cuentas.
- Transactions Service: Maneja la gestión de transacciones entre cuentas.

## Estructura del proyecto
```
/microservices-challenge
    /accounts-service
        /app
            __init__.py
            models.py
            routes.py
            services.py
            utils.py
        .env
        Dockerfile
        main.py
        requirements.txt
    /transactions-service
        /app
            __init__.py
            models.py
            routes.py
            services.py
            utils.py
        .env
        Dockerfile
        main.py
        requirements.txt
    docker-compose.yml
    README.md
    tach-challenge.md
```

## Requisitos Previos
- Docker
- Docker Compose
- Python 3.9 o superior
- MongoDB

## Configuración de variables de entorno
Dentro de cada archivo .env como se ilustra en la estructura debe contener lo siguiente:
```
MONGO_URI=mongodb:URL de MongoDB
ACCOUNT_API_URL=URL del servidor de Sanic del microservicio de cuentas
```

(Aclaración: la variable de entorno **ACCOUNT_API_URL**, solo debe estar en el archivo .env del microservicio de transferencias, en el de cuentas no es necesaria) 

## Instrucciones para Ejecutar los Microservicios
### Paso 1: Clonar el Repositorio
```sh
git clone https://github.com/YagoMaureira/Microservices-Challenge.git
cd microservices-challenge
```

### Paso 2: Construir y Ejecutar los Contenedores
```sh
docker-compose up --build
```

## Documentación de la API
### Accounts Service
#### Crear Cuenta
- URL: /accounts
- Método: POST
- Descripción: Crea una nueva cuenta.
Cuerpo de la Solicitud:

```json
{
  "cvu": "cvu de 22 digitos numericos",
  "name": "User1",
  "email": "user1@example.com",
  "balance": 500.0
}
```

#### Obtener Cuenta
- URL: /accounts/cvu
- Método: GET
- Descripción: Obtiene los detalles de una cuenta por su CVU.

#### Actualizar Cuenta
- URL: /accounts/cvu
- Método: PUT
- Descripción: Actualiza los valores de una cuenta por su CVU.

Cuerpo de la Solicitud:

```json
{
  "name": "User1",
  "email": "user1@example.com",
  "balance": 500.0
}
```

#### Borrar Cuenta
- URL: /accounts/cvu
- Método: DELETE
- Descripción: Elimina una cuenta por su CVU.

### Transactions Service
#### Crear Transacción
- URL: /transactions
- Método: POST
- Descripción: Crea una nueva transacción entre dos cuentas.

Cuerpo de la Solicitud:
```json
{
  "sender_cvu": "CVU de 22 digitos numericos",
  "receiver_cvu": "CVU de 22 digitos numericos",
  "amount": 100.0
}
```

#### Obtener Transacciones por CVU
- URL: /transactions/cvu/cvu
- Método: GET
- Descripción: Obtiene todas las transacciones asociadas a un CVU específico.

## Consideraciones de Diseño
#### Patrón de Diseño Utilizado
Para la creación de la instancia del objeto Sanic, se ha implementado el Factory Pattern. Esto permite una fácil configuración y escalabilidad de los microservicios.