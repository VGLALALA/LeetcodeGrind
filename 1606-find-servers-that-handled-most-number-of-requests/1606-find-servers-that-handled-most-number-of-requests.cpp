class Solution {
public:
/*
 free = list(range(k))  # already a heap: each free server is keyed by its next turn

        handled, busy = [], []  # busy: (time it frees up, server)
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:  # done by time t
                heappush(free, i + (heappop(busy)[1] - i) % k)  # its first turn from i on
            if free:  # otherwise the request is dropped
                x = heappop(free) % k
                heappush(busy, (t + d, x))
                handled.append(x)

        return multimode(handled)
*/  
    vector<int> multimode(vector<int>& nums) {
        unordered_map<int, int> freq;
        int maxFreq = 0;

        for (int x : nums) {
            maxFreq = max(maxFreq, ++freq[x]);
        }

        vector<int> result;
        for (int x : nums) {
            if (freq[x] == maxFreq) {
                result.push_back(x);
                freq[x] = 0;
            }
        }
        return result;
    }
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        priority_queue<int, vector<int>, greater<int>> freeServer;
        priority_queue<
            pair<long long, int>,
            vector<pair<long long, int>>,
            greater<pair<long long, int>>
        > busy;
        for (int i = 0; i < k; i++) {
            freeServer.push(i);
        }
        vector<int> handled;
        int n = arrival.size();
        for(int i = 0; i < n; i++){
            int t = arrival[i], d = load[i];
            while (busy.size() > 0 && busy.top().first <= t){
                int server = busy.top().second;
                busy.pop();

                freeServer.push(i + (server - i % k + k) % k);
            }
            if(!freeServer.empty()){
                int x = freeServer.top() % k;
                freeServer.pop();
                busy.push({(long long)t + d, x});
                handled.push_back(x);
            }
        }
        return multimode(handled);

    }
};