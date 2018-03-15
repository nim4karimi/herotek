from django.urls import path , re_path , include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import ApiTest


class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiTest
        fields = ('name','decription')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ApiViewSet(viewsets.ModelViewSet):
    queryset = ApiTest.objects.all()
    serializer_class = ApiSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'apitest', ApiViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]