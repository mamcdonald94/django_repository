from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		# find all baseball leagues
		# "leagues": League.objects.filter(sport__iexact="baseball"),
		# find all women's leagues
		# "leagues": League.objects.filter(name__icontains="women"),
		# find all hockey leagues
		# "leagues": League.objects.filter(sport__icontains="hockey"),
		# find all non-football leagues
		# "leagues": League.objects.exclude(sport__icontains='football'),
		# find all leagues that call themselves conferences
		# "leagues": League.objects.filter(name__icontains="conference"),
		# find all leagues in the Atlantic region
		# "leagues": League.objects.filter(name__icontains="atlantic"),
		"teams": Team.objects.all(),
		# find all teams in Dallas
		# "teams": Team.objects.filter(location__icontains='dallas'),
		# all teams named raptors
		# 'teams': Team.objects.filter(team_name__icontains='raptors'),
		# all teams whose location includes city
		# "teams": Team.objects.filter(location__icontains='city'),
		# all teams whose names begin with T
		# "teams": Team.objects.filter(team_name__istartswith='t'),
		# all teams, ordered alphabetically by location
		# "teams": Team.objects.order_by('location'),
		# all teams, ordered by team name in reverse alphabetical order
		# "teams": Team.objects.order_by('team_name').reverse(),
		"players": Player.objects.all(),
		# every player with last name "Cooper"
		# "players": Player.objects.filter(last_name__iexact="cooper"),
		# every player with first name "Joshua"
		# "players": Player.objects.filter(first_name__iexact="joshua"),
		# every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		# "players": Player.objects.filter(last_name__iexact="cooper").exclude(first_name__iexact="joshua"),
		# all players with first name "Alexander" OR first name "Wyatt"
		# "players": Player.objects.filter(Q(first_name__iexact="alexander") | Q(first_name__iexact="wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")