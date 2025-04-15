class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def countingSort(arr):
            max_val = max(arr)
            count = [0] * (max_val + 1)

            while len(arr) > 0:
                num = arr.pop(0)
                count[num] += 1

            for i in range(len(count)):
                while count[i] > 0:
                    arr.append(i)
                    count[i] -= 1

            return arr
        sarr = countingSort(costs)
        r = 0
        for val in sarr:
            if coins - val >= 0:
                r += 1
                coins -= val
                continue
            return r
        return r
            

            

