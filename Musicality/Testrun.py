from Musicality import Tonality as t, Chord as c, Scale as s

tone = t.Tone()
tone.CreateFromNumberInTonemap(6)
chord = c.Chord()
chord.CreateChordFromTone(tone, "Diminished")

print(chord.GetPretty())

tone = t.Tone()
tone.CreateFromNumberInTonemap(0)
chord1 = c.Chord()
chord1.CreateChordFromTone(tone, "Major")

print(chord1.GetPretty())

scales = s.GetScalesFittingChords(s,[chord, chord1])
for scale in scales:
    print(scale.GetPretty())

# for tone in chord.tones:
#     print(tone.name)

#Scale test
# scale = s.Scale()
# scale.CreateFromToneAndMode(tone, "Lydian")
# print(scale.GetPretty())




