
def get_fill_words():
    fill_words = []
    fill_words += ['an', 'auf', 'ab', 'also', 'aber', 'auch', 'als', 'aus', 'am']
    fill_words += ['bei', 'beim', 'bin', 'bist']
    fill_words += ['denn', 'den', 'der', 'die', 'das', 'des', 'dass', 'dem', 'dann', 'da', 'diese', 'diesem', 'dafür', 'dieses', 'diesen', 'doch', 'damit', 'drei']
    fill_words += ['ein', 'eine', 'einer', 'es', 'er', 'etwas', 'eins']
    fill_words += ['für', 'fünf']
    fill_words += ['hat']
    fill_words += ['in', 'im', 'ist', 'ihren']
    fill_words += ['ja']
    fill_words += ['nur']
    fill_words += ['ob', 'oder']
    fill_words += ['sich', 'sind', 'so']
    fill_words += ['und', 'um']
    fill_words += ['vor', 'vier']
    fill_words += ['wer', 'wie', 'was', 'wo', 'wenn']
    fill_words += ['zwar', 'zu', 'zum', 'zwei', 'zur']
    fill_words += ['']
    return set(fill_words)


def sanitize_speech(string_list):
    fill_words = get_fill_words()
    string_list = set(string_list)
    return list(string_list - fill_words)


def get_sanitized_wordlist(string):
    wordlist = string.split(' ')
    wordlist = [w.lower() for w in wordlist if not w.isdigit()]
    sanitized_wordlist = sanitize_speech(wordlist)
    return sanitized_wordlist
