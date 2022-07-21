from rest_framework import serializers, viewsets
from app1.models import User, Meeting, Reserve


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReserveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserve
        fields = ['id', 'reserve_userid', 'meeting_id_id', 'reserve_time', 'update_time']


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    meeting_id = serializers.StringRelatedField(many=True)

    class Meta:
        model = Meeting
        fields = ['id', 'meeting_name', 'create_userid', 'update_userid', 'create_time', 'update_time', 'is_delete',
                  'meeting_id']


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer



