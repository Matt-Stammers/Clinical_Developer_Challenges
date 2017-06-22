
// Example program by Jeremy Thornton - CDC
#include <iostream>
#include <string>

int main() {
  std::cout << "What's up Doc?\n"
  << "1: pneumothorax\n"
  << "2: shock\n"
  << "3: seizures" << std::endl;
  int a, b;
  std::cin >> a >> b;
  std::cout << "First treat ";
  switch (a+b) {
    case 3:
        std::cout << "pneumothorax!";
        break;
    case 4:
        std::cout << "seizures!";
        break;
    case 5:
        std::cout << "shock!";
        break;
  }
  std::cout << std::endl;
}
