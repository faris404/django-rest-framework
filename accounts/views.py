
from rest_framework.response import Response
from .ser import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utils import generate_access_token, generate_refresh_token



class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user.has_perm('todo_management.single_view'))
        print(request.user.has_perm('todo_management.add_todo'))

        user = request.user
        serialized_user = UserSerializer(user).data
        return Response({'user': serialized_user })


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        # @api_view(['POST'])
        # @permission_classes([AllowAny])
        # @ensure_csrf_cookie

        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()
        if (username is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'username and password required')

        user = User.objects.filter(username=username).first()
        if(user is None):
            raise exceptions.AuthenticationFailed('user not found')
        if (not user.check_password(password)):
            raise exceptions.AuthenticationFailed('wrong password')

        serialized_user = UserSerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }

        return response




class Signup(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:

            User = get_user_model()
            # username = request.data.get('username')
            password = request.data.pop('password')
            print(password)
            response = Response()
            # if (username is None) or (password is None):
            #     raise exceptions.AuthenticationFailed(
            #         'username and password required')

            user = User.objects.create(**request.data)
            user.set_password(password)
            user.groups.set([1])
            user.save()
            # if(user is None):
            #     raise exceptions.AuthenticationFailed('user not found')
            # if (not user.check_password(password)):
            #     raise exceptions.AuthenticationFailed('wrong password')

            serialized_user = UserSerializer(user).data

            # access_token = generate_access_token(user)
            # refresh_token = generate_refresh_token(user)

            # response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
            response.data = {
                'user': serialized_user,
            }

            return response

        except Exception as e:
            return Response(data=e.args)
