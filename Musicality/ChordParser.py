import Musicality.Tonality as t

def StringToNoteAndStyle(input):
    #If Length is 1 it is simply a major chord of one letter
    if len(input) == 1:
        return input, "Major"
    #If Length is 2 it is either minor or with #
    if len(input) == 2:
        if input.__contains__("m") or input.__contains__("M"):
            return input, "Minor"
        else:
            return input, "Major"
    if len(input) == 3:
        return input.__replace__("m", ""), "Minor"

    type = ""
    if input.__contains__("aug") or input.__contains__("Aug"):
        type = "Augmented"
        tone = IterateUntilValidTone(input)
        return tone, type

    if input.__contains__("dim") or input.__contains__("Dim"):
        type = "Diminished"
        tone = IterateUntilValidTone(input)
        return tone, type

    if input.__contains__("sus2") or input.__contains__("Sus2"):
        type = "Sus2"
        tone = IterateUntilValidTone(input)
        return tone, type

    if input.__contains__("sus4") or input.__contains__("Sus4"):
        type = "Sus4"
        tone = IterateUntilValidTone(input)
        return tone, type

    if input.__contains__("Maj") or input.__contains__("maj"):
        type = "Major"
        tone = IterateUntilValidTone(input)
        return tone, type

    if input.__contains__("Min") or input.__contains__("min"):
        type = "Minor"
        tone = IterateUntilValidTone(input)
        return tone, type

    print("WARNING: No chord could be recognized from string")
    return "No tone found", "No chord type found"


def IterateUntilValidTone(input):
    tone = ""
    for char in input:
        if t.toneMap.__contains__(str(char)):
            tone = str(char)
    return tone



