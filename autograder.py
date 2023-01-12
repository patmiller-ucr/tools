import argparse

# parse cpp file name and --test file from command line
parser = argparse.ArgumentParser(description='Autograder for C++ files')
parser.add_argument('cppFilePath', type=str, help='Path to C++ file')
parser.add_argument('--test', type=int, required=False, help='Test number')

args = parser.parse_args()

# read cpp file and parse tests from file
with open(args.cppFilePath) as cppFile:
  cppFileLines = cppFile.readlines()
  print(cppFileLines)
