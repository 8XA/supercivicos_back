# supercivicos_back

# Para correr el servidor:

pip install virtualenv\
cd supercivicos_back\
virtualenv -p python3 supercivicosENV\
source supercivicosENV/bin/activate\
pip install -r requirements.txt\
cd scbackend\
python manage.py runserver

# Endpoint GET:
http://localhost:8000/empresas/ \
El mismo enlace le permite hacer POST
# Ejemplo:
    {
        "empresa": "fulanitos inc.",
        "responsable": "Mangano, Perengano",
        "calle": "avenida fulana",
        "num_exterior": "23",
        "num_interior": "2",
        "colonia": "fulana",
        "ciudad": "fulana",
        "pais": "mangano",
        "CP": 00000,
        "email": "fulano@mangano.com",
        "telefono": 5124587415,
        "contrasena": "asd123"
    }

# O si prefiere la terminal:
pip install httpie\
El paquete httpie sirve para hacer GET o POST como en los siguientes ejemplos:\
http POST http://localhost:8000/empresas/ empresa="fulanitos inc." responsable="fulanito2" calle="avenida fulanita" num_exterior="23" num_interior="2" colonia="fulanita" ciudad="fulanita" pais="manganito" CP=00000 email="fulanito@manganito.com" telefono=5412548965 contrasena="asd123"\
http GET http://localhost:8000/empresas/

Es posible que httpie se instale en el home de usuario, en tal caso las rutas son:\
~/.local/bin/http POST http://localhost:8000/empresas/ empresa="fulanitos inc." responsable="fulanito2" calle="avenida fulanita" num_exterior="23" num_interior="2" colonia="fulanita" ciudad="fulanita" pais="manganito" CP=00000 email="fulanito@manganito.com" telefono=5412548965 contrasena="asd123"\
~/.local/bin/http GET http://localhost:8000/empresas/
