# Function: Convert a Decimal number to a Binary string
def decimal_to_binary(decimal_num):
    # Special case: if the number is 0, return "0" immediately
    if decimal_num == 0:
        return "0"
        
    # Initialize an empty string to store binary digits
    binary_str = ""
    
    # Loop until the decimal number becomes 0
    while decimal_num > 0:
        # Get the remainder when dividing by 2 (either 0 or 1)
        remain = decimal_num % 2
        
        # Prepend the new remainder to the front of the result string
        binary_str = str(remain) + binary_str 
        
        # Perform integer division by 2 to prepare for the next iteration
        decimal_num = decimal_num // 2 
        
    # Return the final binary representation
    return binary_str


# Function: Convert a Binary string to a Decimal number
def binary_to_decimal(binary_str):
    # Initialize the decimal result to 0
    decimal_num = 0
    # Start with a place value of 1 for the rightmost bit (2^0 = 1)
    place_value = 1  
    
    # Start from the last character (rightmost bit) of the string
    index = len(binary_str) - 1
    
    # Traverse backwards from right to left
    while index >= 0:
        # Get the bit character at the current index ('0' or '1')
        bit = binary_str[index]
        
        # If the bit is '1', add the current place value to the decimal total
        if bit == "1":
            decimal_num = decimal_num + place_value
            
        # Double the place value for the next bit to the left (powers of 2: 1, 2, 4, 8, ...)
        place_value = place_value * 2 
        
        # Decrement the index to move to the next bit on the left
        index = index - 1
        
    # Return the accumulated decimal value
    return decimal_num


# Test: Decimal to Binary conversion
print("--- DECIMAL TO BINARY ---")
# Prompt user to enter a number and convert the input to an integer
number_to_convert = int(input("Enter the number: "))
# Call the function to convert the input to binary
bin_result = decimal_to_binary(number_to_convert)
# Print the conversion result
print("Number", number_to_convert, "to binary:", bin_result)

# Test: Binary to Decimal conversion
print("\n--- BINARY TO DECIMAL ---")
# Prompt user to enter a binary string
binary_string_to_convert = input("Enter the binary string: ")
# Call the function to convert the binary string to decimal
dec_result = binary_to_decimal(binary_string_to_convert)
# Print the conversion result
print("Binary string", binary_string_to_convert, "to decimal:", dec_result)
