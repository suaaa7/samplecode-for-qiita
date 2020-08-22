def concat(str1: str, str2: str):
    if not isinstance(str1, str) and isinstance(str2, str):
        raise TypeError

    return str1 + str2
