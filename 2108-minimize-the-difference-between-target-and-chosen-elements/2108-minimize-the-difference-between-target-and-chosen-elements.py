class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Start with a set containing only sum 0 (no rows chosen yet)
        possible_sums = {0}
        
        for row in mat:
            new_sums = set()
            for val in row:
                for s in possible_sums:
                    new_sums.add(s + val)
            possible_sums = new_sums
        
        # Find the sum with minimal absolute difference to target
        min_diff = float('inf')
        for s in possible_sums:
            diff = abs(target - s)
            if diff < min_diff:
                min_diff = diff
                if min_diff == 0:   # cannot get better than zero
                    break
        
        return min_diff

