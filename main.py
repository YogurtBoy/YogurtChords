import random

TIME_SIGNATURE_NUM = 4
TIME_SIGNATURE_DEN = 4
NUM_MEASURES = 2
NUM_SONG_NOTES = NUM_MEASURES * TIME_SIGNATURE_NUM
NUM_NOTES = 12
# Cn = 0, Cs = 1, Dn = 2 ... Bb = 10, Bn = 11
NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

BEAT_WIDTH = 5


def return_rand_chords(num_chords: int):
    chords_list = []
    for ii in range(num_chords):
        chords_list.append(NOTES[random.randrange(0, NUM_NOTES)])

    return chords_list

def format_string(in_string: str, form_length: int):
    out_string = str()
    for str_idx in range(form_length):
        if str_idx < len(in_string):
            out_string += in_string[str_idx]
        else:
            out_string += ' '
    return out_string

def list_to_staff(song_bank_list: list):
    staff_string = '&['
    for bank_c in range(len(song_bank_list)):
        if not (bank_c % 4) and bank_c:
            staff_string += ' | '    
        staff_string += song_bank_list[bank_c]
    staff_string += ']'
    return staff_string
    

def main():
    print("Activated...")
    random.seed()

    song_bank = []
    for note_c in range(NUM_SONG_NOTES):
        song_bank.append(' -   ')
    beat = random.randint(1, TIME_SIGNATURE_NUM)

    num_chords = 4
    rand_chords = return_rand_chords(num_chords)
    print(rand_chords)

    # song_string = str()
    note_c = 0
    for chord_c in range(num_chords):
        chords_remaining = len(rand_chords) - chord_c
        beats_remaining = NUM_SONG_NOTES - note_c
        beats_remaining_for_chord = beats_remaining - chords_remaining
        chord_beat = random.randrange(note_c, note_c + beats_remaining_for_chord)
        song_bank[chord_beat] = format_string(rand_chords[chord_c], 5)
        note_c = chord_beat + 1

    print("SONG BANK:")
    print(list_to_staff(song_bank))


if __name__ == "__main__":
    main()


