""" serializer for recipe api """

from rest_framework import serializers

from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id','title','time_minutes','description','price','link']
        read_only_fields = ['id']