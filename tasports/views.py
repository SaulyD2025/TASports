from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, SelectTeamsForm, LoginForm
from .models import Game, Teams
import datetime, requests

User = get_user_model()

def home(request):
    API_KEY = "1bf0507e-6f74-4380-ae3d-2319491da73b"
    headers = {"Authorization": API_KEY}
    date = datetime.date.today().strftime('%Y-%m-%d')
    BASE_URL = f"https://api.balldontlie.io/v1/games?start_date={date}&per_page=75"
    usergames = []
    if request.user.is_authenticated:
        response = requests.get(BASE_URL, headers=headers)
        if response.status_code == 200:
            games = response.json()['data']

            for game in games:
                homenick = game['home_team']['name']
                homeid = game['home_team']['id']
                awaynick = game['visitor_team']['name']
                awayid = game['visitor_team']['id']
                time = game['datetime']
                Game.objects.update_or_create(
                    hometeam_name=homenick,
                    hometeam_id=homeid,
                    awayteam_name=awaynick,
                    awayteam_id=awayid,
                    fulldatetime=time
                )
            for game in Game.objects.all():
                matchedhometeam = Teams.objects.get(id=game.hometeam_id)
                matchedawayteam = Teams.objects.get(id=game.awayteam_id)
                game.hometeam_src = matchedhometeam.logopath
                game.awayteam_src = matchedawayteam.logopath
                game.save()

            for team in request.user.favouriteteams.all():
                for game in Game.objects.all():
                    if team.id == game.hometeam_id or team.id == game.awayteam_id:
                        usergames.append(game)

        return render(request, 'loggedinhome.html', {'usergames':usergames})

    else:
        response = requests.get(BASE_URL, headers=headers)
        games = response.json()['data']
        if response.status_code == 200:
            for game in games:
                homenick = game['home_team']['name']
                homeid = game['home_team']['id']
                awaynick = game['visitor_team']['name']
                awayid = game['visitor_team']['id']
                time = game['datetime']
                Game.objects.update_or_create(
                    hometeam_name=homenick,
                    hometeam_id=homeid,
                    awayteam_name=awaynick,
                    awayteam_id=awayid,
                    fulldatetime=time
                )
                for game in Game.objects.all():
                    matchedhometeam = Teams.objects.get(id=game.hometeam_id)
                    matchedawayteam = Teams.objects.get(id=game.awayteam_id)
                    game.hometeam_src = matchedhometeam.logopath
                    game.awayteam_src = matchedawayteam.logopath
                    game.save()

        else:
            errmessage = "404"
            return errmessage

        return render(request, 'loggedouthome.html', {'Games':Game.objects.all()})

def loginview(request):
    errmessage = ''
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            errmessage = "This user does not exist."
    return render(request, 'login.html', {'errmessage': errmessage, 'form' : form})

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('teamselection')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def teamselection(request):
    if request.method == 'POST':
        form = SelectTeamsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SelectTeamsForm()
    return render(request, 'teamselection.html', {'form': form})

# Create your views here.
