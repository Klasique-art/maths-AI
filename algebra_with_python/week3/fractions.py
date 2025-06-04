# convert decimal to integer

# get the decimal input from user
digits = input("Enter a decimal number: ")

# count how many decimal places (subtract 1 cos the . will be counted as char)
exp = len(digits) - 1 # exponent

# convert input to float
n = float(digits)

# exponent to get numerator
num = int(n * 10**exp)

# exponent to get denominator
deno = 10**exp

# percent - 1st 2 decimal places
percent = n * 100

# output
print("The decimal is", n)
print("The fraction is", num, "/", deno)
print("Percent is", percent, "%")