from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        #Includes all the attributes from the Room model
        fields ='__all__' 
        exclude=['host','participants']
        
class UserForm(ModelForm):
    class Meta:
        model= User
        fields = ['username']