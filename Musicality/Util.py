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