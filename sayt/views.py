from django.shortcuts import render

from sayt.models import Contact


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        date = requests.POST.get('date')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email, date=date
        )

        ctx = {
            "contact": index,

        }
    return render(requests, "index.html", ctx)