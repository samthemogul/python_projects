from math import ceil, log, floor

def from_datetime_to_string(datetime_object):
    return datetime_object.strftime("%Y-%m-%dT%H:%M:%SZ")

def power_of_two(value):
    return (ceil(log(value, 2)) == floor(log(value, 2)))

def compute_round_name(game_count):
    input_type = type(game_count)
    if input_type is int or input_type is float or (input_type is str and game_count.isnumeric()):
        if int(game_count) == 1:
            return 'Final'
        if int(game_count) == 2:
            return 'Semi-Finals'
        if int(game_count) == 4:
            return 'Quarter-Finals'

        return f'Round of {game_count * 2}'

    raise TypeError(f"{game_count} must be a number or a string we can convert to a number")


