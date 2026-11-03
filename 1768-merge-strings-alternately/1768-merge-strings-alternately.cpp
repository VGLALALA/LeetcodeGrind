#include <string>
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ns = "";
        int len = min(word1.size(), word2.size());
        for(int i = 0; i < len; i++){
            ns += word1[i];
            ns += word2[i];
        }
        
        ns += word1.substr(len);
        ns += word2.substr(len);
        return ns;
    }
};