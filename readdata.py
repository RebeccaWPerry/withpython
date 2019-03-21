""" Demonstrate use of Python for reading and plotting data from csv file.

csv reading based on: https://realpython.com/python-csv/

The csv and collections modules are part of the Python Standard Library.

The sample csv file used in this example is available at:
https://drive.google.com/drive/folders/1giaGOhJYWIXfZzy-zxmbrUIOB9Y_ROdu
"""

import csv
from collections import Counter
import matplotlib.pyplot as plt

#NOTE: for Python to find the csv file, you must CD (change directory) to the
#directory containing the downloaded csv file or modify the csvfile variable
#to be the full filepath for the csv file

#sample csv is the 2018 Python Developer's Survey
csvfile = 'python_psf_external_18.csv'

#import some of the data from the csv into a list
usecase_responses = []
with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            questions = [question for question in row]
            usecase_index = questions.index('What do you use Python for the most?')
            line_count += 1
        else:
            usecase_responses.append(row[usecase_index])
            line_count += 1
    print(f'Processed {line_count} lines.')

#how many responses were for each Python use case
usecase_counts = Counter(usecase_responses)

#how many different use cases were there?
n_usecases = len(usecase_counts)

#create a histogram
plt.figure(figsize=(10, 10))
plt.barh(range(n_usecases), list(usecase_counts.values()))
plt.xticks(fontsize=12)
plt.yticks(range(n_usecases), list(usecase_counts.keys()),
           rotation='horizontal', fontsize=12)
plt.xlabel('Number of Respondents', fontsize=12)
plt.title('2018 Python Developer Survey\n'
          'What do you use Python for the most?', fontsize=18)
plt.tight_layout()
plt.show()
