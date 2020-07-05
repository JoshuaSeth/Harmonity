import Musicality.Util as u

toneMap = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
keyboardStart = -2

class Tone:
    def __init__(self):
        self.nrInToneMap = -1
        self.name = ""

    def CreateFromString(self, string):
        if not toneMap.__contains__(string):
            print("ERROR: the current tonemap does not contain tone: " + string)
            return
        self.nrInToneMap = toneMap.index(string)
        self.name = string

    def CreateFromNumberInTonemap(self, nr):
        self.nrInToneMap = nr
        self.name = toneMap[nr]

    def GetToneAbove(self, steps):
        tone = Tone()
        nr = self.nrInToneMap+steps
        nr = u.ClipToLength(u, nr, toneMap.__len__())
        tone.CreateFromNumberInTonemap(nr)
        return tone

    def GetName(self):
        return self.name




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



