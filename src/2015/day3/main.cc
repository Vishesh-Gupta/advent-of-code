#include <iostream>
#include <fstream>
#include <string>
#include <tuple>
#include <map>

int main(int argc, char *argv[]) {
  std::istream *infile = &std::cin;
  try {
    switch(argc) {
      case 2: infile = new std::ifstream(argv[1]); break;
      case 1: throw 1;
      default: throw 1;
    }
  } catch (...) {
    std::cerr << "usage " << argv[0] << "input";
    exit(1);
  }

  std::string directions{};
  std::getline(*infile, directions);
  std::map<std::tuple<int, int>, bool> visitedHouses;
  int north{},east{};
  int RoboNorth{}, RoboEast{};
  for (int i = 0; i < directions.size(); ++i) {
    char currDirection=directions[i];
    if (i % 2 == 0) {
      switch(currDirection) {
        case '^': north++; break;
        case '>': east++; break;
        case 'v': north--; break;
        case '<': east--; break; 
      }
      if (visitedHouses[std::tuple<int, int>(north, east)] == false) {
        visitedHouses[std::tuple<int, int>(north, east)] = true;
      } 
    } else {
      switch(currDirection) {
        case '^': RoboNorth++; break;
        case '>': RoboEast++; break;
        case 'v': RoboNorth--; break;
        case '<': RoboEast--; break; 
      }
      if (visitedHouses[std::tuple<int, int>(RoboNorth, RoboEast)] == false) {
        visitedHouses[std::tuple<int, int>(RoboNorth, RoboEast)] = true;
      }
    }
  }

  std::cout << "size" << visitedHouses.size() << std::endl;
  return 0;
}