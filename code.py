"""
Load module to filter data on fly
"""
from __future__ import print_function
import pandas as pd

class Load():
    """
    Load class is used for exclusive dataframe filtering
    which takes `df` a csv file and convert into dataframe
    """
    def __init__(self, filename):
        self.version = open('VERSION').readlines()[0]
        self.df = pd.read_csv(filename)
        self.data = """W_A11,2000-02,Moving average,59.66666667,50.92582302,
                        68.40751031,Injuries,Number,Assault,Validated,Whole 
                        pop,All ages,FatalW_A11,2001-03,Moving average,60,10,
                        20,30,33,31,12,51.23477459,68.76522541,Injuries,
                        Number,Assault,Validated,Whole pop,All ages,Fatale 
                        50, 50, 60,pop,All ages,Fatal"""


    def get_version(self):
        """ Get current `version` of library"""
        return self.version

    def pick_numbers(self):
        """

        From self.data extract all numbers as a list
        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"

        :returns: [59.66666667,50.92582302,68.40751031]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_numbers()
            >> [1,2,3,4,5,6]

        """
        num = []
        for i in self.data.split(","):
            try:
                num.append(float(i))
            except ValueError:
                pass
        return num

    @classmethod
    def sum_all_numbers(cls):
        """
        From `self.data` extract all numbers and return the sum of all numbers

        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"
        :returns 179.0

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.sum_all_numbers()
            >> 179.0


        """
        num = df.pick_numbers()
        return sum(num)

    def extract_vowels(self):
        """
        Return all vowels in the given string `self.data`

        :returns [] all vowels as list

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.extract_vowels()
            >> ['A', 'E', 'I', 'O']
        """
        final = [each.upper() for each in self.data if each in "AeEeIiOoUu"]
        final_set = set(final)
        return list(final_set)

    @classmethod
    def pick_odd_numbers(cls):
        """
        Take the string from `self.data` and extract all odd numbers and return
        list of all odd numbers from the string

        :returns: [1, 3, 5]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_odd_numbers()
            >> [1, 3, 5]

        """
        num = df.pick_numbers()
        num = [round(i) for i in num]
        num1 = [i for i in num if i%2 != 0]
        return num1

    @classmethod
    def get_mean(cls):
        """
        Take the string from `self.data` and extract all numbers and return
        the mean of extracted list of numbers.

        :returns: 50

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_mean()
            >> 50
        """
        num = df.pick_numbers()
        return sum(num)/len(num)

    def get_all_categorical(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which are categorical variables

        :returns:   All categorical.
        :rtype:     List

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_categorical()
            >> ['Series_reference', 'Type']
        """
        cols = self.df.columns
        num_cols = self.df._get_numeric_data().columns
        return list(set(cols) - set(num_cols))

    def get_all_continuous(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which contain ccontinuous variables

        :returns:   All continuous.
        :rtype:    List

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_continuous()
            >> ['Lower_CI', 'Upper_CI', 'Units']
        """
        num_cols = self.df._get_numeric_data().columns
        return list(num_cols)

    @classmethod
    def addition(cls, x, y):
        """
        Take X and Y as input and now return the sum of both

        :param      x:    Number
        :type       x:    Integer
        :param      y:    Number
        :type       y:    Integer

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.addition(10, 20)
            >> 30
        """
        return x + y



if __name__ == '__main__':
    # instantiate the object
    df = Load('data.csv')
    print(df.addition(10, 20))
    print(df.pick_numbers())
    print(df.sum_all_numbers())
    print(df.extract_vowels())
    print(df.pick_odd_numbers())
    print(df.get_mean())
    print(df.get_all_categorical())
    print(df.get_all_continuous())
