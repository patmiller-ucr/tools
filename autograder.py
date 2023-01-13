import argparse
import subprocess
import sys

def runSubprocess(commands):
  output = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if output.returncode != 0:
    print('Compilation failed')
    print(output.stderr.decode('utf-8'))
    sys.exit(1)
  return output.stdout.decode('utf-8')

# parse cpp file name and --test file from command line
parser = argparse.ArgumentParser(description='Autograder for C++ files')
parser.add_argument('cppFilePath', type=str, help='Path to C++ file')
parser.add_argument('--test', type=int, required=False, help='Test number')

args = parser.parse_args()
tests = []

# read cpp file and parse tests from file
with open(args.cppFilePath) as cppFile:
  cppFileLines = cppFile.readlines()

  # parse tests from cpp file
  for i in range(len(cppFileLines)):
    if cppFileLines[i].lower().startswith('// test'):
      tests.append(cppFileLines[i])
      tests.append(cppFileLines[i+1])
      tests.append(cppFileLines[i+2])

# compile cpp file and ensure that it does not have any errors
compilation = runSubprocess(['g++', args.cppFilePath])
# run compilation and capture output
output = subprocess.run(['./a.out'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(output.stdout.decode('utf-8'))
