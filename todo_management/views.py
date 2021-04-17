from rest_framework.response import Response
from .ser import TodoSerializer,TodoPostSerializer
from .models import Todo
from rest_framework import status
from rest_framework.views import APIView
from django.db import connection
from rest_framework.permissions import AllowAny
from todo.utils import dictfetchall,dictfetchone,execute
from django.http import JsonResponse
# Create your views here.



class TodoList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # posts = Todo.objects.all()

        data = execute(
            'select user_id,username,task from todo t left join users u on t.user_id=u.id',
            many=False
            )
        print(data)
        # data = dictfetchall(data)
        # with connection.cursor() as cursor:
        #     cursor.execute("select user_id,username,task from todo t left join users u on t.user_id=u.id")
        #     posts = dictfetchall(cursor)


        # posts = Todo.objects.raw('select * from todo')

        # serializer = TodoSerializer(posts,many=True)
        return JsonResponse({'data':data},status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        print(type(request.data))

        serializer = TodoPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data

           
            return Response(data, status=status.HTTP_201_CREATED)
        error=""
        for i in serializer.errors:
            error = serializer.errors.get(i)[0].replace('This',i)
            break
        return Response({'msg':error}, status=status.HTTP_400_BAD_REQUEST)
