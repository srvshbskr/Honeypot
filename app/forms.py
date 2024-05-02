from django.forms import ModelForm,HiddenInput,CharField
from .models import User

class userForm(ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'
    
    # hidden = CharField(widget=HiddenInput() ,required=False )

    def __init__(self, *args, **kwargs):
        super(userForm, self).__init__(*args, **kwargs)
        self.fields['hidden'].initial = "some_value"  
