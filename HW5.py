
# Your name:
# Your student id:
# Your email:
# List who you have worked with on this homework:

import re, os, unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines

def find_bio_names(string_list):
    """
    This function returns a dictionary with the keys being numbers, (1 - 10)
    and the values being the names of each biography subject
    """
    pass

def find_contractions_and_possessives(string_list):
    """
    This function finds all (real, English language) words with an apostrophe in them
    """
    pass

def find_section_headings(string_list):
    """
    This functions returns a list of section headings in the list of strings
    """
    pass

def find_birth_years(string_list):
    """
    This function returns a dictionary where the keys are names and the values are corresponding birth years
    If the birth year is unknown, use the string 'unknown' in place of a birth year
    Hint: you could call your find_bio_names function here to help
    """
    pass

## Extra credit
def count_mid(string_list, middle):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word, not at 
    the start of end
    """
    pass

#Implement your own tests
class TestAllMethod(unittest.TestCase):

    def test_find_bio_names(self):
        pass

    def test_find_contractions_and_possessives(self):
        pass

    def test_find_section_headings(self):
        pass

    def test_find_birth_years(self):
        pass

    #Uncomment if working on Extra Credit
    #def test_count_mid(self):
    #    pass

def main():
    #Feel free run your functions here as well!
    bios = read_file("best_picture.txt")
    

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)