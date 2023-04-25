from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Medcard,mkb
from .forms import MedcardForm
from django.views.generic import DetailView,UpdateView, DeleteView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from first.utils import render_to_pdf
# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)  
            return redirect('medcard')
        else:
            messages.info(request,'Неыерный логин или пароль')

    context = {}
    return render(request, 'first/sign_in.html', context)

def logoutuser(request):
    logout(request)
    return redirect('sign_in')


@login_required(login_url='sign_in')
def mainpage(request):
    return render(request, 'first/mainpage.html')

@login_required(login_url='sign_in')
def addcard(request):
    error = ''
    if request.method == 'POST':  
        form = MedcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('medcard')
        else:
            error = 'неверные данные' 

    form = MedcardForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'first/addcard.html', data)

@login_required(login_url='sign_in')
def medcard(request):
    card = Medcard.objects.order_by('-datetime')
    return render(request, 'first/medcard.html', {'card':card})


@method_decorator(login_required(login_url='sign_in'), name='dispatch')
class CardDetailView(DetailView):
    model = Medcard
    template_name = 'first/student.html'
    context_object_name = 'medcard'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        datetime = self.object.datetime
        now = datetime.now(datetime.tzinfo)
        if now - datetime < timedelta(hours=24):
            context['can_edit'] = True
        else:
            context['can_edit'] = False
        return context

@method_decorator(login_required(login_url='sign_in'), name='dispatch')    
class CardUpdateView(UpdateView):
    model = Medcard
    template_name = 'first/addcard.html'
    form_class = MedcardForm

@method_decorator(login_required(login_url='sign_in'), name='dispatch')
class CardDeleteView(DeleteView):
    model = Medcard
    diag = Medcard.diagnosis
    template_name = 'first/deletecard.html'
    success_url = '/students/medcard/'

@login_required(login_url='sign_in')
def Mkb_10(request):
    mkb10 = mkb.objects.all()
    return render(request, 'first/mkb10.html', {'mkb10':mkb10})

@login_required(login_url='sign_in')
def searchcard(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        cardname = Medcard.objects.filter(iin__contains = searched)
        return render(request, 'first/searchcard.html',{'searched': searched, 'cardname':cardname})
    else:
        return render(request, 'first/searchcard.html',{})

@login_required(login_url='sign_in')    
def searchmkb(request):
    if request.method == 'POST':
        searchedmkb = request.POST['searchedmkb']
        mkb10 = mkb.objects.filter(name__iregex = searchedmkb)
        return render(request, 'first/searchmkb.html',{'searchedmkb': searchedmkb, 'mkb10':mkb10})
    else:
        return render(request, 'first/searchmkb.html',{})
    

class GeneratePdf(DetailView):
    model = Medcard
    template_name = 'first/direction.html'
    context_object_name = 'stud_data'