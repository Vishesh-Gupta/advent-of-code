#include <iostream>
#include <string>
#include <fstream>
#include "md5.h"

bool mining5(std::string hash) {
  MD5 md5;

  std::string hashed = md5(hash);
  for (int i = 0; i < 5; i++) {
    if (hashed[i] != '0') return false;
  }

  return true;
}

bool mining6(std::string hash) {
  MD5 md5;

  std::string hashed = md5(hash);
  for (int i = 0; i < 6; i++) {
    if (hashed[i] != '0') return false;
  }

  return true;
}

int main(int argc, char *argv[]) {
  std::istream  *infile = &std::cin;

  try {
    switch(argc) {
      case 2: infile = new std::ifstream(argv[1]); break;
      case 1: throw 1;
      default: throw 1;
    } 
  } catch (...) {
    std::cerr << "usage " << argv[0] << " input";
    exit(1);
  }

  int i = 0;
  std::string secretKey{};
  std::string hash = secretKey + std::to_string(i);
  std::getline(*infile, secretKey);
  while (!mining5(hash)) {
    hash = secretKey + std::to_string(i);
    i++;
  }
  std::cout << "MD5 (atleast 5 zeros) number: " << i - 1 << std::endl;
  i = 0;
  while (!mining6(hash)) {
    hash = secretKey + std::to_string(i);
    i++;
  }
  std::cout << "MD5 (atleast 6 zeros) number: " << i - 1 << std::endl;

  return 0;
}