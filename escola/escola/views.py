from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework  import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttle import MatriculaAnonRateThrottle

class EstudanteViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Estudante.objects.all().order_by("id")
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]    
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]    
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class ListaMatriculaEstudante(generics.ListAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]    
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]    
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer
