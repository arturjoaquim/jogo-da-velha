def validate_field(field_list, field):
    try:
        field = int(field)
    except (ValueError):
        print("Digite valores inteiros para preencher um campo.")
        return False

    if field >= 0 and field <= 8:
        if field_list[field] == None:
            return True
        else:
            print("Este campo já foi preenchido.")
            return False
    else:
        print("O valor do campo precisa estar entre 0 e 8.")
        return False


def validate_player_name(player_name):
    if len(player_name) >= 3 and len(player_name) <= 20:
        if player_name.isalnum():
            return True
        else:
            print("Seu nome só pode ter caracteres alfanúmericos.")
    else:
        print("Seu nome precisa ter de 3 à 20 caracteres.")
        return False
