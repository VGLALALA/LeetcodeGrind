class Solution {
public:
    string reverseWords(string s) {
        vector<string> slst;
        stringstream ss(s);
        string word;
        while(ss >> word){
            slst.push_back(word);
        }
        reverse(slst.begin(),slst.end());
        string out;
        for (int i = 0; i < slst.size(); i++) {
            out += slst[i];
            if (i < slst.size() - 1) {
                out += " ";
            }
        }
        return out;
    }
};