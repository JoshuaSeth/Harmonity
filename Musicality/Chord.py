import Musicality.ChordConfigurations as c
import Musicality.Util as u
import Musicality.Tonality as t
import Musicality.Scale as s

class Chord:
    def __init__(self):
        self.notes = []
        self.tones = []
        self.baseNote = None
        self.baseTone = None
        self.configuration = None

    def CreateChordFromTone(self, tone, configuration):
        self.baseTone=tone
        self.tones.append(tone)

        self.configuration = c.chordConfigurations[configuration]
        for steps in self.configuration:
            self.tones.append(tone.GetToneAbove(steps))

    def CreateTriadFromToneAndScale(self, tone, scale):
        self.baseTone = tone
        self.tones.append(tone)

        indexOfSecond = u.ClipToLength(u, scale.tones.index(self.baseTone) + 2, scale.tones.__len__())
        self.tones.append(scale.tones[indexOfSecond])

        indexOfThird = u.ClipToLength(u, scale.tones.index(self.baseTone) + 4, scale.tones.__len__())
        self.tones.append(scale.tones[indexOfThird])

        chordConfig1 = t.toneMap.index(self.tones[1].name) - t.toneMap.index(self.tones[0].name)
        if chordConfig1 < 0:
            chordConfig1 = t.toneMap.__len__()+chordConfig1

        chordConfig2 = t.toneMap.index(self.tones[2].name) - t.toneMap.index(self.tones[0].name)
        if chordConfig2 < 0:
            chordConfig2 = t.toneMap.__len__()+chordConfig2
        self.configuration = [chordConfig1, chordConfig2]

    def GetName(self):
        return self.baseTone.name + " " + u.GetKeyByValue(c.chordConfigurations, self.configuration)

    def GetPretty(self):
        return self.GetName() + "\n Configuration: " + str(self.configuration) + "\n Tones: " + str(u.GetNames(self.tones))

    def GetFittingScales(self):
        return s.GetScalesFittingChords(s, [self])

