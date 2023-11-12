from django.forms import ModelForm
from .models import Drawing

class FileUploadForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['imgfile']