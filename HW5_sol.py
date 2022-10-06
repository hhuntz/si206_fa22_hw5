# Your name: SOLTUION
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
    name_dict = {}
    name_counter = 1
    reg_exp = r'\b[Nn]ame: '
    for line in string_list:
        line = line.rstrip()
        x = re.findall(reg_exp, line)
        if x:
            name_dict[name_counter] = line[6:]
            name_counter += 1
    return name_dict

def find_possessives(string_list):
    """
    This function finds all words with an apostrophe in the middle
    hint: 
    """
    contraction_list = []
    reg_exp = r"\b[A-Za-z]*'[A-Za-z]+\b"
    for line in string_list:
        for word in line.split():
            x = re.findall(reg_exp, word)
            if x:
                contraction_list.extend(x)
    return contraction_list

def find_section_headings(string_list):
    '''
    This functions returns a list of section headings from a list of strings
    '''
    reg_exp = r'==+.+==+'
    section_headings = []

    for line in string_list:
        for word in line.split():
            x = re.findall(reg_exp, word)
            if x:
                section_headings.extend(x)

    return section_headings

def find_birth_years(string_list):
    """
    This function returns a dictionary where the keys are names and the values are corresponding birth years
    """
    names = list(find_bio_names(string_list).values())
    years_dict = {}
    years = []
    reg_exp = r'\b(B|b)orn: '

    for string in string_list:
        x = re.findall(reg_exp, string)
        if x:
            if string[-8:-1] != 'unknown':
                years.append(string[-5:-1])
            else:
                years.append('unknown')
    for i in range(len(names)):
        years_dict[names[i]] = years[i]
    
    return years_dict


## Extra credit
def count_mid(string_list, middle):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word, not at 
    the start of end
    """
    reg_exp = r'\b[A-Za-z]+' + re.escape(middle) + r'[A-Za-z]+\b'

    words = []

    for line in string_list:
        x = re.findall(reg_exp, line)
        for i in x:
            words.append(i[0])

    return len(words)

#Implement your own tests
class TestAllMethod(unittest.TestCase):

    def setUp(self):
        self.bios = read_file("206_hw5_wiki_bios.txt")

    def test_find_bio_names(self):
        self.assertEqual(find_bio_names(["Name: Holden", "name: Barb Ericson", "title: The Sandlot"]), {1: "Holden", 2: "Barb Ericson"})
        self.assertEqual(find_bio_names([]), {})

    def test_findpossessives(self):
        self.assertEqual(find_possessives([]), [])
        self.assertEqual(find_possessives(["Can't", "won't", "Harris' ballons won't fly"]), 
            ["Can't", "won't", "won't"])
        self.assertEqual(len(find_possessives(self.bios)), 8)

    def test_find_section_headings(self):
        self.assertEqual(find_section_headings([]), [])
        self.assertEqual(find_section_headings([
            '===yep===',
            '=no=',
            '==yes==',
            'nope',
            'shouldnot=work'
            'shouldnot==work'
        ]), ['===yep===', '==yes=='])

    def test_find_birth_years(self):
        self.assertEqual(len(find_birth_years(self.bios)), 10)
        self.assertEqual(find_birth_years(['Name: Holden', 'Born: 1995\n']), {'Holden': '1995'})

    #Uncomment if working on Extra Credit
    def test_count_mid(self):
        self.assertEqual(count_mid(self.bios, "a"), 581)
        self.assertEqual(count_mid(self.bios, "is"), 45)

def main():
    #Feel free run your functions here as well!
    #bios = read_file("206_hw5_wiki_bios.txt")
    pass

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)