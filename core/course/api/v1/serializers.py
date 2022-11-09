from copyreg import pickle
from ...models import Course , RegisteredUser
from rest_framework import serializers
from account.models import User
from ...models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course

        fields = [
            'name',
            'category',
            'description',
            'price',
                  ]


class RegistereSerializer(serializers.ModelSerializer):
   
    class Meta:
         model = RegisteredUser


         fields = (
             'identification_card',
             'picture',
             'course',
             #'user'
                   )



    def create(self, validated_data ):
        print(validated_data)
        user = User.objects.get(id = self.context.get('request').user.id)
       # course = Course.objects.get(id = self.context['pk'])
        validated_data['user'] = user
       # validated_data['course'] = course 
        return super().create(validated_data)