from rest_framework import serializers
from .models import RequestConstraint
from CustomUser.models import User
Q
class RequestConstraintSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = RequestConstraint
        fields = ('owner', 'examname', 'date', 'time', 'longitude', 'latitude')

    def create(self, validated_data):
        Eid = exame
        sid = Exame + Dtae + time
        admitid = id
        lat =
        long =

        if owner =
            return
