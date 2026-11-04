
class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size();

        // Coordinate compression
        vector<int> vals(nums.begin(), nums.end());
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());

        int m = vals.size();
        unordered_map<int, int> pos_of;

        for (int i = 0; i < m; i++) {
            pos_of[vals[i]] = i + 1;
        }

        vector<int> rk;
        for (int v : nums) {
            rk.push_back(pos_of[v]);
        }

        // Fenwick trees
        vector<int> cnt(m + 1, 0);
        vector<long long> sm(m + 1, 0);

        int top = 1;
        while (top * 2 <= m) {
            top *= 2;
        }

        int need = (x + 1) / 2;
        int w = n - x + 1;

        vector<long long> cost(w, 0);
        long long total = 0;

        // Sliding window
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            total += v;

            int p = rk[i];
            while (p <= m) {
                cnt[p]++;
                sm[p] += v;
                p += p & -p;
            }

            if (i >= x) {
                int u = nums[i - x];
                total -= u;

                p = rk[i - x];
                while (p <= m) {
                    cnt[p]--;
                    sm[p] -= u;
                    p += p & -p;
                }
            }

            if (i >= x - 1) {
                int pos = 0;
                int rem = need;
                long long s0 = 0;

                int pw = top;
                while (pw > 0) {
                    int nxt = pos + pw;

                    if (nxt <= m && cnt[nxt] < rem) {
                        pos = nxt;
                        rem -= cnt[nxt];
                        s0 += sm[nxt];
                    }

                    pw >>= 1;
                }

                long long med = vals[pos];
                int c0 = need - rem;

                cost[i - x + 1] =
                    med * c0 - s0
                    + (total - s0)
                    - med * (x - c0);
            }
        }

        // Dynamic programming
        const long long INF = 1LL << 60;
        vector<long long> prev(n + 1, 0);

        for (int t = 0; t < k; t++) {
            vector<long long> cur(n + 1, INF);

            for (int j = x; j <= n; j++) {
                long long a = cur[j - 1];
                long long b = prev[j - x] + cost[j - x];

                cur[j] = min(a, b);
            }

            prev = cur;
        }

        return prev[n];
    }
};
