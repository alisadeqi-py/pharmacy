from os import stat
from django.shortcuts import  get_object_or_404 
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView
from .serializers import CourseSerializer ,RegistereSerializer 
from ...models import Course
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import (
                                        HTMLFormRenderer, 
                                        JSONRenderer, 
                                        BrowsableAPIRenderer,
                                    )

class CourseList(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(status = True)


class CourseDetail(RetrieveAPIView):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class RegisterCourse(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegistereSerializer
    queryset = Course.objects.filter(status = True)



'''class RegisterCourse(CreateAPIView):
    serializer_class = RegistereSerializer
    queryset = Course.objects.all()'''

'''class RegisterCourse(APIView):
 
    def get(self, request , id):
        course = get_object_or_404(Course , pk = id , status = True )
        serializer_class = RegistereSerializer(course)
        return Response(serializer_class.data)
    def post(self, request , id):

        reg_user = {
             'identification_card' : request.data.get('identification_card') ,
             'picture' : request.data.get('picture')
             
        }
    
        serializer  = RegistereSerializer(data = reg_user , many=True , 
        #context = {'pk' : id}
        )  
        
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.data)'''
