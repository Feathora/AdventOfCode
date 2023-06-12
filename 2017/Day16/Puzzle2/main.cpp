#include <iostream>
#include <vector>
#include <functional>
#include <sstream>
#include <string>
#include <fstream>
#include <array>
#include <deque>
#include <time.h>

typedef std::vector<std::function<void()>> Dance;

struct Program
{
    char c;
};

typedef std::deque<Program*> ProgramList;
static ProgramList programs;

void Spin(char n)
{
    // for(int i = programs.size() - n; i < programs.size(); ++i)
    // {
    //     auto program = programs[programs.size() - 1];
    //     programs.pop_back();
    //     programs.push_front(program);
    // }
}

void Exchange(char l, char r)
{
    std::swap(programs[l], programs[r]);
}

void Partner(char l, char r)
{
    // char lPos = -1, rPos = -1;
    // for(char i = 0; i < programs.size(); ++i)
    // {
    //     if(programs[i]->c == l)
    //     {
    //         lPos = i;
    //         if(rPos != -1) break;
    //     }
    //     else if(programs[i]->c == r)
    //     {
    //         rPos = i;
    //         if(lPos != -1) break;
    //     }
    // }

    // Exchange(lPos, rPos);
}

int main(int argc, char** argv)
{
    std::ifstream ifs("input.txt");
    std::string content( (std::istreambuf_iterator<char>(ifs) ),
                       (std::istreambuf_iterator<char>()    ) );

    Dance dance;

    std::istringstream iss(content);
    std::string s;
    while(std::getline(iss, s, ','))
    {
        char type = s[0];
        if(type == 's')
        {
            char n = std::stoi(s.substr(1));
            std::function<void()> f = std::bind(Spin, n);
            dance.push_back(f);
        }
        else
        {
            int slashIndex = s.find_first_of('/');
            std::string l = s.substr(1, slashIndex - 1);
            std::string r = s.substr(slashIndex + 1);
            if(type == 'x')
            {
                std::function<void()> f = std::bind(Exchange, std::stoi(l), std::stoi(r));
                dance.push_back(f);
            }
            else if(type == 'p')
            {
                std::function<void()> f = std::bind(Partner, l[0], r[0]);
                dance.push_back(f);
            }
        }
    }

    for(int i = 0; i < 16; ++i)
    {
        auto program = new Program();
        program->c = 'a' + i;
        programs.push_back(program);
        //if(i != 0) programs[i]->previous = programs[i - 1];
        //if(i != programs.size() - 1) programs[i]->next = programs[i + 1];
    }

    clock_t start = clock();

    for(int i = 0; i < 1000; ++i)
    {
        for(auto& move : dance)
        {
            move();
        }
    }

    std::cout << (double)(clock() - start)/CLOCKS_PER_SEC << std::endl;

    std::string result;
    for(int i = 0; i < programs.size(); ++i)
    {
        result += programs[i]->c;
    }

    std::cout << result << std::endl;
}