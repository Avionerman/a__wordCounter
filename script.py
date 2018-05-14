from decimal import *
import os
import time
import sys


def simple(x_file):
    filename = x_file

    di = dict()
    total = dict()
    with open(filename, 'r', encoding='ISO_8859-1:1987') as file:
        for line in file:
            line = line.rstrip()

            words = line.split()

            for W in words:
                di[W] = di.get(W, 0) + 1    # Save the information into a dictionary.

    class color:    # Because of the vast information, I had to put color in the numbers that I wanted to focus on.
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'


    """ At this point I am searching and collecting the frequence of each word in every file. """
    sum = 0
    biggestFreq = -1
    biggestWord = None
    for index, value in di.items():
        print(index, value)
        string = str(index) + " " + str(value)
        sum = sum + value
        if value > biggestFreq:
            biggestFreq = value
            biggestWord = index

    print('The word ' + color.BLUE + color.BOLD + color.UNDERLINE + biggestWord + color.END
          + ' was the most frequent in the current file with '
          + color.BLUE + color.BOLD + color.UNDERLINE + str(biggestFreq) + color.END + ' appears')


    """ Finding the different words that exists in each file. """
    total_diff_words = len(di)
    print("Total sum of word counting is: ", color.RED + color.BOLD + color.UNDERLINE + str(sum) + color.END)
    print("The total different words are: ",
          color.RED + color.BOLD + color.UNDERLINE + str(total_diff_words) + color.END)

    getcontext().prec = 3
    median = Decimal(sum) / Decimal(total_diff_words)
    print("Median equals to:", color.RED + color.BOLD + color.UNDERLINE + str(median) + color.END)
    print("\n\n\n\n\n\n")

    """ Collecting the words that are having sum higher than the median of the words, for the current file. """
    sumKeeper = 0
    for index1, value1 in di.items():
        if value1 > median:
            indexKeeper = index1
            sumKeeper = sumKeeper + 1
            print(indexKeeper)

    print('Totally found: ' + color.BLUE + color.BOLD + color.UNDERLINE + str(sumKeeper) + color.END + ' words')

    getcontext().prec = 3
    percentage = (Decimal(sumKeeper) / Decimal(total_diff_words)) * 100
    median_total = (Decimal(median) / Decimal(1))
    string = str(percentage) + "%"

    print("Only the " + color.BLUE + color.BOLD + color.UNDERLINE + str(string) + color.END +
          " of the total words are having counter higher than the Median frequency "
          + color.BLUE + color.BOLD + color.UNDERLINE + str(median_total) + color.END)



def main():
    os.chdir('/home/avioner/Desktop/scripts_python/word_counter/etext01')   # IMPORTANT! Here you must insert the directory or path in which your file/s exist.

    beginning_time = time.time()    # Collecting the beginning time to see how much time needs.
    counter = 0
    for f in os.listdir():          # From the above line, ''os.chdir'' I keep in a list the name of the total files that exists in there
        simple(f)
        counter = counter +1        # Counting the sum of the files that I am reading (testify).
    print("Demanded time: ", time.time()-beginning_time)
    print("\n Total txt files: ", counter)

if __name__=="__main__":
    main()
