#include <iostream>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>

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

    int lineLength = lines[0].size();
    std::vector<std::map<char, int>> freqsPerColumn(lineLength);

    for(const auto& line : lines)
    {
        for(int i = 0; i < lineLength; i++)
        {
            freqsPerColumn[i][line[i]] += 1;
        }
    }

    std::string message;
    for(const auto& freqs : freqsPerColumn)
    {
        std::vector<std::pair<char, int>> counts;
        for(const auto& pair : freqs)
                counts.push_back(pair);

        sort(counts.begin(), counts.end(),
            [](const auto& a, const auto& b)
            {
            return a.second < b.second;
            });

        message += counts[0].first; 
    }

    std::cout << message << std::endl;

}
