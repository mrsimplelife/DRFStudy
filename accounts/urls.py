from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

urlpatterns = [
    # http POST localhost:8000/accounts/api-token-auth/ username=youme password=user1234
    # http localhost:8000/post/1/ "Authorization: Token 52dbeb747c60a55ee3d27c5546eb22bb733215ce"
    path("api-token-auth/", obtain_auth_token),
    # http POST localhost:8000/accounts/api-jwt-auth/ username=youme password=user1234
    path("api-jwt-auth/", obtain_jwt_token),
    # http localhost:8000/post/1/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InlvdW1lIiwiZXhwIjoxNjE1MjA5NDY0LCJlbWFpbCI6IiJ9.1JUxz5bF6wZwbmH1ju5Nb_1mdYqpPbdPjj3lnw72UcI"
    path("api-jwt-auth/verify/", verify_jwt_token),
    # http POST localhost:8000/accounts/api-jwt-auth/refresh/ token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InlvdW1lIiwiZXhwIjoxNjE1MjA5NDY0LCJlbWFpbCI6IiJ9.1JUxz5bF6wZwbmH1ju5Nb_1mdYqpPbdPjj3lnw72UcI
    path("api-jwt-auth/refresh/", refresh_jwt_token),
]