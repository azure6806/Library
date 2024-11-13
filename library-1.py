
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"


def is_alpha(word):
    for character in word:
        if(character not in ASCII_LOWERCASE and character not in ASCII_UPPERCASE):
            return True
        else:
            return False


def is_digit(s):
    def is_digit(s):
        for character in s:
            if(character not in DECIMAL_DIGITS):
                return False
        return True



def to_lower(s):
    result = ""
    for character in s:
        if character in ASCII_UPPERCASE:
            result += ASCII_LOWERCASE[ASCII_UPPERCASE.index(character)]
        else:
            result += character
    return result

def to_upper(s):
    result = ""
    for character in s:
        if character in ASCII_LOWERCASE:
            result += ASCII_UPPERCASE[ASCII_LOWERCASE.index(character)]
        else:
            result += character
    return result


def find_chr(s, char):
    for i, character in enumerate(s):
        if character == char:
            return i
    return -1

def find_str(s, substr):
    len_sub = len(substr)
    for i in range(len(s) - len_sub + 1):
        if s[i:i + len_sub] == substr:
            return i
    return -1


def replace_chr(s, old, new):
    result = ""
    for character in s:
        if character == old:
            result += new
        else:
            result += character
    return result


def replace_str(s, old, new):
    result = ""
    i = 0
    len_old = len(old)
    while i < len(s):
        if s[i:i + len_old] == old:
            result += new
            i += len_old
        else:
            result += s[i]
            i += 1
    return result



