
# Briefly describe the artifact. What is it? When was it created? 
The artifact is a C++ program chosen for a capstone project in computer science.  It reads a text file containing one word per line and provides a menu driven interface with four options.  1. Count occurrences of a user specified word (case-insensitive), 2, display all words and their frequencies, 3 display words with frequencies represented as asterisks, and 4, exit the program.  Enhancements include case insensitive word searching, input validation for words (letters only), and file error handling, all implemented using vectors and loops to match the original code's style.

# Justify the inclusion of the artifact in your ePortfolio. Why did you select this item? What specific components of the artifact showcase your skills and abilities in software development? How was the artifact improved? 
I selected the artifact for my ePortfolio because it represents a significant achievement from my capstone project in computer science, demonstrating my ability to develop a functional, user interactive C++ program that processes file input and provides meaningful output.  This artifact highlights my skills in file handling, user input validation, and program design, which are critical for software development.  Its menu driven interface and enhanced features make it a strong example of my ability to create robust, user friendly applications while adhering to a specific coding style.

# Specific Components Showcasing Skills and Abilities:
1. File I/O and Data Processing: The program reads a text file (CS210_Project_Three_Input_File.txt) and processes it to count word frequencies, stored in vectors.  This showcases my ability to handle file input/output operations and manipulate data structures effectively, as seen in the loops that parse the file and update word counts.
  
2. User Input Handling and Validation: The isValidWord function ensures that user inputs for word searches contain only letters, demonstrating my understanding of input validation to prevent errors.  The switchInput function and try-catch block handle menu inputs , reflecting my ability to manage user interactions and error conditions.
    
3. Case-Insensitive Search Implementation: The toLower function converts words to lowercase for comparison, ensuring that searches are not case sensitive.  This feature highlights my attention to user experience and my ability to implement practical enhancements using basic C++ string manipulation.
   
4. Structured Programming: The use of a switch statement for the menu and clear loop structures demonstrates my ability to write organized, efficient code that aligns with performance considerations, as noted in the original comment about switch statements being faster than if-else trees.
   
5. Error Handling: The file opening check with a clear error message showcases my ability to anticipate and handle potential runtime issues, ensuring the program is robust and user friendly. 

The artifact was enhanced from its original version to improve usability and readabiliyu while maintaining my original coding style.  These include:
1. Case Insensitive Search: Added the toLower function to make word searches case insensitive, improving user experience by treating variations like "Apple" and "apple" as the same word. 

2. Input Validation: Introduced the isValidWord function to validate word inputs for option 1, ensuring only alphabetic inputs are accepted, which prevents crashes or incorrect results from invalid inputs.
    
3. File Error Handling: Added a check for file opening failures at the start of main, providing a clear error message and program termination if the input file cannot be accessed, enhancing reliability.
    
4. Style Preservation: Ensured the enhancements used vectors and loops instead of advanced data structures like map, matching my original code’s simplicity and structure.

3 Did you meet the course outcomes you planned to meet with this enhancement in Module One? Do you have any updates to your outcome-coverage plans? 
No.  This is due to switching to a SNHU school project for the remainder of the course.

# Reflect on the process of enhancing and modifying the artifact. What did you learn as you were creating it and improving it? What challenges did you face? 
Adding case insensitive search with the toLower function taught me how small changes can significantly improve usability by matching words like "Apple" and "apple," while implementing input validation with isValidWord reinforced the importance of anticipating user errors to ensure robustness.  Enhancing file error handling deepened my understanding of reliable program design, and maintaining the original vector based style with loops taught me to adapt improvements to project constraints.  Challenges included preserving the original code’s simplicity, as using vectors instead of a more efficient map required careful design to maintain correctness, and ensuring consistent case insensitive logic across file reading and user input demanded thorough testing.  Designing effective input validation was also tricky.
