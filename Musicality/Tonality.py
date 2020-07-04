toneMap = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
keyboardStart = -2

class Tone:
    nrInToneMap = -1
    name = ""

    def CreateFromString(self, string):
        self.nrInToneMap = toneMap.index(string)
        self.name = string

    def CreateFromNumberInTonemap(self, nr):
        self.nrInToneMap = nr
        self.name = toneMap[nr]

    def GetToneAbove(self, steps):
        tone = Tone()
        nr = self.nrInToneMap+steps
        if nr > toneMap.__len__():
            nr = nr-toneMap.__len__() -1
        tone.CreateFromNumberInTonemap(nr)
        return tone




class Note:
    tone = None
    height = keyboardStart

    def GetAsNumber(self):
        diffBottomHere = self.height - keyboardStart
        octavesCount = diffBottomHere * toneMap.__len__()
        inToneMapNR = self.tone.nrInToneMap
        return octavesCount+inToneMapNR

    def GetAsName(self):
        return str(self.tone) + str(self.height)

    def Create(self, tone, number):
        self.tone = tone
        self.height = number



