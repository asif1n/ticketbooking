from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app1.models import Movie, Ticket
import datetime


# Create your views here.


def home(request):
    return render(request, 'base1.html')


def registration(request, **kwargs):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save(commit=True)

            return redirect(loginn)
        else:
            return render(request, 'register.html', {'form': f})
    else:
        f = UserCreationForm()
        return render(request, 'register.html', {'form': f})


def loginn(request):
    if request.method == "POST":
        t1 = request.POST['t1']
        t2 = request.POST['t2']
        user = authenticate(username=t1, password=t2)
        if user is not None:
            login(request, user)
            return redirect(ticket)
        return redirect(registration)
    else:
        return render(request, 'login.html')


# def changepassword(request):
#     if request.method == "POST":
#         t1 = request.POST['t1']
#         u = User.objects.get(username=t1)
#         u.set_password('new password')
#         u.save()
#     else:
#         return render(request, 'changepassword.html')


@login_required
def ticket(request):
    if request.method == 'POST':
        t2 = request.POST['t1']
        print(t2)
        print(type(t2))

        t3 = datetime.datetime.strptime(t2, '%Y-%m-%d')
        print(t3)
        print(type(t3))
        time = datetime.datetime.now()
        print(time)
        list1 = Movie.objects.filter(Date__exact=t3)
        return render(request, 'base.html', {'list1': list1, 'time': time})
    else:
        return render(request, 'base.html')


@login_required
def booking(request, *args, **kwargs):
    t = kwargs.pop("t")
    id = kwargs.pop("id")
    print(t, id)
    if int(t) == 11:
        t1 = int(t)
        k = str(t) + 'AM'
    else:
        t1 = int(t) + 12
        k = str(t) + 'PM'

    if request.method == 'POST':
        a = int(request.POST['t'])
        print(a)
        # p=int(request.POST['p'])
        # print(p)
        #
        total=0
        l = Ticket.objects.get(movie=id, time__hour=t1)
        print(l.Tickets ,a)
        if (l.Tickets >= a and l.Tickets > 0):
            l.Tickets = l.Tickets - a
            l.save()
            total =total+ a * 100
            print(total)
            state = "tickets are "
        # print(l.Tickets)
        elif (l.Tickets < a and l.Tickets > 0):
            state = "tickets are not avaliable as required"
            # total = 0

        else:
            state = "tickets are not avaliable"

            # total = 0

        return render(request, 'booking.html',
                      {'l': l, 'total': total, 'k': k, 'a': a, 'state': state})

    else:
        return render(request, 'booking.html')
