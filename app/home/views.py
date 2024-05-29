from django.shortcuts import render
from django.http import HttpResponse

from analysis.models import Analysis
from course.models import Course

# Create your views here.

def index(request):
    user_id = request.user.id
    courses = Course.objects.all()
    analysis = Analysis.objects.filter(user_id=user_id).order_by("-date_created")[:7]
    weight_dates = map(lambda x: x.date_created, analysis)
    print(weight_dates)
    # Page from the theme
    return render(request, 'pages/index.html', {'courses': courses, 'analysis': analysis}) 
    # return render(request, 'pages/index.html', {'courses': courses, 'analysis': {
    #     'weight': {
    #         'dates': weight_dates
    #     }
    # }})
