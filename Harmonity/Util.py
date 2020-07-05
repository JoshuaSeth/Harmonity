def Contains(list, name):
    for item in list:
        if item.name == name:
            return True
    return False

def ClipToLength(self, nr, maxLen):
    if nr >= maxLen:
        nr = nr - maxLen
    if nr >= maxLen:
        self.ClipToLength(nr)
    return nr


def GetKeyByValue(dict, value):
    key_list = list(dict.keys())
    val_list = list(dict.values())

    if val_list.__contains__(value):
        return key_list[val_list.index(value)]
    else:
        print("WARNING: " + str(value) + " not found")
        return "?"

def GetNames(list):
    stringList = []
    for item in list:
        try:
            stringList.append(item.GetName())
        except NotImplementedError:
            print("ERROR: Supplied item does not implement GetName Function")
            return None
    return stringList
