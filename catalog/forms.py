from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.forms import BooleanField, ImageField

from .models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class ProductForm(StyleFormMixin, forms.ModelForm):
    image = ImageField(
        label="Изображение",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])
        ],
        widget=forms.FileInput(attrs={"class": "form-control"}),
        required=False,
    )
    FORBIDDEN_WORDS = {
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    }

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        name_words = [
            word.strip(".,!?;:()\"'") for word in name.lower().split()
        ]
        for name_word in name_words:
            if name_word in self.FORBIDDEN_WORDS:
                raise ValidationError("Эти слова запрещены в названии")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        description_words = [
            word.strip(".,!?;:()\"'") for word in description.lower().split()
        ]
        for description_word in description_words:
            if description_word in self.FORBIDDEN_WORDS:
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
