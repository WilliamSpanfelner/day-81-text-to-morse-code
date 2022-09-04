# first create a dictionary of the Morse Code
#

# [Morse code](https://en.wikipedia.org/wiki/Morse_code)
# [Morse code](https://www.theproblemsite.com/reference/mathematics/codes/morse-code)

# First Morse code message: "What God Hath Wrought"

# The length of one dot is one unit;
# A dash is three units;
# The space between parts of the same character is one unit;
# The gap between characters is three units long;
# The gap between words is seven units long.
import pysine

MORSE_CHART = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '0': '_____',
    '.': '._._._',
    ',': '__..__',
    '?': '..__..',
    "'": '.____.',
    "!": '_._.__',
    "/": '_.._.',
    "(": '_.__.',
    ")": '_.__._',
    "&": '._...',
    ":": '___...',
    ";": '_._._.',
    "=": '_..._',
    "+": '._._.',
    "-": '_...._',
    "_": '..__._',
    '"': '._.._.',
    "$": '..._.._',
    "@": '.__._.',
    "Error": '........',
}

MORSE_CODE_BOOL = {
    'a': [True, False],
    'b': [False, True, True, True],
    'c': [False, True, False, True],
    'd': [False, True, True],
    'e': [True],
    'f': [True, True, False, True],
    'g': [False, False, True],
    'h': [True, True, True, True],
    'i': [True, True],
    'j': [True, False, False, False],
    'k': [False, True, False],
    'l': [True, False, True, True],
    'm': [False, False],
    'n': [False, True],
    'o': [False, False, False],
    'p': [True, False, False, True],
    'q': [False, False, True, False],
    'r': [True, False, True],
    's': [True, True, True],
    't': [False],
    'u': [True, True, False],
    'v': [True, True, True, False],
    'w': [True, False, False],
    'x': [False, True, True, False],
    'y': [False, True, False, False],
    'z': [False, False, True, True],
    '1': [True, False, False, False, False],
    '2': [True, True, False, False, False],
    '3': [True, True, True, False, False],
    '4': [True, True, True, True, False],
    '5': [True, True, True, True, True],
    '6': [False, True, True, True, True],
    '7': [False, False, True, True, True],
    '8': [False, False, False, True, True],
    '9': [False, False, False, False, True],
    '0': [False, False, False, False, True],
    '.': [True, False, True, False, True, False],
    ',': [False, False, True, True, False, False],
    '?': [True, True, False, False, True, True],
    "'": [True, False, False, False, False, True],
    "!": [False, True, False, True, False, False],
    "/": [False, True, True, False, True],
    "(": [False, True, False, False, True],
    ")": [False, True, False, False, True, False],
    "&": [True, False, True, True, True],
    ":": [False, False, False, True, True, True],
    ";": [False, True, False, True, False, True],
    "=": [False, True, True, True, False],
    "+": [True, False, True, False, True],
    "-": [False, True, True, True, False],
    '"': [True, False, True, True, False, True],
    '$': [True, True, True, False, True, True, False],
    '@': [True, False, False, True, False, True],
    'Error': [True, True, True, True, True, True, True, True],
}

WORD_GAP = "       "
CHAR_GAP = "   "

morse_formatted_text = ""
morse_code = ""
morse_code_with_timing = []


def gen_tones_for(code):
    """
    Reads the morse code list and sounds a tone based on string values
    :param code: A list of morse code pulses
    """

    freq = 550.0
    silent_freq = 0
    dur = 0.1
    for pulse in code:
        if pulse == ".":
            pysine.sine(frequency=freq, duration=dur)
        elif pulse == "_":
            pysine.sine(frequency=freq, duration=dur * 3)
        elif pulse == "1":
            pysine.sine(frequency=silent_freq, duration=dur)
        elif pulse == "3":
            pysine.sine(frequency=silent_freq, duration=dur * 3)
        else:
            pysine.sine(frequency=silent_freq, duration=dur * 7)


def morse_encode(character):
    """
    :rtype: tuple
    :param character: a string representing a letter in the word to be encoded
    :return: a tuple including the Morse code encoded character, the length of the code, and a list
    of the components of a message with timing.
    """
    encoded_character = ""
    encoded_character_with_timing = []
    for pulse_index, bool_pulse in enumerate(MORSE_CODE_BOOL[character]):
        if bool_pulse:
            encoded_character += "."
            encoded_character_with_timing += ["."]
        else:
            encoded_character += "_"
            encoded_character_with_timing += ["_"]
        if pulse_index < len(MORSE_CODE_BOOL[character]) - 1:
            encoded_character_with_timing += ["1"]

    return encoded_character, len(MORSE_CODE_BOOL[character]), encoded_character_with_timing


char_list_to_encode = list(input("Enter the text you wish to convert: \n").lower())
enumerated_text = enumerate(char_list_to_encode)

for index, char in enumerated_text:

    if char == " ":
        morse_formatted_text += WORD_GAP
        morse_code += WORD_GAP
    else:
        if char not in MORSE_CODE_BOOL.keys():
            print("Only alphanumeric characters can be converted to Morse Code (e.g. letters from A - Z or a number "
                  "from 0 - 9)")
        else:
            spaces = ""

            # Assign components of tuple returned from morse_encode
            encoded_char = morse_encode(char)[0]
            code_length = morse_encode(char)[1]

            # To include timing the next character to be encoded in the sequence
            # must be known
            for pulse in morse_encode(char)[2]:
                morse_code_with_timing += pulse

            if index < len(char_list_to_encode) - 1:
                if char_list_to_encode[index + 1] == " ":
                    morse_code_with_timing += "7"
                else:
                    morse_code_with_timing += "3"

            for i in range(code_length - 1):
                spaces += " "
            morse_formatted_text += char + spaces + CHAR_GAP
            morse_code += encoded_char + CHAR_GAP

print(morse_formatted_text)
print(morse_code)
print(morse_code_with_timing)
gen_tones_for(code=morse_code_with_timing)
