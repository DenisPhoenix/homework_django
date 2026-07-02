from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name = self.cleaned_data.get("name")
        name_words = [
            word.strip(".,!?;:()\"'") for word in name.lower().split()
        ]
        for name_word in name_words:
            if name_word in forbidden_words:
                raise ValidationError("Эти слова запрещены в названии")
        return name

    def clean_description(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        description = self.cleaned_data.get("description")
        description_words = [
            word.strip(".,!?;:()\"'") for word in description.lower().split()
        ]
        for description_word in description_words:
            if description_word in forbidden_words:
                raise ValidationError("Эти слова запрещены в описании")
        return description
