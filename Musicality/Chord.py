import Musicality.ChordConfigurations as c
import Musicality.Util as u

class Chord:
    def __init__(self):
        self.notes = []
        self.tones = []
        self.baseNote = None
        self.baseTone = None

    def CreateChordFromTone(self, tone, configuration):
        self.baseTone=tone
        self.tones.append(tone)

        chordConfiguration = c.chordConfigurations[configuration]
        for steps in chordConfiguration:
            self.tones.append(tone.GetToneAbove(steps))

    def CreateTriadFromToneAndScale(self, tone, scale):
        self.baseTone = tone
        self.tones.append(tone)

        indexOfSecond = u.ClipToLength(u, scale.tones.index(self.baseTone) + 2, scale.tones.__len__())
        self.tones.append(scale.tones[indexOfSecond])

        indexOfThird = u.ClipToLength(u, scale.tones.index(self.baseTone) + 4, scale.tones.__len__())
        self.tones.append(scale.tones[indexOfThird])



    def PrintTones(self):
        printTones =[]
        for tone in self.tones:
            printTones.append(tone.name)
        return printTones
