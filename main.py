from game import Game, GameValidations, Player


def main():
    game = Game()
    game_validations = GameValidations(game)
    player = Player(game)

    # for i in range(2):
    #     while True:
    #         name_player = input(f"Digite o nome do player {i + 1}: ")
    #         if validate_player_name(name_player):
    #             player = Player(name_player, game)
    #             break

    # 

    while True:
        game.start_game()
        game.show_rating()
        i = 0
        while i < 9:
            game.start_round()
            for player_index, player in enumerate(game.players):
                while True:
                    print("{:-^40s}".format("-"))
                    print("{:*^40s}".format(f"Jogador {player_index}"))
                    print("{:-^40s}".format("-"))
                    field_index = input("Digite um campo de 0 à 8 para marcar.")

                    if game_validations.validate_field_index(field_index):
                        game.player_move(player, field_index)
                        i += 1
                        break
                    else:
                        pass
                if game_validations.validate_winner(player.points):
                    break
            if game_validations.validate_winner(player.points):
                game.end_round()
                break
        if game_validations.validate_winner(player.points):
            game.end_game()
            break


main()
