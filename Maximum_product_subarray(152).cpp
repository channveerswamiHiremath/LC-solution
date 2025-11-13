class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mn = nums[0];
        int mx = nums[0];
        int curr_max = nums[0];
        int max_pro = nums[0];

        for(int i = 1; i < nums.size(); i++){
            int prev_mx = mx;  
            mx = max(nums[i], max(nums[i] * mx, nums[i] * mn));
            mn = min(nums[i], min(nums[i] * prev_mx, nums[i] * mn));
            curr_max = mx;
            max_pro = max(curr_max, max_pro);
        }
        return max_pro;
    }
};
