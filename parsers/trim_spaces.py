def trim_spaces(str):
    while (str[0]==' ') | (str[-1]==' '):
        if str[0]==' ': str = str[1:]
        if str[-1]==' ': str = str[:-1]
    return str