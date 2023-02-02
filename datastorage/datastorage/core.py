from django.http import JsonResponse, HttpResponse
from datastorage.models import MultiValuedData
from django.shortcuts import render
import json


def view(request):
    print(list(MultiValuedData.objects.all().values()))
    return render(request, 'view.html', {"rows": MultiValuedData.objects.all().values()})


def getJSON(request):
    if request.method == "GET":
        return render(request, 'text.html')
    else:
        try:
            json_data = json.loads(request.POST['json'])
            for data_source, data_type_dict in json_data.items():
                if type(data_type_dict) != dict:
                    continue
                for data_type, data in data_type_dict.items():
                    to_store = MultiValuedData()
                    to_store.user_id = json_data['user']
                    to_store.data_source = data_source
                    to_store.data_type = data_type
                    to_store.data = data
                    to_store.save()
        except Exception as e:
            return JsonResponse({"": e.args})
    return JsonResponse({"Done": "Done"})

# {
#         "user": 1210,
#         "address": {
#             "postal": "1230 Cityline Apt 2111, Richardson, Texas, 75081",
#             "billing": "5612 Waterview Apt 190, Richardson, Texas, 75080",
#             "mailing": "5612 City Apt 190, Richardson, Texas, 75084"
#         },
#         "phone_number": {
#             "home": "+19739354411",
#             "office": "+19129311144"
#         }
#     }
