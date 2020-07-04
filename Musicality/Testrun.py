from Musicality import Tonality as t, Chord as c, Scale as s

tone = t.Tone()
tone.CreateFromNumberInTonemap(0)
chord = c.Chord
chord.CreateChordFromTone(chord, tone, "Sus4")

# for tone in chord.tones:
#     print(tone.name)

scale = s.Scale()
scale.CreateFromToneAndMode(tone, "Lydian")

for tone in scale.tones:
    print(tone.name)