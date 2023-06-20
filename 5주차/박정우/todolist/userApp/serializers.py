from rest_framework.serializers import Modelserializers
from userApp.models import User

class UserSerializer(Modelserializers):
    class Meta:
        model = User
        fields = "__all__"