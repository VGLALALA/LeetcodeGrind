class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int best = 1, up = 1, down = 1;
        for (int i = 0; i + 1 < nums.size(); i++) {
            int a = nums[i];
            int b = nums[i + 1];

            up = a < b ? up + 1 : 1;
            down = a > b ? down + 1 : 1;
            best = max(best, max(up, down));
        }
        return best;
        
    }
};