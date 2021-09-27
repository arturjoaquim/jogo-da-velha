class Game:

    '''
    Crie um objeto Game para operar e gerenciar um jogo da velha.

    Atributos:
        field_values       (iterable): Nome do cliente.
        game_round         (int): Cpf do cliente. Deve ser passado com pontos e traços.
        players            (iterable): Saldo do cliente.
        _circles_points     (iterable): Número da agencia do cliente.
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
        self.game_round = None
        self.players = []
        self._circles_points = []
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


    def start_game(self):
        self._set_players_team()
        print("O jogo começou!")


    def player_move(self, player, field):
        field = int(field)
        if field >= 0 and field <= 8:
            if self.field_values[field] == None:
                self.field_values[field] = player.team
                print(f"O campo {field} foi marcado para o time {player.team} com sucesso.")
                return True
            else:
                print("Este campo já foi marcado")
                return False
        else:
            print("Digite um campo de 0 à 8.")
            return False


    def check_wins(self):
        if self.game_round == 3:
            pass


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
