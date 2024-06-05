from .models import User
from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    
    token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email', 
            'age',
            'asset',
            'password',
            'token',
            ]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# class UserUpdateSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ('email','asset')




# class CustomRegisterSerializer(RegisterSerializer):
#     phone_number = serializers.IntegerField()
#     date_of_birth = serializers.DateField()

#     def save(self, request):
#         user = super().save(request)
#         user.phone_number = self.data.get('phone_number')
#         user.date_of_birth = self.data.get('date_of_birth')
#         user.save()
#         return user

# class UserSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email = validated_data['email'],
#             username = validated_data['username'],
#             password = validated_data['password'],
#             age = validated_data['age'],
#             asset = validated_data['asset'],
#         )
#         return user
#     class Meta:
#         model = User
#         fields = ['age', 'email', 'username', 'password','asset']