from django.http import JsonResponse
from datastorage.models import MultiValuedData


def view(request):
    return JsonResponse({"": list(MultiValuedData.objects.values())})


def processJSON(request):
    jsonData = {
        "user": 1205,
        "address": {
            "postal": "1230 Cityline Apt 2111, Richardson, Texas, 75081",
            "billing": "5612 Waterview Apt 190, Richardson, Texas, 75080"
        },
        "phone_number": {
            "home": "+19739354411",
            "office": "+19129311144"
        }
    }
    try:
        for data_source, data_type_dict in jsonData.items():
            if type(data_type_dict) != dict:
                continue
            for data_type, data in data_type_dict.items():
                to_store = MultiValuedData()
                to_store.user_id = jsonData['user']
                to_store.data_source = data_source
                to_store.data_type = data_type
                to_store.data = data
                to_store.save()
    except Exception as e:
        return JsonResponse({"": e.args})
    return JsonResponse({"Done": "Done"})
