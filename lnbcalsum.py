#15. Adding numbers
# ● Write code to take inline input from user
# ● Max 5 numeric input need to be selected
# ● If inline inputs are not having 5 numeric then throw error and ask to rerun
# code
# ● Arrange numbers in decreasing order and calculate sum of numbers
# ● If sum is less than 5 then reask for all inputs
# ● Filename must be lnbcalsum.py

x = list(map(int, input("Enter inline input: ").split()))
try:
    assert (len(x) >= 5),"Inline input is less than 5, please rerun the code."
    sum = 0
    x.sort(reverse=True)
    for num in x:
        sum += num
    
    assert (sum >= 5), "Sum is less than 5, please re enter all the numbers."
    print("Sum: ", sum)
except Exception as e:
    print(e)
