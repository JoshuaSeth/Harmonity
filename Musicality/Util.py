def Contains(list, name):
    for item in list:
        if item.name == name:
            return True
    return False