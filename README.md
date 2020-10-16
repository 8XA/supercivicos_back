# supercivicos_back

# Para correr el servidor:

pip install virtualenv\
cd ruta_del_repositorio_clonado/supercivicos_back\
virtualenv -p python3 supercivicosENV\
source supercivicosENV/bin/activate\
pip install -r requirements.txt\
cd scbackend\
./manage.py runserver

# Endpoint GET:
http://localhost:8000/empresas/ \
El mismo enlace le permite hacer POST

# O si prefiere la terminal:
pip install httpie\
El paquete httpie sirve para hacer GET o POST como en los siguientes ejemplos:\
http POST http://localhost:8000/empresas/ nombre = "fulanito" empresa = "fulanitos inc." responsable = "fulanito2" ... etc\
http GET http://localhost:8000/empresas/

Es posible que httpie se instale en el home de usuario, en tal caso las rutas son:\
~/.local/bin/http POST http://localhost:8000/empresas/ nombre = "fulanito" empresa = "fulanitos inc." responsable = "fulanito2" ... etc\
~/.local/bin/http GET http://localhost:8000/empresas/
