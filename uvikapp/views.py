from django.shortcuts import render, redirect

from uvikapp.forms import GameForm
from uvikapp.models import Game

case1 = {'players': 2, 'squares': 8, 'cards': 13, 'sequence': 'RYGPBRYGBRPOP', 'cardList': 'R,B,GG,Y,P,B,P,RR'}
case2 = {'players': 2, 'squares': 6, 'cards': 5, 'sequence': 'RYGRYB', 'cardList': 'R,YY,G,G,B'}
case3 = {'players': 3, 'squares': 9, 'cards': 6, 'sequence': 'QQQQQQQQQ', 'cardList': 'Q,QQ,Q,Q,QQ,Q'}


def index(request):
	test_case = request.GET.get('case')

	if test_case:
		if test_case == '1':
			form = GameForm(initial=case1)
		elif test_case == '2':
			form = GameForm(initial=case2)
		elif test_case == '3':
			form = GameForm(initial=case3)
		else:
			form = GameForm()
	else:
		form = GameForm()
	return render(request, 'index.html', {'form': form})


def game(request):
	if request.method == 'POST':
		form = GameForm(request.POST)
		if form.is_valid():
			players = form.cleaned_data.get('players')
			squares = form.cleaned_data.get('squares')
			cards = form.cleaned_data.get('cards')
			sequence = form.cleaned_data.get('sequence')
			cardList = form.cleaned_data.get('cardList')

			result = get_game_result(players, sequence, cardList)

			game = Game(players=players, squares=squares, cards=cards, sequence=sequence, cardList=cardList,
						result=result)
			game.save()

			return render(request, 'index.html', {'form': form, 'game': Game.objects.last()})

	return redirect('index')


def get_game_result(number_of_players, board_sequence, cards_in_deck):
	_cards = [item.strip() for item in cards_in_deck.split(',')]
	_players = range(1, number_of_players + 1)
	_player_position = dict((x, -1) for x in _players)

	for index, player, cards in player_deck_generator(_players, _cards):
		for card in cards:
			position = _player_position[player]
			_find = board_sequence.find(card, position + 1)
			if _find < 0 or _find == len(board_sequence) - 1:
				return 'Player {0} won after {1} cards.'.format(player, index + 1)
			_player_position[player] = _find

	return 'No player won after {0} cards.'.format(len(_cards))


def player_deck_generator(player, deck):
	player_index = 0
	deck_index = 0

	while deck_index < len(deck):

		if player_index >= len(player):
			player_index = 0

		yield (deck_index, player[player_index], deck[deck_index])

		player_index += 1
		deck_index += 1
