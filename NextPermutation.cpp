class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        next_permutation(nums.begin(), nums.end());
    }
};

// Used the built function next_permutation to find the next permutation of the array
// [1,2,3] would be [1,3,2] much easier than any other langauge so i chose to do it in 
// c++ for time efficiency.
