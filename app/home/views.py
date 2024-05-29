from user.models import Profile
from django.shortcuts import render
from django.http import HttpResponse

from analysis.models import Analysis
from course.models import Course

# Create your views here.

def index(request):
    user_id = request.user.id
    courses = Course.objects.all().order_by("-date_created")[:7]
    analysis = Analysis.objects.filter(user_id=user_id).order_by("-date_created")[:7]
    users = Profile.objects.all()
    # weight_dates = map(lambda x: x.date_created, analysis)
    # print(weight_dates)
    top = {
        'users': len(users),
        'weight': analysis[0].weight if len(analysis) > 0 else 0,
        'calories': analysis[0].calories_pd if len(analysis) > 0 else 0,
        'courses': len(courses),
    }
    # Page from the theme
    return render(request, 'pages/index.html', {'courses': courses, 'analysis': analysis, 'top': top}) 
    # return render(request, 'pages/index.html', {'courses': courses, 'analysis': {
    #     'weight': {
    #         'dates': weight_dates
    #     }
    # }})
