chordConfigurations ={"Major" : [4, 7],
                     "Minor" : [3, 7],
                     "Augmented": [4,8],
                     "Diminished" : [3, 6],
                      "Sus2":[2,7],
                      "Sus4":[5,7]}

def GetNameByConfiguration(configuration):
    key_list = list(chordConfigurations.keys())
    val_list = list(chordConfigurations.values())

    if val_list.__contains__(configuration):
        return key_list[val_list.index(configuration)]
    else:
        print(configuration)
        return "?"