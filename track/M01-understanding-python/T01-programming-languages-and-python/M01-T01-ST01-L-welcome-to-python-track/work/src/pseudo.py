# To print Hello World 
# Start
#   print "Hello World"
# End

print("Hello World! \nThank you for learning python")
print("Hello World!", end=" ")
 print("Thank you for learning python")


# To find wheather number (n) is even or odd
# Start
# read n
#     if n % 2 = 0
#       print "Even"
#     else
#       print "odd"
#    End if
# End

n = 15
if n%2 ==0:
    print("Even")
else:
    print("Odd")


# To find the number is pos,neg or Zero
# Start
# read n
#   if n > 0
#     print "Positive"
#   else if n < 0
#     print "Negative"
#   else
#     print "Zero"
#   End if
# End

n = 10
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative ")
else:
    print("Zero")
    

# To find the largest number among  3 numbers (a,b,c)
# Start
# read a,b,c
#    if a > b AND  a > c
#        print "a is largest"
#    else if  b > a AND b > c
#        print "b is largest"
#    else
#        print "c is largest"
#    End if
# End

a= 10 ;b = 12 ;c = 44
if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")