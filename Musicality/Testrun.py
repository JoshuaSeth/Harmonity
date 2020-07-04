from Musicality import Tonality as t, Chord as c

tone = t.Tone()
tone.CreateFromNumberInTonemap(0)
chord = c.Chord
chord.CreateChordFromTone(chord, tone, "Major")

for tone in chord.tones:
    print(tone.name)