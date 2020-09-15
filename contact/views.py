
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactViews(CreateView):

    model = Contact
    form_class = ContactForm
    success_url = "/"