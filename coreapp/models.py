from django.db import models
from django.forms import ModelForm
from django.core.validators import MinLengthValidator


class Contact(models.Model):
    name = models.CharField(
            max_length=35,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Shows up in the admin list
    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at',)

