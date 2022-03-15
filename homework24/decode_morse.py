morse_code_dict = {'.-': 'A', '-...': 'B',
                   '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K',
                   '.-..': 'L', '--': 'M', '-.': 'N',
                   '---': 'O', '.--.': 'P', '--.-': 'Q',
                   '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W',
                   '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                   '.-.-.-': '.', '-.-.--': '!', ' ': '',
                   '...---...': 'SOS'
                   }


def decode_morse(morse_code):
    out = []
    spases = []
    for letter in morse_code.strip().split(' '):
        if letter in morse_code_dict:
            out.append(morse_code_dict[letter])
        elif letter == '':
            spases.append(letter)
            out.append(' '.join(spases))
            if len(spases) >= 2:
                spases = []
    return ''.join(out)


print(decode_morse('    .... . .-.. .-.. ---   .- ... ... '))


def decode_morse_2(morse_code):
    out = []
    for word in morse_code.strip().split('   '):
        tmp = []
        for code in word.split(' '):
            tmp.append(morse_code_dict[code])
        out.append(''.join(tmp))
    return ' '.join(out)


print(decode_morse_2('    .... . .-.. .-.. ---   .- ... ... '))


def decode_morse_3(morse_code):
    out = []
    for word in morse_code.strip().split('   '):
        out.append(''.join(morse_code_dict.get(code, '') for code in word.split(' ')))
    return ' '.join(out)


print(decode_morse_3('    .... . .-.. .-.. ---   .- ... ... '))


def decode_morse_4(morse_code):
    return ' '.join([''.join([morse_code_dict[code] for code in word.split(' ')]) for word in morse_code.strip().split('   ')])


print(decode_morse_4('    .... . .-.. .-.. ---   .- ... ... '))