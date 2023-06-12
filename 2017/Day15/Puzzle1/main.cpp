#include <cstdint>
#include <iostream>
#include <deque>
#include <algorithm>

typedef std::deque<int64_t> generator;

int processed;

int64_t generate(int64_t previous, int64_t factor)
{
    return (previous * factor) % 2147483647ll;
}

bool compare(int64_t a, int64_t b)
{
    return (a & 0xFFFF) == (b & 0xFFFF);
}

int processQueues(generator& a, generator& b)
{
    int result = 0;
    size_t size = std::min(a.size(), b.size());
    for(size_t i = 0; i < size; ++i)
    {
        ++processed;
        result += compare(a[0], b[0]);
        a.pop_front();
        b.pop_front();
    }

    return result;
}

int main(int argc, char** argv)
{
    int64_t a = 618;
    int64_t b = 814;

    int result = 0;

    processed = 0;

    generator genA;
    generator genB;

    while(processed < 5000000)
    {
        a = generate(a, 16807ll);
        b = generate(b, 48271ll);

        if((a % 4) == 0) genA.push_back(a);
        if((b % 8) == 0) genB.push_back(b);

        result += processQueues(genA, genB);
    }

    std::cout << result << std::endl;

    return 0;
}