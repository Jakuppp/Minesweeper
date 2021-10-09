def transform_input(input: str) -> tuple:
    try:
        x, dot, y = input.partition('.')
        out = (int(x), int(y))
        return out
    except Exception as err:
        print(err)