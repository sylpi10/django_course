from django.shortcuts import render
from peoplebook.peoples import people

# Create your views here.
def users_list(request, display='small'):
   context = {
        'display': display,
        'users' : people
   }
   return render(request, "peoplebook/list.html", context)


def users_detail(request, name):
  context = {
    'user' : people[name],
  }
  return render(request, "peoplebook/detail.html", context)



