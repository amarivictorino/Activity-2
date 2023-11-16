def print_ascii_title():
    title_art = """
       *****    **              ***     ***               
  ******  *  **** *            ***     ***              
 **   *  *   *****              **      **              
*    *  *    * *                **      **              
    *  *     *                  **      **       ****   
   ** **     *         ***      **      **      * ***  *
   ** **     *        * ***     **      **     *   **** 
   ** ********       *   ***    **      **    **    **  
   ** **     *      **    ***   **      **    **    **  
   ** **     **     ********    **      **    **    **  
   *  **     **     *******     **      **    **    **  
      *       **    **          **      **    **    **  
  ****        **    ****    *   **      **     ******   
 *  *****      **    *******    *** *   *** *   ****    
*     **              *****      ***     ***            
*                                                       
 **                                                                   
    """
    print(title_art)

# Call the function before getting user input
print_ascii_title()

# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

# Display the inputted data
print('\033[0m', "------------------------")
print('\033[92m', "\nUser Information:")
print("Name: ", name)
print("Age: ", age)
print("Address: ", address)
print('\033[0m', "------------------------")

