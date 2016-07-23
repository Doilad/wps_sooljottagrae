from django import forms
from posts.models import Post
from tags.models import AlcoholTag, FoodTag, PlaceTag


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'image', 'alcohol_name', 'food_name', 'place_name',)
