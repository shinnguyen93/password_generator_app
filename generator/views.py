from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random
import string

# Create your views here.
def index(request):
   if request.method == "POST":
      alphabet_string = string.ascii_lowercase
      alphabet_list = list(alphabet_string)

      alphabet_upper = string.ascii_uppercase
      alphabet_list_upper = list(alphabet_upper)

      if request.POST.get('uppercase'):
         alphabet_list.extend(alphabet_list_upper)

      if request.POST.get('special'):
         alphabet_list.extend(list('!@#$%&*?'))

      if request.POST.get('number'):
         alphabet_list.extend(list('!@#$%&*?'))

      length = int(request.POST.get('length'))

      thepassword = ''

      for x in range(length):
         thepassword += random.choice(alphabet_list)

      return render(request,'generator/index.html',{"password":thepassword})
   else:
      return render(request,'generator/index.html')