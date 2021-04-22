from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip
import bcrypt


def index(request):
    return render(request, 'index.html')


def create(request):

    if request.method == "POST":

        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        hash_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/user/dashboard')
    return redirect("/")


def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/user/dashboard')
        messages.error(request, "Email or password are invalid.")

    return redirect("/")


def dashboard(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')

    context = {
        'logged_user': User.objects.get(id=request.session['logged_user']),
        'trips': Trip.objects.all(),
        'other_trip': Trip.objects.exclude(user=request.session['logged_user'])



    }
    return render(request, 'dashboard.html', context)


def newtrip(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')

    context = {
        'logged_user': User.objects.get(id=request.session['logged_user'])
    }
    return render(request, 'newtrip.html', context)


def createtrip(request):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    if request.method == "POST":

        errors = Trip.objects.trip_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/trips/new')

        current_user = User.objects.get(id=request.session['logged_user'])

        new_trip = Trip.objects.create(
            dest=request.POST['dest'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            plan=request.POST['plan'],
            user=current_user



        )
        return redirect('/user/dashboard')


def deletetrip(request, trip_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    trip_delete = Trip.objects.get(id=trip_id)
    trip_delete.delete()
    return redirect('/user/dashboard')


def editform(request, trip_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')

    context = {
        'logged_user': User.objects.get(id=request.session['logged_user']),
        'trip': Trip.objects.get(id=trip_id),

        'trip_id': trip_id
    }
    return render(request, 'edit.html', context)


def updatetrip(request, trip_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first!")
        return redirect('/')
    if request.method == "POST":

        errors = Trip.objects.trip_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/trips/edit/{trip_id}')

        current_trip = Trip.objects.get(id=trip_id)
        current_trip.dest = request.POST['dest']
        current_trip.start_date = request.POST['start_date']
        current_trip.end_date = request.POST['end_date']
        current_trip.plan = request.POST['plan']

        current_trip.save()

        return redirect('/user/dashboard')


def tripinfo(request, trip_id):
    context = {
        'logged_user': User.objects.get(id=request.session['logged_user']),
        'trips': Trip.objects.get(id=trip_id),

    }
    return render(request, 'tripinfo.html', context)


def jointrip(request, trip_id):
    user = User.objects.get(id=request.session['logged_user'])
    this_trip = Trip.objects.get(id=trip_id)
    user.join_trip.add(this_trip)
    return redirect('/user/dashboard')


def canceltrip(request, trip_id):
    user = User.objects.get(id=request.session['logged_user'])
    this_trip = Trip.objects.get(id=trip_id)
    user.join_trip.remove(this_trip)
    return redirect('/user/dashboard')


def logout(request):
    request.session.flush()
    return redirect('/')
