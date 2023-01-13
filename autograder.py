import argparse
import subprocess

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

result = subprocess.run(['g++', args.cppFilePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
  print('Compilation failed')
  print(result.stderr.decode('utf-8'))
  exit(1)

result2 = subprocess.run(['./' + args.cppFilePath[:-4]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result2.stdout.decode('utf-8'))
