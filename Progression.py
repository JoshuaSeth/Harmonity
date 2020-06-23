def GetNextChordPosition(current):
    possibles = []
    if current == 1:
        possibles.append(2)
        possibles.append(3)
        possibles.append(4)
        possibles.append(5)
        possibles.append(6)
        #possibles.append(7)
    if current == 2:
        possibles.append(5)
        #possibles.append(7)
    if current == 3:
        possibles.append(4)
        possibles.append(6)
    if current == 4:
        possibles.append(2)
        possibles.append(1)
        possibles.append(5)
        #possibles.append(7)
    if current == 5:
        #possibles.append(7)
        possibles.append(1)
        possibles.append(6)
    if current == 6:
        possibles.append(4)
        possibles.append(2)
    if current == 7:
        possibles.append(1)
        possibles.append(3)
    return possibles