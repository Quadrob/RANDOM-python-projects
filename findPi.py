# My attempt at : 
#   Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
#   Keep a limit to how far the program will go.
#
# Robert Zeelie     created 12/09/19


#a generator function to calculate pi up to the decimal place specified by the user input
def pi_calculator(user_Input):
    
    """Generate user_Input digits of Pi."""
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while (user_Input >= 0):
        if ((4 * q + r - t) < (m * t)):
            yield m #returns value
            user_Input -= 1
            q, r, t, k, m, x = (10*q), (10*(r-m*t)), t, k, ((10*(3*q + r))//t-10*m), x
        else:
            q, r, t, k, m, x = (q*k), ((2*q+r)*x), (t*x), (k+1), ((q*(7*k+2)+r*x)//(t*x)), (x+2)

#main function which call the pi calculator and stores the genarator functions output and prints it
def main():
    
    user_Input = int(input("\nPlease enter an amout less than or equal to 10 000 of decimal places of pi youd like: "))
    if (user_Input > 10000 or user_Input < 1):
        print("\n\tRequest is invalid!\n")
    else:
        print("\nPi to " + str(user_Input) + " decimal places : \n")
        pi_array = []
        for i in pi_calculator(user_Input):
            pi_array.append(str(i))
        pi_array = (pi_array[:1] + ['.'] + pi_array[1:])
        output_String = ("".join(pi_array))
        print(output_String + "\n\n\tGoodbye\n")

#make sure this is run as main module
if __name__ == '__main__':
    main()






