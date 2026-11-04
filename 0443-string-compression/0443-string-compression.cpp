class Solution {
public:
    int compress(vector<char>& chars) {
        int ans = 0;
        int i = 0;
        while(i < chars.size()){
            char letter = chars[i];
            int count = 0;
            while(i < chars.size() && chars[i] == letter){
                count++;
                i++;
            }
            chars[ans] = letter;
            ans++;
            if(count > 1){
                for(char c : to_string(count)){
                    chars[ans] = c;
                    ans++;
                }
            }
            
        }
        return ans;
    }
};