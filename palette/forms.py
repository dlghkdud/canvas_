from django import forms
from palette.models import Drawing, Comment


class DrawingForm(forms.ModelForm):
    class Meta:
        model = Drawing  # 사용할 모델
        fields = ['subject', 'content', 'imgfile', 'uploadedFile']  # QuestionForm에서 사용할 Question 모델의 속성

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 사용할 모델
        fields = ['content']  
