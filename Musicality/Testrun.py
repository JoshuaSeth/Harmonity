from Musicality import Tonality as t, Chord as c, Scale as s, Harmonity as h


chord = h.MakeChord("D min")
print(chord.GetPretty())
chord.GetFittingScales().PrintPretty()

# for tone in chord.tones:
#     print(tone.name)

#Scale test
# scale = s.Scale()
# scale.CreateFromToneAndMode(tone, "Lydian")
# print(scale.GetPretty())




