from rest_framework import serializers
from reg_empresa.models import Empresas

class RegEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Empresas
            fields = ['empresa','responsable','calle','num_exterior',
            'num_interior','colonia','ciudad','pais','CP','email','telefono','contrasena']
