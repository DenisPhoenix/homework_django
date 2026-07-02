from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.forms import BooleanField, ImageField

from .models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs.update(
                    {
                        "class": "form-check-input",
                    }
                )
            else:
                fild.widget.attrs.update(
                    {
                        "class": "form-control",
                    }
                )


class ProductForm(StyleFormMixin, forms.ModelForm):
    image = ImageField(
        validators=[FileExtensionValidator(allowed_extensions=["JPEG", "PNG"])]
    )

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

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            megabyte_limit = 5.0
            if image.size > megabyte_limit * 1024 * 1024:
                raise ValidationError(
                    f"Размер файла не должен превышать {megabyte_limit} МБ"
                )
        return image
