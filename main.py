import random

TIME_SIGNATURE_NUM = 4
TIME_SIGNATURE_DEN = 4
NUM_MEASURES = 4
NUM_SONG_NOTES = NUM_MEASURES * TIME_SIGNATURE_NUM
NUM_NOTES = 12
# Cn = 0, Cs = 1, Dn = 2 ... Bb = 10, Bn = 11
NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

BEAT_WIDTH = 5

# Return a list of random chords of specified length
def return_rand_chords(num_chords: int):
    chords_list = []
    for ii in range(num_chords):
        # Select a random chord from the list of possible notes
        chords_list.append(NOTES[random.randrange(0, NUM_NOTES)])

        # 1/2 chance that the chord is a minor chord
        if random.randrange(0, 2):
            chords_list[-1] += 'm'

        # 1/3 chance that the chord is a 7th
        if not random.randrange(0, 3):
            chords_list[-1] += '7'

    return chords_list

# Make a copy of the input string that is the specified length
def format_string(in_string: str, form_length: int):
    out_string = str()
    for str_idx in range(form_length):
        # If the input string is more than the specified length, clip characters from end
        if str_idx < len(in_string):
            out_string += in_string[str_idx]
        # If the input string is less than the specified length, append spaces
        else:
            out_string += ' '

    return out_string

# Take a list of chords and beats and make it into a prettier string
def list_to_staff(song_bank_list: list):
    # Append a treble clef 
    staff_string = '&['
    for bank_c in range(len(song_bank_list)):
        # Make measure break lines at the end of each measure
        if not (bank_c % TIME_SIGNATURE_NUM) and bank_c:
            staff_string += ' | '
    
        staff_string += song_bank_list[bank_c]

    staff_string += ']'

    return staff_string

# Take the random list of chords and make it into a song list with beats
def build_song_from_chords(chord_list: list):
    song_bank = []
    for note_c in range(NUM_SONG_NOTES):
        song_bank.append(' -   ') # Use a dash in place of a rest


    beat_c = 0 # Counter to keep track of which beat we're on
    for chord_c in range(len(chord_list)):
        chords_remaining = len(chord_list) - chord_c
        beats_remaining = NUM_SONG_NOTES - beat_c # Calc how many beats are left in the song
        beats_remaining_for_chord = beats_remaining - chords_remaining # Calc number of beats but leave room for remaining chords
        
        chord_beat = random.randrange(beat_c, beat_c + beats_remaining_for_chord)

        if not chord_c:
            chord_beat = random.randint(1, TIME_SIGNATURE_NUM) # Make sure there's a chord in the first measure
        song_bank[chord_beat] = format_string(chord_list[chord_c], 5)
        beat_c = chord_beat + 1
    return song_bank


def main():
    print(" ")
    print("Activated...")
    random.seed()

    num_chords = random.randint(1, NUM_MEASURES*(round(TIME_SIGNATURE_NUM / 2)))
    rand_chords = return_rand_chords(num_chords)

    song = build_song_from_chords(rand_chords)

    print("SONG BANK:")
    print(list_to_staff(song))

    print(" ")


if __name__ == "__main__":
    main()


