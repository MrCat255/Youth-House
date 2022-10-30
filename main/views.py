from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Applications


# Create your views here.


class Send(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # user = request.query_params['user']
        name = str(request.data["name"])
        tel = str(request.data["tel"])
        email = str(request.data["email"])
        date = request.data["date"]
        activity = int(request.data["activity"])
        print(name)
        print(tel)
        print(email)
        print(date)
        print(activity)

        v = Applications()
        v.name = str(name)
        v.tel = tel
        v.email = email
        v.date = date
        v.hall = int(activity)

        v.save()

        return Response()
