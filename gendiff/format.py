def format(data, plain=False):
    if isinstance(data, dict):
        return "[complex value]"
    match data:
        case True:
            return "true"
        case False:
            return "false"
        case None:
            return "null"
        case _:
            if isinstance(data, int) or isinstance(data, float):
                return str(data)
            return f"'{str(data)}'" if plain else str(data)
