def birthdayCakeCandles(candles):
    # Since it takes O(n) to find the max height, the worst case time complexity
    # should be O(n) for most efficient solution
    # i.e., a single pass solution
    counter = 0
    if len(candles) > 0:
        current_max = candles[0]
        for candle in candles:
            if candle > current_max:
                current_max = candle
                counter = 0
            if current_max == candle:
                counter += 1
    return counter

print(birthdayCakeCandles([4,4,1,3])) # Output = 2
# The tallest candles are 4. There are 2 candles with this height, so the function should return 2.
print(birthdayCakeCandles([1, 1, 1, 1])) # Output = 4
# All candles are the same height, so all are the tallest.
print(birthdayCakeCandles([])) # Output = 0
# No candles, so nothing to blow out.