import json
from read_files import get_speeches, write_list_to_csv
from utils import get_sanitized_wordlist


class ChristmasCounter(object):

    def __init__(self, speeches_dict):
        self.speeches_dict = speeches_dict
        self.freq_per_year = {}
        self.global_freq = {}

    def count_words_in_speech(self, year, speech_string):
        sanitized_wordlist = get_sanitized_wordlist(speech_string)

        for word in sanitized_wordlist:

            if word in self.global_freq.keys():
                self.global_freq[word] += 1
            else:
                self.global_freq[word] = 1

            year = str(year)
            if year not in self.freq_per_year.keys():
                self.freq_per_year[year] = {}

            if word in self.freq_per_year[year].keys():
                self.freq_per_year[year][word] += 1
            else:
                self.freq_per_year[year][word] = 1

    def count_all_years(self):
        for year_file in self.speeches_dict.keys():
            year = year_file.split('.')[0]
            self.count_words_in_speech(year, speeches_dict[year_file])

    def sort_freq_dict(self, freqdict):
        aux = [(freqdict[key], key) for key in freqdict]
        aux.sort()
        aux.reverse()
        return aux

    def sorted_global_freq(self):
        return self.sort_freq_dict(self.global_freq)

    def sorted_year_freq(self, year):
        year = str(year)
        return self.sort_freq_dict(self.freq_per_year[year])

    def global_freq_to_csv(self):
        sorted_freq = self.sorted_global_freq()
        write_list_to_csv(sorted_freq, 'frequency.csv')

    def year_freq_to_csv(self, year):
        year = str(year)
        sorted_freq = self.sorted_year_freq(year)
        write_list_to_csv(sorted_freq, 'frequency_%s.csv' % year)

    def global_freq_to_json(self):
        data = {'data': self.global_freq}
        with open('frequency.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)

    def year_freq_to_json(self, year):
        year = str(year)
        year_file = '%s.json' % year
        data = self.freq_per_year[year]
        with open(year_file, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)



if __name__ == '__main__':

    speeches_dict = get_speeches()
    counter = ChristmasCounter(speeches_dict)
    counter.count_all_years()

    counter.global_freq_to_json()
    #  counter.year_freq_to_json(1999)
    #  counter.year_freq_to_json(2000)
    #  counter.global_freq_to_csv()
    #  counter.year_freq_to_csv(1949)
    #  counter.year_freq_to_csv(1962)
    #  counter.year_freq_to_csv(1989)
    #  counter.year_freq_to_csv(2017)
