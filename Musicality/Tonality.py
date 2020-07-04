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
        nr = self.ClipToLength(nr)
        tone.CreateFromNumberInTonemap(nr)
        return tone

    def ClipToLength(self, nr):
        if nr >= toneMap.__len__():
            nr = nr - toneMap.__len__() - 1
        if nr >= toneMap.__len__():
            self.ClipToLength(nr)
        return nr


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



