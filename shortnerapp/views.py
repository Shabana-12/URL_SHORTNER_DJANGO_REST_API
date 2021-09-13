
from django.shortcuts import render,redirect
from rest_framework.response import Response
from . models import Shortener
from . serializers import TodoSerializer
from rest_framework.views import APIView

from django.views import View
from django.conf import settings
# Create your views here.
class ListTodoAPIView(APIView):
    def get(self,request):
        todos = Shortener.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
class TodoDetailAPIView(APIView):
    def get(self,request,pk):
        todos = Shortener.objects.get(id=pk)
        serializer = TodoSerializer(todos, many=False)
        return Response(serializer.data)
class CreateTodoAPIView(APIView):
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class UpdateTodoAPIView(APIView):
    def post(self,request,pk):
        todo = Shortener.objects.get(id=pk)
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class DeleteTodoAPIView(APIView):
    def get(self,request,pk):
        todo = Shortener.objects.get(id=pk)
        todo_instance = Shortener.objects.get(id=pk)
        todo_instance.delete()
        return Response('Deleted')
    
# class Redirector(View):
#     def get(self,request,shortener_link,*args, **kwargs):
#         shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
#         redirect_link=Shortener.objects.filter(short_url=shortener_link).first().long_url
#         return redirect(redirect_link)

    