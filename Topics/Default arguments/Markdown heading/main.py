def heading(text, level=1):
    if level <= 1:
        return '# ' + text
    elif level >= 6:
        return ('#' * 6) + ' ' + text
    else:
        return ('#' * level) + ' ' + text
