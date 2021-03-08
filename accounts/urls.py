from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # http POST localhost:8000/accounts/api-token-auth/ username=youme password=user1234
    # http localhost:8000/post/ "Authorization: Token 52dbeb747c60a55ee3d27c5546eb22bb733215ce"
    path("api-token-auth/", obtain_auth_token),
]
