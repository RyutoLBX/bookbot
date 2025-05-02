from stats import *
from sys import exit, argv

def main():
  if len(argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
  
  print_analysis(argv[1])

main()
