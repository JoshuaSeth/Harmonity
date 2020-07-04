import Musicality.ChordConfigurations as c

class Chord:
    notes = []
    tones = []
    baseNote = None
    baseTone = None

    def CreateChordFromTone(self, tone, configuration):
        self.baseTone=tone
        self.tones.append(tone)

        chordConfiguration = c.chordConfigurations[configuration]
        for steps in chordConfiguration:
            self.tones.append(tone.GetToneAbove(steps))
