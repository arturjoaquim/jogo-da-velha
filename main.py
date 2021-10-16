from game import Game, GameValidations, Player


game = Game()
game_validations = GameValidations(game)

for i in range(2):
    Player(game)

while True: # Passar o front para pygame
    game.start_game()
    game.show_rating()
    breaker = False
    while game.round < 9 and not breaker:
        game.start_round()
        for player_index, player in enumerate(game.players):
            while True:
                game.show_message(f"Jogador {player_index}")
                field_index = input("Digite um campo de 0 à 8 para marcar.")

                if game_validations.validate_field_index(field_index):
                    player.move(field_index)
                    game.round += 1
                    break
            if game_validations.validate_winner(player.points):
                print(player)
                game.show_message("Jogador 1 wins", f" ＼(°o°)／ Parabêns {player.team} ＼(°o°)／ ")
                breaker = True
                break

