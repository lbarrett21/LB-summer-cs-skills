def even_odd_counter(nums):
    even = 0
    for i in nums:
        if i%2 == 0:
            even += 1
    
    odd = len(nums) - even
    even = str(even)
    odd = str(odd)

    return ("There are " + even + " even numbers and " + odd + " odd numbers." )

print (even_odd_counter([1, 2, 3, 4, 5, 6]))