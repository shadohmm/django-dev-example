from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.


def index(request):
    web_list=AccessRecord.objects.order_by('date')
    date_dict={'access_rec':web_list}
    return render(request,'index.html',context=date_dict)
