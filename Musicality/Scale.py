import Musicality.Tonality as t
import Musicality.Modes as m
import Musicality.Util as u

class Scale():
    baseTone = None
    tones = []
    mode = None
    modeName = ""

    def CreateFromToneAndMode(self, tone, modeName):
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
