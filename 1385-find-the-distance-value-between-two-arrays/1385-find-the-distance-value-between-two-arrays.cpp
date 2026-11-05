class Solution {
public:
    bool helper(int v, vector<int>& arr2, int d){
        for(int j = 0; j < arr2.size(); j++){
                if(abs(v - arr2[j]) <= d){
                    return false;
                }
            }
        return true;
    }
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int cnt = 0;
        for(int i = 0; i < arr1.size(); i++){
            if(helper(arr1[i], arr2, d)){
                cnt++;
            }
        }
        return cnt;
    }
};