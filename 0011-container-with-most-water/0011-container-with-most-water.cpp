class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_v = 0;
        int lp = 0, hp = height.size() - 1;
        while(lp < hp){
            int width = hp - lp;
            int area = width * min(height[lp], height[hp]);
            max_v = max(max_v, area);
            if(height[lp] < height[hp]){
                lp++;
            }
            else{
                hp--;
            }
        }
        return max_v;
    }
};