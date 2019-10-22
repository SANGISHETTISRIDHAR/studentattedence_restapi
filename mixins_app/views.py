from django.shortcuts import render
from .serializers import TeacherSerializer,Studentserializer,Attendenceserializer
from .models import Teacher,Student,Atendence
from rest_framework import mixins,generics
# Create your views here.

class Teacherlist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class =TeacherSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class Teacherdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class =TeacherSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)
class Studentlist(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get(self,request):
       return self.list(request)
    def post(self,request):
       return self.create(request)
class Studentdeails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

class Attendeclist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Atendence.objects.all()
    serializer_class = Attendenceserializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class Attendedetails(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Atendence.objects.all()
    serializer_class = Attendenceserializer
    def get(self, request,pk):
        # lookup_field=pk
        return self.retrieve(request,)
    def put(self, request,pk):
        # lookup_field = pk
        return self.update(request)

    def delete(self, request,pk):
        # lookup_field = pk
        return self.destroy(request)

