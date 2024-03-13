from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        
        extra_kwargs = {
            'password': {'write_only' : True} #password should not be returned to the user
        }
        
        # we overide the default create function by creating our own so that we can modify how data is stored in the db.
        def create(self, validated_data):
            password = validated_data.pop('password', None)  # we extract the field with password from validated_data
 
            instance = self.Meta.model(**validated_data) #Validated_data without the popped password

            if password is not None:
                instance.set_password(password) #Why did we use instance to set password

            instance.save()
            return instance
