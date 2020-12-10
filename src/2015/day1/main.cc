#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

int main(int argc, char*argv[]) {
  std::string filename = "input";
  std::istream *infile = &std::cin;
  try {
    switch (argc) {
      case 2: filename = argv[1]; break;
      case 1: throw 1;
      default: throw 1;
    }
  } catch ( ... ) {
    std::cerr << "usage" << argv[0] << "input" << std::endl;
    exit( 1 );
  }

  infile = new std::ifstream(filename);

  int left{ 0 }, right{ 0 };

  char parenthesis{};
  int position_basement{};

  while (!infile->eof()) {
    *infile >> parenthesis;
    if (parenthesis == '(') {
      left++;
    } else {
      right++;
    }
    position_basement++;
    if (left - right == -1) {
      break;
    } 
  }

  if (parenthesis == '(') {
    left--;
  } else {
    right--;
  }

  std::cout << "floors: " << left - right << std::endl;
  std::cout << "position: " << position_basement; 

  return 0;
}