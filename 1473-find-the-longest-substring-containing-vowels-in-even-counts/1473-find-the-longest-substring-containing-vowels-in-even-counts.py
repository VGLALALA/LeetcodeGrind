class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map each vowel to a unique bit position
        vowel_to_bit = {'a': 1 << 0, 'e': 1 << 1,
                        'i': 1 << 2, 'o': 1 << 3, 'u': 1 << 4}
        
        # state represents parity (even/odd) of each vowel seen so far
        state = 0
        first_occurrence = {0: -1}   # state 0 occurs before string starts
        max_len = 0
        
        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                # Toggle the bit corresponding to this vowel
                state ^= vowel_to_bit[ch]
            
            if state in first_occurrence:
                # Substring from after previous occurrence of same state to current index
                max_len = max(max_len, i - first_occurrence[state])
            else:
                # Record first time we see this state
                first_occurrence[state] = i
        
        return max_len
