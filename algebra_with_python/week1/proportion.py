# setup a proportion:
# n1/d1 = n2/d2

# using cross multiplication, we put 0 for unknown value
n1 = 1
d1 = 2
n2 = 0 # 0 for unknown value
d2 = 16

# if we're solving for n2 (n2 is unknown) then the formula will be
if n2 == 0:
    answer = (n1 * d2) / d1 
    # print("n2 = ", answer)

# if we're solving for d2 (d2 is unknown) then the formula will be
if d2 == 0:
    answer = (d1 * n2) / n1
    # print("d2 = ", answer)
