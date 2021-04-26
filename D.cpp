#include <iostream>
#include <cmath>
using namespace std;

uint16_t move(uint16_t x, int len)
{
    uint16_t temp = x & 0b1;
    x >>= 1;
    x |= temp << (len - 1);
    return x;
}

int main()
{
    uint16_t N, m;
    cin >> N;
    m = N;
    int len = trunc(log2((float)N)) + 1;
    for (int i = 0; i < len; i++)
    {
        N = move(N, len);
        if(N > m) m = N;
    }
    cout << m;
    return 0;
}