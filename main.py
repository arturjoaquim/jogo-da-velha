from game import Game, Player

game = Game()

for i in range(2):
    name_player = input(f"Digite o nome do player {i + 1}: ")
    player = Player(name_player, game)

game.start_game()
game.show_rating()
game.next_round()

i = 0
while i < 9:

	for player in game.players:
		while True:
			if i >= 9:
				break

			print("{:-^40s}".format("-"))
			print("{:*^40s}".format(f"Jogador {player.id}"))
			print("{:-^40s}".format("-"))
			if game.player_move(player, input("Digite um campo de 0 à 8 para marcar.")):
				i += 1
				# print(i)
				break
			else:
				pass
	game.next_round()
	if game.check_winner():
		break



print("{:-^40s}".format("-"))
print("{:*^20s}".format("O jogo acabou"))
print("{:-^40s}".format("-"))