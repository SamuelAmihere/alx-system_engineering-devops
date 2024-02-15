#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0

    if type(roman_string) == str and roman_string is not None:
        rom_dec = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                'D': 500, 'M': 1000}

        n = len(roman_string) - 1
        temp, i = {}, 1

        while (n >= 0):
            rom, dec = roman_string[n], rom_dec[roman_string[n]]
            if (n + 1) < len(roman_string):
                prev_rom = roman_string[n + 1]
            else:
                prev_rom = roman_string[n]

            try:
                temp[rom].append(dec)
            except KeyError:
                temp[rom] = [dec]

            # compare current roman numeral to previous
            if (rom_dec[rom] < rom_dec[prev_rom]):
                # reduce value
                result -= temp[rom].pop()
            else:
                result += dec

            n -= 1
            i += 1
    return result
