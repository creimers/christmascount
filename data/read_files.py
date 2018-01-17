import os
import csv

file_dir = os.path.dirname(os.path.abspath(__file__))


def get_speeches(target_speeches):
    """
    Args:
        target_speeches (string): name of speeches dir
    Returns:
        speeches_dir (dict)
    """
    speeches_dir = os.path.join(file_dir, 'speeches', target_speeches)
    if not os.path.isdir(speeches_dir):
        raise IOError('speech dir %s does not exist' % target_speeches)

    speeches_dict = {}

    for speech in os.listdir(speeches_dir):
        speech_file = os.path.join(speeches_dir, speech)

        with open(speech_file, 'r') as speech_file_content:
            data = speech_file_content.read()\
            	.replace('\n', '')\
            	.replace(',', '')\
            	.replace('.', '')\
            	.replace('"', '')\
            	.replace('„', '')\
            	.replace('»', '')\
            	.replace("'", '')\
            	.replace(";", '')\
            	.replace("–", '')\
            	.replace("-", '')\
            	.replace("?", '')\
            	.replace("!", '')\
            	.replace("@", '')\
            	.replace(":", '')

            speeches_dict[speech] = data

    return speeches_dict


def write_list_to_csv(mylist, filename):

	csv_path = os.path.join(file_dir, filename)
	with open(csv_path, 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		wr.writerow(["count", "word"])
		for elm in mylist:
			wr.writerow([elm[0], elm[1]])


if __name__ == '__main__':
    get_speeches()
