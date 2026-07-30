class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        slots = len(nums)
        buckets = [[] for _ in range(slots + 1)]

        counters = collections.Counter(nums)
        print(counters.items())
        
        for value, frequency in counters.items():
            buckets[frequency].append(value)
        print(buckets)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    print(result)
                    return result

