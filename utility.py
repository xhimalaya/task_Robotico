import re, argparse


class FileIOOperation():
    def __init__(self, parser):
        self.output=[]
        try:
            self.filename = parser.filename
            with open(self.filename, 'r') as f:
                self.data = f.read()
            if parser.lines:
                self.output.append("Number of lines : {}".format(self.count_lines()))
            if parser.characters:
                self.output.append("Number of characters : {}".format(self.count_char()))
            if parser.words:
                self.output.append("Number of words :  {}".format(self.count_word()))
            if parser.numerics:
                self.output.append("numerics values : {}".format(self.display_neumaric()))
            if parser.alphabets:
                self.output.append("All alphabets: {}".format(self.display_alphabets()))
        except FileNotFoundError:
            print("File not found")
            exit()

    def count_char(self):
        return len(self.data)
    
    def count_word(self):
        return len(self.data.replace("."," ").replace(","," ").split(" "))
    
    def count_lines(self):
        return len(self.data.split("\n"))
    
    # def count_sentence(self):
    #     return len(self.data.split("."))
    
    def display_neumaric(self):
        return ",".join(re.findall("[\d]+",self.data))
    
    def display_alphabets(self):
        return "".join(re.findall("[a-zA-Z]+",self.data))

parser = argparse.ArgumentParser(description="Counts the number of lines,words, characters,numerics and alphabets in a file")
parser.add_argument("-l", "--lines",help="Counts the number of lines", action='store_true')
parser.add_argument("-c", "--characters",help="Counts the number of characters", action='store_true')
parser.add_argument("-w", "--words",help="Counts the number of words", action='store_true')
parser.add_argument("-n", "--numerics",help="Counts the number of numerics", action='store_true')
parser.add_argument("-a", "--alphabets",help="Counts the number of alphabets", action='store_true')
parser.add_argument('filename')
args = parser.parse_args()



fileIOobj= FileIOOperation(args)
for i in fileIOobj.output:
    print(i,"  ",fileIOobj.filename,"\n")
