from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
import aftership
import requests
import trackingmore



trackingmore.set_api_key('1b17d38c-bbf4-4313-a71d-569b566bc08a')



def InputForm(request):
    return render(request, 'trackapp/InputForm.html')

def Result(request):
    name = request.GET.get('name')
    email = request.GET.get('emf')
    track_number1=request.GET.get('trn')
    company = request.GET.get('company')


    for item in trackingmore.get_all_trackings()["data"]["items"]:
        if item["tracking_number"]==track_number1:
            trackingmore.delete_tracking_item(company, track_number1)
    td= trackingmore.create_tracking_data(company,track_number1)
    track_data = trackingmore.realtime_tracking(td)
    #return JsonResponse(track_data, safe=False)
    track_info1= track_data["items"][0]["origin_info"]["trackinfo"]
    lis = []
    for item1 in track_info1:
        lis.append(item1)

    context = {

        'track_number':track_data["items"][0]["tracking_number"] ,
        'current_status':track_data["items"][0]["status"],
        'last_event': track_data["items"][0]["lastEvent"],
        #'track_info':track_data["items"][0]["origin_info"]["trackinfo"]
        'lis': lis ,
        'name':name,
    }


   #context = { 'lis' :[1,2,3,5,7]}

    return render(request, 'trackapp/Result.html', context)





