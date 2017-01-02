#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <sstream>

std::vector<std::string> split(const std::string& p_input)
{
    std::vector<std::string> res;
    std::string buff;
    std::stringstream ss(p_input);
    while(ss >> buff)
        res.push_back(buff);
    return res;
}

bool isRegister(const std::string& p_str)
{
    return p_str == "a" || p_str == "b" || p_str == "c" || p_str == "d";
}

int main(int argc, char** argv)
{
    if(argc < 2)
    {
        std::cout << "Usage: " << argv[0] << " <input_filename>" << std::endl;
        return 1;
    }

    std::ifstream file(argv[1]);
    std::vector<std::string> lines;
    std::string part;
    while(std::getline(file, part))
    {
        lines.push_back(part);
    }

    std::map<std::string, int> registers;
    registers["c"]++;
    for(int i = 0; i < lines.size(); ++i)
    {
        auto command = split(lines[i]);
        if(command[0] == "cpy")
        {
            if(isRegister(command[2]))
            {
                if(isRegister(command[1]))
                {
                    registers[command[2]] = registers[command[1]];
                }
                else
                {
                    registers[command[2]] = std::stoi(command[1]);
                }
            }
        }
        if(command[0] == "inc")
        {
            registers[command[1]]++;
        }
        if(command[0] == "dec")
        {
            registers[command[1]]--;
        }
        if(command[0] == "jnz")
        {
            int jump = 0;
            if(isRegister(command[1]) && registers[command[1]] != 0)
            {
                jump = std::stoi(command[2]);
            }
            else if(!isRegister(command[1]) && std::stoi(command[1]) != 0)
            {
                jump = std::stoi(command[2]);
            }
            if(jump != 0)
            {
                jump--;
                i += jump;
            }
        }
    }
    std::cout << registers["a"] << std::endl;
}
