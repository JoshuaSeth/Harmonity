from Musicality import Tonality as t, Chord as c, Scale as s

tone = t.Tone()
tone.CreateFromNumberInTonemap(0)
chord = c.Chord()
chord.CreateChordFromTone(tone, "Sus4")

# for tone in chord.tones:
#     print(tone.name)

scale = s.Scale()
scale.CreateFromToneAndMode(tone, "Major")

for tone in scale.tones:
    print(tone.name)
    chord1 = c.Chord()
    chord1.CreateTriadFromToneAndScale(tone, scale)
    print(chord1.GetName())
    print(chord1.PrintTones())



