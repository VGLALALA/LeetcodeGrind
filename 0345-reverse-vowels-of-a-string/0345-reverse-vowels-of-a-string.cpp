class Solution {
public:
    string reverseVowels(string s) {
        vector<char> word(s.begin(),s.end());
        int start = 0;
        int end = s.size() - 1;
        string vowels = "aeiouAEIOU";
        while(start < end){
            while(start < end && vowels.find(word[start]) == string::npos){
                start++;
            }
            while(start < end && vowels.find(word[end]) == string::npos){
                end--;
            }
            swap(word[start],word[end]);
            start++;
            end--;
        }
        string result;
        for(char c : word){
            result += c;
        }
        return result;
    }
};