from itertools import chain, combinations


class Game:

    '''
    Crie um objeto Game para operar e gerenciar um jogo da velha.

    Atributos:
        field_values       (iterable): Nome do cliente.
        game_round         (int): Cpf do cliente. Deve ser passado com pontos e traços.
        players            (iterable): Saldo do cliente.
        circles_points     (iterable): Número da agencia do cliente.
        squares_points     (iterable): Número da conta do cliente.
    '''

    field_points = [2, 7, 6, 9, 5, 1, 4, 3, 8]


    @staticmethod
    def powerset(iterable): # Retorna um objeto com todas as combinações dos valores de um iterable.
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


    def __init__(self):
        self.field_values = [None, None, None, None, None, None, None, None, None]
        self.game_round = 0
        self.players = []
        self.winner = None
        self.circles_points = []
        self.squares_points = []


    def add_player(self, player):
        assert len(self.players) < 2
        self.players.append(player)
        print(f"Player {player.get_player_name()} foi adicionado ao jogo!")


    def _set_players_team(self):
        self.players[0].team = "Circles"
        self.players[1].team = "Squares"


    def get_player_by_id(self, id_player):
        for player in self.players:
            if player.id == id_player:
                return player


    def show_rating(self):
        for player in self.players:
            print("{:-^40s}".format("-"))
            print("{:*^40s}".format(f"Player {player.name}"))
            print("{}".format(f"Vitórias: {player.wins}"))
            print("{}".format(f"Derrotas: {player.defeats}"))
            print("{:-^40s}".format("-"))


    def start_game(self):
        self._set_players_team()
        print("O jogo começou!")


    def _add_point(self, team, field):
        if player.team == "Circles":
            self.circles_points.append(self.field_points[field])
        elif player.team == "Squares":
            self.squares_points.append(self.field_points[field])


    def player_move(self, player, field):
        field = int(field)
        self.field_values[field] = player.team
        self._add_point(player, field)
        print(f"O campo {field} foi marcado para o time {player.team} com sucesso.")


    def _is_winner(self, points_list):
        if self.game_round >= 3:
            combinations_list = self.powerset(points_list)
            for combination in combinations_list:
                if len(combination) == 3:
                    if sum(combination) == 15:
                        return True 


    def check_winner(self):
        players_scores = [self.circles_points, self.squares_points]
        for index, player_score in enumerate(players_scores):
            print(index, player_score)
            if self._is_winner(player_score):
                self.winner = self.get_player_by_id(index + 1)
                return True


    def start_round(self):
        self.game_round += 1
        print("{:-^60s}".format("-"))
        print("{:*^60s}".format(f"Round {self.game_round}"))
        print("{:-^60s}".format("-"))


    def end_round(self):
        if self.winner:
            print("{:-^40s}".format("-"))
            print("{:*^40s}".format(f"Jogador 1 wins!"))
            print("{:*^40s}".format(f" ＼(°o°)／ Parabêns {self.winner.name} ＼(°o°)／ "))
            print("{:-^40s}".format("-"))
            return True

    def end_game(self):
        if self.winner:
            print("{:-^40s}".format("-"))
            print("{:*^40s}".format("O jogo acabou"))
            print("{:-^40s}".format("-"))
            return True


class Player:

    id = 1

    def __init__(self, name, game):
        self.id = Player.id
        self.name = name
        self.team = None
        self.wins = None
        self.defeats = None
        Player.id += 1
        game.add_player(self)

    def get_player_name(self):
        name = self.name
        return str(name)
