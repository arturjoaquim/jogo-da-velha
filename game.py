from itertools import chain, combinations


class Game:

    points = [2, 7, 6, 9, 5, 1, 4, 3, 8]

    @staticmethod
    def show_message(*messages):
        print("{:-^60s}".format("-"))
        for message in messages:
            print("{:-^60s}".format(message))
        print("{:-^60s}".format("-"))

    def __init__(self):
        self.fields = [None, None, None, None, None, None, None, None, None]
        self.players = []
        self.math_in_progress = False
        self.round = 0

    def _set_players_team(self):  # Mudar funcionalidade
        for player in self.players:
            # self.show_message(f"Player {player.id}, escolha seu time [X/0].")
            team_player = input(
                f"Player {player.id}, escolha seu time [squares/circles].")
            player.team = team_player

    def show_rating(self):
        for player in self.players:
            self.show_message(
                f"Player {player.id}",
                f"Vitórias: {player.wins}",
                f"Derrotas: {player.defeats}")

    def start_math(self):
        self.show_message("A partida começou", "Escolha de times")
        self.math_in_progress = True
        self._set_players_team()
    
    def start_round(self):
        self.round += 1
        self.show_message(f"Round {self.round}")

    def _add_point(self, player, field_index):
        point = self.points[field_index]
        player.points.append(point)
        self.fields[field_index] = player.team

    def reset_game(self):
        self.round = 0
        self.fields = [None, None, None, None, None, None, None, None, None]
        self.math_in_progress = False
        for player in self.players:
            player.status = None
            player.points = []
            player.team = None
    
    def set_players_status(self, winner_player):
        for player in self.players:
            if player == winner_player:
                player.status = "winner"
                player.wins += 1
            else:
                player.status = "loser"
                player.defeats += 1


class GameValidations():

    @staticmethod
    # Retorna um objeto com todas as combinações dos valores de um iterable.
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(
            combinations(
                s, r) for r in range(
                len(s) + 1))

    def __init__(self, game) -> None:
        self.game = game

    def validate_field_index(self, field_index):
        try:
            field_index = int(field_index)
        except (ValueError):
            print("Digite valores inteiros para preencher um campo.")
            return False

        if field_index >= 0 and field_index <= 8:
            if not self.game.fields[field_index]:
                return True
            else:
                print("Este campo já foi preenchido.")
                return False
        else:
            print("O valor do campo precisa estar entre 0 e 8.")
            return False

    def validate_winner(self, points_list):
        # if self.round >= 3:
        combinations_list = self.powerset(points_list)
        for combination in combinations_list:
            if len(combination) == 3:
                if sum(combination) == 15:
                    return True

    def is_game_over(self):
        players_status = [player.status for player in self.game.players]
        if "winner" in players_status or self.game.round > 9:
            return True

    # def validate_player_name(player_name):
    #     if len(player_name) >= 3 and len(player_name) <= 20:
    #         if player_name.isalnum():
    #             return True
    #         else:
    #             print("Todos os caracteres precisam ser alfanuméricos.")
    #     else:
    #         print("Seu nome precisa ter de 3 à 20 caracteres.")
    #         return False


class Player():

    id = 1

    def __init__(self, game):
        self.game = game
        self.points = []
        self.status = None
        self.team = None
        self.wins = 0
        self.defeats = 0
        self.id = Player.id
        Player.id += 1
        game.players.append(self)

    def move(self, field_index):
        # if game_validations.validate_field_index(field_index):
        field_index = int(field_index)
        self.game.fields[field_index] = self.team
        self.game._add_point(self, field_index)
        print(
            f"O campo {field_index} foi marcado para o time {self.team} com sucesso.")


if __name__ == "__main__":
    game = Game()
    game_validations = GameValidations(game)
    for i in range(2):
        Player(game)

    game.players[0].status = "winner"

    if game_validations.is_game_over():
        print("Oi")
    else:
        print("Ola")
