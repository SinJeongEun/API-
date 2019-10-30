from .models import Post
from rest_framework import serializers

class PostSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #field = '__all__'
        fields = ['id', 'title','body'] 
        write_only_fields = ('title',)

    