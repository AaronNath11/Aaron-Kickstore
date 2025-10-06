from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
    
    def clean_title(self):
        nama = self.cleaned_data["nama"]
        return strip_tags(nama)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)