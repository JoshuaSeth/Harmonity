toneMap = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
keyboardStart = -2

class Tone:
    nrInToneMap = -1
    string = toneMap[nrInToneMap]

    def CreateFromString(self, string):
        self.nrInToneMap = toneMap.index(string)
        self.string = string

    def CreateFromNumberInTonemap(self, nr):
        self.nrInToneMap = nr
        self.string = toneMap[nr]



class Note:
    tone = None
    height = keyboardStart

    def GetAsNumber(self):
        diffBottomHere = self.height - keyboardStart
        octavesCount = diffBottomHere * toneMap.__len__()
        inToneMapNR = self.tone.nrInToneMap
        return octavesCount+inToneMapNR


