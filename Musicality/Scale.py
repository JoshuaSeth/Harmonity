import Musicality.Tonality as t
import Musicality.Modes as m
import Musicality.Util as u

class Scale():
    def __init__(self):
        self.baseTone = None
        self.tones = []
        self.mode = None
        self.modeName = ""
        self.chords = []

    def CreateFromToneAndMode(self, tone, modeName):
        #If needed parse string to tone
        if type(tone) == str:
            toneObj = t.Tone()
            toneObj.CreateFromNumberInTonemap(t.toneMap.index(tone))
            tone= toneObj

        self.baseTone = tone
        self.tones.append(tone)

        self.modeName=modeName
        self.mode = m.Modes[modeName]
        count = 0
        for permutation in self.mode:
            count = count + permutation
            newTone = self.baseTone.GetToneAbove(count)

            if not u.Contains(self.tones, newTone.name):
                self.tones.append(newTone)

        #CREATE CHORDS
        from Musicality import Chord
        for tone in self.tones:
            chord = Chord.Chord()
            chord.CreateTriadFromToneAndScale(tone, self)
            self.chords.append(chord)

    def GetPretty(self):
        return self.baseTone.GetName() + " " + self.modeName + "\n" + "Tones: " + str(u.GetNames(self.tones)) + "\n" + "Chords: " + str(u.GetNames(self.chords))



def GetAllScales():
    scales = []
    for tone in t.toneMap:
        for mode in list(m.Modes.keys()):
            scale = Scale()
            scale.CreateFromToneAndMode(tone, mode)
            scales.append(scale)
    return scales

def GetScalesFittingChords(self, chords):
    scales = GetAllScales()
    possibleScales = []
    for scale in scales:
        append = True
        for chord in chords:
            for tone in chord.tones:
                if not u.Contains(scale.tones, tone.GetName()):
                    append = False

        if append == True:
            possibleScales.append(scale)
    return possibleScales