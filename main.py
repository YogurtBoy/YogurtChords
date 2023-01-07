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
    # Create the song bank and populate with empty beats
    song_bank = []
    for note_c in range(NUM_SONG_NOTES):
        song_bank.append(' -   ') # Use a dash in place of a rest

    # Generate a list of random beats for the chords to fall on
    beat_sched = []
    for rand_c in range(len(chord_list)):
        rand_beat = random.randint(1, NUM_SONG_NOTES)
        while rand_beat in beat_sched:
            rand_beat = random.randint(1, NUM_SONG_NOTES)
        beat_sched.append(rand_beat)
    beat_sched.sort()
    # Make sure there's a chord in the first measure
    if not (beat_sched[0] < TIME_SIGNATURE_NUM):
            beat_sched[0] = random.randint(1, TIME_SIGNATURE_NUM)

    # Replace rests in the song bank with chords from the random chord list
    for chord_c in range(len(chord_list)):    
        song_bank[beat_sched[chord_c] - 1] = format_string(chord_list[chord_c], 5)

    return song_bank


def main():
    print(" ")
    print("Activated...")
    random.seed()

    # Generate the primary list of random chords
    num_chords = random.randint(1, NUM_MEASURES*(round(TIME_SIGNATURE_NUM / 2)))
    rand_chords = return_rand_chords(num_chords)

    song = build_song_from_chords(rand_chords)

    print("SONG BANK:")
    print(list_to_staff(song))

    print(" ")


if __name__ == "__main__":
    main()


