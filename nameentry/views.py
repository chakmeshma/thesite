from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Person
import json


@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            parsed_entry_data = json.loads(request.body)
            if 'first_name' not in parsed_entry_data or 'last_name' not in parsed_entry_data: raise ValueError

            new_name = Person(first_name=parsed_entry_data['first_name'], last_name=parsed_entry_data['last_name'])
            new_name.save()
        except ValueError:
            raise SuspiciousOperation("Invalid JSON")

    names = Person.objects.all()
    return render(request, 'entries_list.html', {'names_list': names})
