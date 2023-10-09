"""Write a program that asks a fisher the length of a zander in centimeters.
If the zander does not fulfill the size limit, the program instructs
to release the fish back into the lake and notifies the user of how many centimeters below the size limit
the caught fish was.
A zander must be 42 centimeters or longer to meet the size limit."""
length = float(input('Size of the zander: '))
if(length < 42):
    print(f'Release!!! {42-length:.2f} cm below the limit')
else:
    print(f'Winner Winner !! Zander dinner')
