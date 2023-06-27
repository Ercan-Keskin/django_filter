# rest framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

# my imports
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from .paginations import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination
  

class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination
    filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields= ['first_name', 'last_name', 'number']
    search_fields = ['first_name', 'last_name', 'number', 'id']
    
    
class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    pagination_class = CustomPageNumberPagination
    
