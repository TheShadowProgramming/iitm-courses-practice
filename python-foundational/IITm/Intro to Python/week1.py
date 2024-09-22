print("Running a google assistant chat greeting someone")
print("Hi Good Morning, Can I know your name?")
n = str(input())
# for giving input to the computer we use input function
# but we need to define which type of input are we giving
# and we do that by choosing b/w str, int, sometimes char
print("Nice to meet you", n, "!")
# by using commas in between qoutes we can print multiple things
print("So what's your age btw?")
p = float(input())

if p < 20:
    print("Wow!, you're a teenager")
elif (p > 20) and (p < 60):
    print("Wow!, you're an adult")
else:
    print("Wow!, you're an experienced person")
q = str(input("So where do you live? : "))
print('Good to know that you live in', q)

r = 0

while p < 60:
    p = p+1
    r = r+1

print("So you have", r, "years left to become an experienced person!, Nice!")

g = bool(input("So do you think, current government is compatible or not ? :"))
print(g)

h=bool(g)