from django.shortcuts import render, HttpResponse 
from .forms import verify_form

def index(request):
    if request.method == 'POST': 
        form = verify_form(request.POST) 
        
        if form.is_valid(): 
            return HttpResponse("Yay! you are human.") 
        else: 
            return HttpResponse("OOPS! Bot suspected.") 
            
    else: 
        form = verify_form()  
        return render(request, 'captcha/index.html', {'form':form})



