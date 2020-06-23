


toneMap = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
keyboardStart = -2

def GetNote(numberFromCminus2):
    inChromaticScale = numberFromCminus2 % toneMap.__len__()
    totalNotes = numberFromCminus2-inChromaticScale
    height = int(totalNotes/toneMap.__len__() + keyboardStart)
    noteName = toneMap[inChromaticScale]
    noteName = noteName+height.__str__()
    return noteName

def NoteNumberByName(noteName):
    noteNameWithoutHeight, splitNote = StrippedNoteName(noteName)
    if splitNote.__len__()==1:
        print("WARNING ASKING NOTE NUMBER FOR TONE, NOT NOTE DEFAULTING TO SECOND OCTAVE")
        splitNote.append("2")
    height = int(splitNote[splitNote.__len__()-1])
    positiveHeight = height-keyboardStart
    totalNotes = positiveHeight*toneMap.__len__()
    inChromaticScaleNr = toneMap.index(noteNameWithoutHeight)
    return int(totalNotes+inChromaticScaleNr)


def StrippedNoteName(noteName):
    #print("notename:" + noteName)
    splitNote = SplitNote(noteName)
    # print(splitNote)
    #print("split:"+str(splitNote))
    noteNameWithoutHeight = splitNote[0]
    if(splitNote.__len__()>1):
        if (not splitNote[1].isdigit() and not splitNote[1].__contains__("-")):
            noteNameWithoutHeight += splitNote[1]
    return noteNameWithoutHeight, splitNote

def OnlyNoteTone(noteName):
    splitNote = SplitNote(noteName)
    # print(splitNote)
    noteNameWithoutHeight = splitNote[0]
    if(splitNote.__len__()>1):
        if (not splitNote[1].isdigit() and not splitNote[1].__contains__("-")):
            noteNameWithoutHeight += splitNote[1]
    return noteNameWithoutHeight

def StripChord(chordName):
    splitChord = SplitNote(chordName)
    # print(splitNote)
    strippedChord = splitChord[0]
    if(splitChord.__len__()>1):
        if (not splitChord[1].isdigit() and not splitChord[1].__contains__("-") and not splitChord[1].__contains__("m")):
            strippedChord += splitChord[1]
    if(splitChord.__len__()>2):
        if (not splitChord[2].isdigit() and not splitChord[2].__contains__("-")):
            strippedChord += splitChord[2]
    return strippedChord


def SplitNote(word):
    coll = [char for char in word if char is not "-"]
    if word.__contains__("-") and word.__contains__("#"):
        coll[2] = str(int(coll[2])*-1)
    if word.__contains__("-") and not word.__contains__("#"):
        coll[1] = str(int(coll[1]) * -1)
    return coll

