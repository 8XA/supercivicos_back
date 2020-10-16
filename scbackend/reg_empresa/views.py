from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reg_empresa.models import Empresas
from reg_empresa.serializers import RegEmpresaSerializer

@api_view(['GET','POST'])
def empresas_lista(request):
    if request.method == 'GET':
        empresas = Empresas.objects.all()
        serializer = RegEmpresaSerializer(empresas, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegEmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
