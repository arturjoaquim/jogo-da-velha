from game import Game, GameValidations, Player


game = Game()
game_validations = GameValidations(game)

for i in range(2):
    Player(game)

# game.start_game()

while True:  # Passar o front para pygame
    if (not game.math_in_progress):
        game.start_math()
        game.show_rating()
    game.start_round()
    for player in game.players:
        while True:
            game.show_message(f"Jogador {player.id}")
            field_index = input("Digite um campo de 0 à 8 para marcar.")

            if game_validations.validate_field_index(field_index):
                player.move(field_index)
                break
        if game_validations.validate_winner(player.points):
            game.show_message(f"Jogador {player.id} wins",
                              f" ＼(°o°)／ Parabéns {player.team} ＼(°o°)／ ")
            game.set_players_status(player)
            break
    if game_validations.is_game_over():
        game.show_message("A partida acabou")
        play_again = input("Deseja continuar jogando? [S/N]")
        if play_again.upper() == "S":
            game.reset_game()
        else:
            game.show_message("Obrigado por jogar <3")
            break
