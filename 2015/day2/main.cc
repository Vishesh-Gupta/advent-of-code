#include <iostream>
#include <string>
#include <fstream>


unsigned int calculate_area(int l, int w, int h) {
  int lw = l*w, wh=w*h, hl=h*l;
  int smallestSide = std::min(std::min(lw, wh), hl);
  return 2*(lw) + 2*(wh) + 2*(hl) + smallestSide;  
}

unsigned int calculate_perimeter(int l, int w, int h) {
  int smallestSide = std::min(std::min(l,w), h);
  int secondSmallest{};
  if (smallestSide == l) {
    secondSmallest = std::min(w,h);
  } else if (smallestSide == w) {
    secondSmallest = std::min(l, h);
  } else if (smallestSide == h) {
    secondSmallest = std::min(l, w);
  }
  int tie = 2*secondSmallest+2*smallestSide;
  int bow = l*w*h;
  return bow + tie;
}

int main(int argc, char*argv[]) {
  std::istream *infile = &std::cin;

  try{
    switch(argc) {
      case 2: infile = new std::ifstream(argv[1]); break;
      case 1: throw 1;
      default: throw 1;
    }
  } catch (...) {
    std::cout << "usage: " << argv[0] << "input" << std::endl;
    exit( 1 );
  }

  int totalGiftWrap{};
  int totalRibbonLength{};
  std::string giftSize{};
  while (std::getline(*infile, giftSize)) {
    int l{0}, w{0}, h{0};
    for (;;) {
      int i = 0; 
      while (giftSize[i] != 'x') {
        if (l != 0) l *= 10;
        l += giftSize[i] - '0';
        i++;
      }
      i++;
      while (giftSize[i] != 'x') {
        if (h != 0) h *= 10;
        h += giftSize.at(i) - '0';
        i++;
      }
      i++;
      while (i < giftSize.size()) {
        if (w != 0) w *= 10;
        w += giftSize.at(i) - '0';
        i++;
      }
      break;
    }
    unsigned int area = calculate_area(l,w,h);
    unsigned int perimeter = calculate_perimeter(l,w,h);
    totalGiftWrap += area;
    totalRibbonLength += perimeter;

  }

  std::cout << "total: " << totalGiftWrap << std::endl;
  std::cout << "total Ribbon Length: " << totalRibbonLength;
  delete infile;
  return 0; 
}