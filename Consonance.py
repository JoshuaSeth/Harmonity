import Tonality as t

class Chord:
    def __init__(self):
        self.notes = []
        self.baseNote = ""

    def MakeChord(self, baseNote, major):
        # if (self.notes.__len__() > 0):
        #     print("WARNING: this chord already has notes, it might turn into two overlapping chords")
        baseNoteNr = t.NoteNumberByName(baseNote)
        self.baseNote = baseNote
        self.notes.append(baseNote)
        if(major):
            self.notes.append(t.GetNote(int(baseNoteNr+4)))
        if(not major):
            self.notes.append(t.GetNote(int(baseNoteNr+3)))
        self.notes.append(t.GetNote(baseNoteNr + 7))
        #print(self.notes)

    def MakeTriad(self, scale, baseNote):
        # if(self.notes.__len__()>0):
        #     print("WARNING: this chord already has notes, it might turn into two overlapping chords")
        self.baseNote = baseNote
        self.notes.append(baseNote)
        nextNoteNr = self.Iterate(scale.notes.index(baseNote), 2, scale.notes.__len__())
        self.notes.append(scale.notes[nextNoteNr])
        lastNoteNr = self.Iterate(nextNoteNr, 2, scale.notes.__len__())
        self.notes.append(scale.notes[lastNoteNr])

    def GetName(self):
        #print("base:" +self.baseNote)
        name, temp= t.StrippedNoteName(self.baseNote)
        minorCountUp = t.NoteNumberByName(self.baseNote)+3
        majorCountUp = t.NoteNumberByName(self.baseNote)+4
        # print(minorCountUp)
        minorNoteName = t.GetNote(minorCountUp)
        majorNoteName = t.GetNote(majorCountUp)
        # print(minorNoteName)
        if(self.notes.__contains__(minorNoteName)):
            name+='m'
        if(not self.notes.__contains__(minorNoteName) and not self.notes.__contains__(majorNoteName)):
            name+="dim"
        return name

    def GetNotes(self):
        noteStrings = []
        for note in self.notes:
            name, temp = t.StrippedNoteName(note)
            noteStrings.append(name)
        return noteStrings


    def NotesAsNumbers(self):
        notesAsNumbers = []
        for note in self.notes:
            notesAsNumbers.append(t.NoteNumberByName(note))
        return notesAsNumbers

    # def GetHarmonicBaseNote(self, asNote):
    #     numbers = self.NotesAsNumbers()
    #     index = 0
    #     for number in numbers:
    #         if (numbers.__contains__(number+4) or numbers.__contains__(number+3)) and numbers.__contains__(number+7):
    #             if not asNote:
    #                 return number
    #             if asNote:
    #                 return t.GetNote(number)

    def Iterate(self, current, addition, maximum):
        count = current+addition
        if(count>=maximum):
            count = self.WithinRange(count, maximum)
        return count

    def WithinRange(self, count, maximum):
        if (count >=maximum):
            count = count - maximum
        if(count>=maximum):
            self.WithinRange(count, maximum)
        return count

    def GetNext(self, notes, index):
        index+=1
        if(index == notes.__len__()):
            index=0
        return notes[index]
