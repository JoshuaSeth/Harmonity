from Musicality import ChordParser as cp, Tonality as t, Chord as c, ChordConfigurations as cc

def MakeChordFromString(string):
    toneName, chordStyleName = cp.StringToNoteAndStyle(string)
    chord = c.Chord()
    tone = t.Tone()
    tone.CreateFromString(toneName)
    chord.CreateChordFromTone(tone, cc.chordConfigurations[chordStyleName])
    return chord

def MakeChord(String=None, Tone=None, ConfigurationByName= None, Configuration=None):
    if String is not None and Tone is None:
        return MakeChordFromString(String)
    if Tone is not None and Configuration is not None:
        chord = c.Chord
        chord.CreateChordFromTone(Tone, Configuration)
        return chord
    if Tone is not None and ConfigurationByName is not None:
        chord = c.Chord
        chord.CreateChordFromTone(Tone, cc.chordConfigurations[ConfigurationByName])
        return chord
    if String is not None and Configuration is not None and len(String) < 3:
        tone = t.Tone()
        tone.CreateFromString(String)
        chord = c.Chord
        chord.CreateChordFromTone(tone, Configuration)
    if String is not None and ConfigurationByName is not None and len(String) < 3:
        tone = t.Tone()
        tone.CreateFromString(String)
        chord = c.Chord
        chord.CreateChordFromTone(tone, cc.chordConfigurations[ConfigurationByName])


    print("Warning: Could not create chord. Make sure to either supply a string for a chord (e.g. 'A Minor') or to supply a tone with a chord configuration or configuratio name (e.g. Tone and 'Minor')")
    return None
