from django.forms import ModelForm
from . import models


class InfoForm(ModelForm):


    class Meta:
        fields = ['first_name','last_name','email_addresse','phone_number']
        model = models.Info