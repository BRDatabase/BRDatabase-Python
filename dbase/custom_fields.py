from django import forms
from django.db import models

class LocationField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.to_python(value)

    def to_python(self, value):
        if value is None or isinstance(value, (list, tuple)):
            return value

        # Assuming value is a string in the format "x,y"
        try:
            x, y = map(float, value.split(','))
            return {'latitude': x, 'longitude': y}
        except (ValueError, TypeError):
            return value

    def get_prep_value(self, value):
        if value is None:
            return value
        return f"{value['latitude']},{value['longitude']}"

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': LocationFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class LocationFormField(forms.MultiValueField):
    def __init__(self, **kwargs):
        fields = (
            forms.FloatField(),
            forms.FloatField(),
        )
        super().__init__(fields, **kwargs)

    def compress(self, data_list):
        if data_list:
            return {'latitude': data_list[0], 'longitude': data_list[1]}
        return None

class LocationWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(attrs={'placeholder': 'X-coordinate'}),
            forms.TextInput(attrs={'placeholder': 'Y-coordinate'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value['latitude'], value['longitude']]
        return [None, None]
