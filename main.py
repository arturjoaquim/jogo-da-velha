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

    # game.start_game()

    loop = True

    while loop:
        i = 0
        game.show_rating()
        while i < 9:
            game.start_round()
            for player in game.players:
                while True:
                    print("{:-^40s}".format("-"))
                    print("{:*^40s}".format(f"Jogador {player.id}"))
                    print("{:-^40s}".format("-"))
                    field_index = input("Digite um campo de 0 à 8 para marcar.")

                    if game_validations.validate_field_index(field_index):
                        game.player_move(player, field_index)
                        i += 1
                        break
                    else:
                        pass
                if game.check_winner(): break
            if game.end_round(): break
        loop = game.end_game()


main()
