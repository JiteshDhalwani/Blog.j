from django import forms

#Forms
CATEGORY_CHOICES = [
    ("None", "None"),
    ("Tech", "Tech"),
    ("Health", "Health"),
    ("Sports", "Sports"),
    ("Business", "Business"),
    ("Finance", "Finance"),  
]
class CreateBlogForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    image_caption = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)