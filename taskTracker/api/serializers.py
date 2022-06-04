from rest_framework import serializers, viewsets
from api.models import User, Task, Team
from api.permissions import IsAllowedToPostOnlyToTL


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'user_role']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TaskSerializerForTL(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')

class TaskSerializerForTM(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name','team','status','started_at','completed_at','timestamp','url')
        read_only_fields = ('name','team','started_at','completed_at','timestamp','url')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    def get_serializer_class(self):
        if self.request.user.user_role == 'TL':
            return TaskSerializerForTL
        return TaskSerializerForTM
    permission_classes = [IsAllowedToPostOnlyToTL]