from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task


# Create your views here.

# def home(request):
#     tasks_objects = Task.objects.all()
#     tasks_list = [f'<li>{t.title}: {t.text}</li>' for t in tasks_objects]
#     result = ''.join(tasks_list)
#
#     if not result:
#         result = "There are no tasks created!"
#
#     html = f'''
#     <h1>It Works!</h1>
#     <ul>
#         {result}
#     </ul>
# '''
#     return HttpResponse(html)

def home(request):

    context = {
        'title': 'It Works from view!',
        'tasks': Task.objects.all(),
    }

    return render(request, 'home.html', context)