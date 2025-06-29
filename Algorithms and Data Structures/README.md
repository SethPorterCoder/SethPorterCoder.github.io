# Briefly Describe the Artifact
The artifact is a python based checkers game AI,  implemented within the Checkers class using the graphics library.  It facilitates an interactive 8x8 checkers game supporting both singleplayer and multiplayer, but for this assignment, I will be focusing only on the singerplayer aspect of it.  The AI, primarily in the CompTurn method, employs a heuristic algorithm to select moves by prioritizing strategies such as back row defense, capturing opponent pieces, promoting pawns to kings, and ensuring move safety.  The game uses a 2D list of Tile objects to represent the board and includes features like saving loading game states and undoing moves.  Enhancements added boundary checks and an undo functionality to improve reliability and user experience, maintaining the original code’s structure.

# Justify the Inclusion of the Artifact in Your ePortfolio
The checkers AI was selected for my ePortfolio as it showcases my ability to optimize algorithms and data structures in a game based context.  The artifact demonstrates advanced algorithmic decision making and efficient data structure use, which is critical for software development. 

# The artifact was improved by:
1. Weighted Scoring System: Modified CompTurn to assign scores to moves based on strategic value (+10 for captures, +5 for king promotions, -5 for back row moves), selecting the highest scored move to enhance consistency, addressing previous issues with random selection’s inconsistency in complex scenarios. 

2. Boundary Checks: Added to SpecialPCCP to prevent index out of bounds errors, improving reliability. 

3. Undo Feature: Implemented via move_history, allowing move reversion to enhance user experience while maintaining the original code’s list-based structure. 

4. Style Preservation: Ensured enhancements used lists and loops, aligning with the original code’s simplicity and style. 
These improvements, demonstrate my ability to optimize algorithms for better performance, making the artifact a compelling addition to my ePortfolio.

# Did You Meet the Course Outcomes You Planned to Meet With This Enhancement in Module One?
The enhanced artifact meets Module One course outcomes for designing efficient algorithms and applying data structures to solve complex problems.  The weighted scoring system in CompTurn improves strategic decision making, achieving algorithm design goals, while the 2D list and move_history demonstrate effective data structure use.  The boundary checks and undo feature further align with outcomes by enhancing reliability and usability. 

# Reflect on the Process of Enhancing and Modifying the Artifact
Enhancing the checkers AI, particularly by reworking the algorithm to use a weighted scoring system, taught me the importance of balancing algorithmcomplexity with performance.  Assigning scores in CompTurn improved strategic consistency, reinforcing my understanding of heuristic optimization, while implementing boundary checks in SpecialPCCP highlighted the need for proper  handling.  The undo feature deepened my knowledge of deep copying for state preservation.  Debugging move logic was difficult due to checkers’ rules, but it enhanced my problem solving skills. 


