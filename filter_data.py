import os
import csv

INPUT_TRACK_DATA_PATH = os.path.join(os.path.dirname(__file__), './sample_data/tracks.csv')
OUTPUT_TRACK_DATA_PATH = os.path.join(os.path.dirname(__file__), './sample_data/tracks_filtered.csv')


def process_data():
    with open(INPUT_TRACK_DATA_PATH, 'rb') as input_csv:
        dict_reader = csv.DictReader(input_csv, delimiter=';')
        reader = csv.reader(input_csv, delimiter=';')

        with open(OUTPUT_TRACK_DATA_PATH, 'w') as output_csv:
            writer = csv.writer(output_csv, delimiter=';')
            writer.writerow(dict_reader.fieldnames)

            for row in reader:
                # nan values
                if any([value == 'nan' for value in row]):
                    continue
                # zero confidence
                if row[11] == '0.0' or row[14] == '0.0' or row[15] == '0.0' or row[19] == '0.0':
                    continue
                # confidence not in [0;1]
                if float(row[11]) > 1.0 or float(row[14]) > 1.0 or float(row[15]) > 1.0 or float(row[19]) > 1.0:
                    continue
                # tempo > 500
                if float(row[17]) > 500:
                    continue
                # fade out > duration
                if float(row[16]) > float(row[8]):
                    continue
                # fade in > duration
                if float(row[9]) > float(row[8]):
                    continue
                # no year
                if row[3] != '0'
                    continue
                writer.writerow(row)


if __name__ == '__main__':
    process_data()
