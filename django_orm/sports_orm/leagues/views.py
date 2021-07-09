from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count

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
		# all leagues with a current player named Sophia
		# "leagues": League.objects.filter(teams__curr_players__first_name__icontains="Sophia"),
		# "teams": Team.objects.all(),
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
		# all teams in the Atlantic Soccer conference
		# "teams": Team.objects.filter(league__name='Atlantic Soccer Conference'),
		# all teams with a current player named Sophia
		# "teams": Team.objects.filter(curr_players__first_name__icontains="Sophia"),
		# all teams, past and present that Samuel Evans has played with
		# "teams": Team.objects.filter(Q(all_players__first_name__icontains="Samuel"), Q(all_players__last_name__icontains="Evans")),
		# every team that Jacob Gray played for before he joined the Oregon Colts
		# "teams": Team.objects.filter(Q(all_players__first_name__icontains="Jacob"), Q(all_players__last_name__icontains="Gray"), ~Q(team_name__iexact="Colts"), ~Q(location__iexact="Oregon")),
		# all teams that have had 12 or more players, past and present
		"teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gt=12),
		# "players": Player.objects.all(),
		# all current players on the Boston Penguins
		# "players": Player.objects.filter(Q(curr_team__team_name="Penguins"), Q(curr_team__location="Boston")),
		#  all current players in the International Collegiate Baseball Conference
		# "players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		# all current players in the American Conference of Amateur Football w/ last name Lopez
		# "players": Player.objects.filter(Q(curr_team__league__name="American Conference of Amateur Football"), Q(last_name__iexact="Lopez")),
		# all football players
		# "players": Player.objects.filter(curr_team__league__sport__icontains="football"),
		# every player with last name "Cooper"
		# "players": Player.objects.filter(last_name__iexact="cooper"),
		# every player with first name "Joshua"
		# "players": Player.objects.filter(first_name__iexact="joshua"),
		# every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		# "players": Player.objects.filter(last_name__iexact="cooper").exclude(first_name__iexact="joshua"),
		# all players with first name "Alexander" OR first name "Wyatt"
		# "players": Player.objects.filter(Q(first_name__iexact="alexander") | Q(first_name__iexact="wyatt")),
		# everyone with the last name Flores who does not currently play for the Washington Roughriders
		# "players": Player.objects.filter(Q(last_name__icontains="Flores"), ~Q(curr_team__team_name__icontains='Roughriders')),
		# all players, past and present, with the Manitoba Tiger-Cats
		# "players": Player.objects.filter(all_teams__team_name__iexact="Tiger-Cats"),
		# all players who were formerly (but aren't currently) with the Wichita Vikings
		# "players": Player.objects.filter(Q(all_teams__team_name__iexact="Vikings"), Q(all_teams__location__iexact="Wichita"), ~Q(curr_team__team_name__iexact="Vikings"), ~Q(curr_team__location__iexact="Wichita")),
		# everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		# "players": Player.objects.filter(Q(first_name__iexact="joshua"), Q(all_teams__league__name__icontains="Amateur Baseball Players")),
		# all players and count of teams played for, sorted by the number of teams they've played for
		"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('-num_teams'),
	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")