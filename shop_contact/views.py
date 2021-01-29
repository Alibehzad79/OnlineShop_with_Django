from django.shortcuts import render


# Create your views here.
from shop_contact.forms import CreateContactForm
from shop_contact.models import Contact
from shop_settings.models import Information, WorkingHours


def contact(request):
    settings = Information.objects.first()
    working_hours = WorkingHours.objects.all()
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get("full_name")
        email = contact_form.cleaned_data.get("email")
        subject = contact_form.cleaned_data.get("subject")
        text = contact_form.cleaned_data.get("text")

        Contact.objects.create(full_name=full_name, email=email, subject=subject, text=text)

        contact_form = CreateContactForm()
    context = {
        "form": contact_form,
        "setting": settings,
        "working_hours": working_hours
    }
    return render(request, "contact/contact.html", context)
