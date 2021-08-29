
from rest_framework import serializers
from .models import GlobalUser, User, SpamScore


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','phone')


class GlobalUserSerializer(serializers.ModelSerializer):
    spamscore = serializers.SerializerMethodField()
    class Meta:
        model = GlobalUser
        fields = ('name', 'phone', 'spamscore')
    
    def get_spamscore(self, obj): 
        try:
            score = SpamScore.objects.get(phone=obj.phone).spam_score
        except:
            score = 0
        return score