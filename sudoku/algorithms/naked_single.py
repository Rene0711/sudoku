def naked_single(values):
    for key, value in values.items():
        if len(value.options) == 1:
            return key
    return False
