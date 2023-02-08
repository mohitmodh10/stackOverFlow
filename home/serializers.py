from rest_framework import serializers
from .models import UserModel,MyPost
from django.contrib.auth.hashers import make_password


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPost
        fields =['id',
                  'text', 'location', 'posted_on',
                  'number_of_votes','voted_by','author']


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only = True)
    class Meta:
        model = UserModel
        fields = ['id','last_login','is_superuser','is_staff','is_active','date_joined','first_name','last_name','email','posts','password']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    def create(self, validated_data):
        user = UserModel(
        email=validated_data['email'],
        first_name = validated_data['first_name'],
        last_name = validated_data['last_name'],
        password = make_password(password=validated_data['password'],hasher='default', salt=None),)
        user.save()
        return user
