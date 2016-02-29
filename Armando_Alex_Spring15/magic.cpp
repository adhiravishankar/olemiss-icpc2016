#include <iostream>

int main(int argc, char ** const argv) {
  unsigned int n;
  std::cin >> n;

  for (unsigned int i = 4; i < n; ++i) {
    if (n % i == 3) {
      std::cout << i << std::endl;
      break;
    }
  }

  return 0;
}
