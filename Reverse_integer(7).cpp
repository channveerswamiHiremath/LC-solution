class Solution {
public:
    int reverse(int x) {
        long long rem = 0;
        if (x > 0) {
            long long val = x;
            while (val > 0) {
                int v = val % 10;
                rem = rem * 10 + v;
                val = val / 10;
            }
        } else {
            long val = -(long long)x;
            while (val > 0) {
                int v = val % 10;
                rem = rem * 10 + v;
                val = val / 10;
            }
            rem = -rem;
        }

        if (rem > INT_MAX || rem < INT_MIN) {
            return 0;
        }
        return (int)rem;
    }
};