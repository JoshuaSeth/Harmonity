import Tonality as t
import Modes as m
from Consonance import Chord
import Progression as p


def GetNotesForScale(mode, baseNote):
    notesInScale = []
    notesInScale.append(baseNote)
    count = t.NoteNumberByName(baseNote)
    for permutation in mode:
        nextNote = t.GetNote(count + permutation)
        notesInScale.append(nextNote)
        count+=permutation
    return notesInScale

def GetChordsForScale(mode, baseNote):
    chords = []
    notes = GetNotesForScale(mode, baseNote)
    print(notes)
    index = 0
    for note in notes:
        chord = Chord()
        chord.MakeTriad(notes, note)
        chords.append(chord)
    print(chords)
    return chords

def GetScaleDegrees(mode, baseNote):
    chords = GetChordsForScale(mode, baseNote)
    scaleDegrees = {}
    scaleDegrees["Tonic"]= chords[0]
    scaleDegrees["Supertonic"]= chords[1]
    scaleDegrees["Mediant"]= chords[2]
    scaleDegrees["Subdominant"]= chords[3]
    scaleDegrees["Dominant"]= chords[4]
    scaleDegrees["Submediant"]= chords[5]
    stepsToStartNote = t.NoteNumberByName(chords[6].notes[0])-t.NoteNumberByName(chords[0].notes[0])
    print(stepsToStartNote)
    if(stepsToStartNote==11 or stepsToStartNote==1):
        scaleDegrees["Leadingtone"]= chords[6]
    else:
        scaleDegrees["Subtonic"]= chords[6]
    return scaleDegrees

def GetScaleDegreesNames(mode, baseNote):
    chords = GetChordsForScale(mode, baseNote)
    scaleDegrees = {}
    scaleDegrees["Tonic"]= chords[0].GetName()
    scaleDegrees["Supertonic"]= chords[1].GetName()
    scaleDegrees["Mediant"]= chords[2].GetName()
    scaleDegrees["Subdominant"]= chords[3].GetName()
    scaleDegrees["Dominant"]= chords[4].GetName()
    scaleDegrees["Submediant"]= chords[5].GetName()
    stepsToStartNote = t.NoteNumberByName(chords[6].notes[0])-t.NoteNumberByName(chords[0].notes[0])
    print(stepsToStartNote)
    if(stepsToStartNote==11 or stepsToStartNote==1):
        scaleDegrees["Leadingtone"]= chords[6].GetName()
    else:
        scaleDegrees["Subtonic"]= chords[6].GetName()
    return scaleDegrees

def GetScalesWithChords(chordCollection):
    #     for each mode starting with each note check if they contain all notes
    # Get notes from chords
    notesInChords = ExtractNotesFromChords(chordCollection)

    # Collect all possible scales by combine modes with basetones
    allScales = GetAllPossibleScales()

    # Strip scales for tones not notes
    allScales = ScalesNotesToScalesTones(allScales)

    # Check which scales fit all the notes
    fittingScaleObjects = []
    for scale in allScales:
        fitsNotes = True
        for note in notesInChords:
            if not scale.notes.__contains__(note):
                fitsNotes=False
        if fitsNotes:
            fittingScaleObjects.append(scale)
    return fittingScaleObjects


def GetNextChordInProgression(chordProgression):
    scales = GetScalesWithChords(chordProgression)
    possibleCombis = []
    for scale in scales:
        lastChordIndex = len(chordProgression)-1
        lastChordName = chordProgression[lastChordIndex].GetName()
        strippedChordName = t.StripChord(lastChordName)
        lastChordIndexInScale = scale.notes.index(strippedChordName) + 1
        indicesOfPossibleFollowing = p.GetNextChordPosition(lastChordIndexInScale)
        for nr in indicesOfPossibleFollowing:
            chord = GetChordsForScale(scale.mode, scale.baseNote)[nr]
            chordScaleCombi = ChordInScale()
            chordScaleCombi.chord = chord
            chordScaleCombi.scale = scale
            chordScaleCombi.chordIndex = nr

            possibleCombis.append(chordScaleCombi)
    return possibleCombis

#     What position does the last chord have in the scales?


def GetAllPossibleScales():
    allScales = []
    for startNote in t.toneMap:
        for modeName, mode in m.Modes.items():
            newScale = Scale()
            newScale.name = str(startNote) + " " + str(modeName)
            newScale.notes = GetNotesForScale(mode, startNote + "2")
            newScale.mode = modeName
            newScale.baseNote = startNote
            allScales.append(newScale)
    return allScales

def ExtractNotesFromChords(chordCollection):
    notesInChords = []
    for chord in chordCollection:
        for note in chord.notes:
            notesInChords.append(t.OnlyNoteTone(note))
    return notesInChords

def ScalesNotesToScalesTones(scales):
    for scale in scales:
        newNotes = []
        for note in scale.notes:
            newNotes.append(t.OnlyNoteTone(note))
        scale.notes = newNotes
    return scales


class Scale:
    name = ""
    notes = []
    mode = m.Modes["Major"]
    baseNote = ""

    def GetChordPositionInScale(self, chord):
        print(chord.baseNote)
        # chordnoteName = t.StripChord(chord.baseNote+"2")
        # return self.notes.index(chordnoteName)

class ChordInScale:
    chord = None
    scale = None
    previousChordIndex = 0
    chordIndex = 0

    def AsString(self):
        return self.chord.GetName() + " with notes: " + str(chord.notes) + " in position: " + str(self.chordIndex) + " in scale: " + self.scale.name

chords = []
chord = Chord()
chord.MakeChord("F2", True)
chord1 = Chord()
chord1.MakeChord("C2", True)
chord2 = Chord()
chord2.MakeChord("D2", False)

chords.append(chord)
chords.append(chord1)
chords.append(chord2)

possibleNextChords = GetNextChordInProgression(chords)
for c in possibleNextChords:
    print(c.AsString())