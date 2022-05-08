from rest_framework import generics
from django.http import HttpResponseRedirect
from .serializer import RegisterSerializer
from django.urls import reverse


# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponseRedirect(reverse("token_obtain_pair"))
