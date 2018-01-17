import sys

from pymongo import MongoClient

from read_files import get_speeches
from utils import get_sanitized_wordlist


def extract_target_speeches():
    args = sys.argv[1:]
    for arg in args:
        if arg.index('--speeches') == 0:
            target_speeches = arg.split('=')[1]
            return target_speeches


def count_words_in_speech(year, speech_string):
    sanitized_wordlist = get_sanitized_wordlist(speech_string)

    for word in sanitized_wordlist:

        year = str(year)

        years.append(year)

        if word in global_freq.keys():
            global_freq[word]['total'] += 1
        else:
            global_freq[word] = {'total': 1}

        if year in global_freq[word].keys():
            global_freq[word][year] += 1
        else:
            global_freq[word][year] = 1


def count_all_years(speeches_dict):
    for year_file in speeches_dict.keys():
        year = year_file.split('.')[0]
        count_words_in_speech(year, speeches_dict[year_file])


def sort_freq_dict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


def sorted_global_freq():
    freq_dict = {k: global_freq[k]['total'] for k in global_freq.keys()}
    return sort_freq_dict(freq_dict)


def global_freq_to_db(target_speeches, collection):
    sorted_freq = sorted_global_freq()
    data = {'key': 'global', 'data': sorted_freq}

    result = collection.insert_one(data)
    print('inserted ' + result.inserted_id.__str__())


def word_freq_to_db(target_speeches, word, collection):

    series = [{
        'year': y,
        'count': global_freq[word].get(y, 0)
    } for y in sorted(list(set(years)))]

    data = {}
    data['word'] = word
    data['series'] = series
    collection.insert_one(data)


if __name__ == '__main__':
    client = MongoClient('mongo', 27017)
    db = client['speeches_count']

    years = []
    global_freq = {}

    target_speeches = extract_target_speeches()
    print(target_speeches)

    speeches_dict = get_speeches(target_speeches)
    count_all_years(speeches_dict)

    global_collection = db[target_speeches + '_global']
    global_collection.drop()
    global_freq_to_db(target_speeches, global_collection)

    word_collection = db[target_speeches + '_word']
    word_collection.drop()
    for word in global_freq.keys():
        word_freq_to_db(target_speeches, word, word_collection)
