MIT Muses Serenades Algorithm
written by Christina Warren


NOTES TO THE USER:

The main algorithm is in the file muses_serenades_algorithm.py. To use it, you don't need to read any of the code. Just run it on the command line and follow the instructions for user input. If you run into any errors, check below in the "USE AND POTENTIAL ERRORS" section. Please contact me with any questions/concerns - cewarren@mit.edu.

If all you want to do is use the algorithm, this is as far as you have to read.


NOTES TO THE DEVELOPER:

If you want to understand how the code works, or if you're trying to edit/improve it (it could definitely use it), the following are my notes on the algorithm.


USE AND POTENTIAL ERRORS:

Input Data Format

Missing Locations from Place_Dic
	If you get an error saying it could not find a value in "place_dic", likely you're missing a building location in "place_dic". To add correct coordinates, use the file mit_map.jpg. The coordinates correspond to the number of pixels measured from the top left corner to the building number.

Serenades Per Hour
	The current number of serenades per hour is 8. To change this, in Part 1, in the section initializing the time_dic, change the time_minutes to reflect the time slots for serenades each hour.

Lunch Constraint
	The current lunch constraint, implemented in the function check_lunch_constraint(), demands that the schedule have six consecutive free time slots (about 45 minutes) between 12:30 and 2:30. To change the total number of free time slots, change the maximum in the return statement. To change the earliest and latest bounds of the time slot, change the start and end variables.

Class Constraint
	Currently there are two different class constraint functions, check_class_constraint_singe() and check_class_constraint_double(). The single function is the ideal, where there are no two serenades scheduled for the same class. However, in the event that this proves impossible, you may need to change the constraint used. The double function allows multiple serenades to be scheduled in one class. To change to this, at the very end of Part 2, change the check_class_constraint alias to check_class_constraint_double.

Search Functions
	Several different search functions have been implemented in Part 3. They're called find_path_*(). They return a tuple with a list of paths (some are set to limit the number returned) and the total distance (in meaningless units). The algorithm currently uses the function find_path_dfs_random(), which performs the best. To change which function is used, change the line after the comment "# use one of the above functions". The following are explanations of each function.

	find_path_exaustive(): Finds all possible paths. To find the optimal path, you can then sort by path length. This function is good for testing on smaller data sets, but in general is incredibly slow and uselessly inefficient.

	find_path_bfs_bb(): Short for breadth first search, branch and bound. This is the only function that finds the optimal path. However, it's also uselessly inefficient. If you're looking to improve the code, getting this to work in a reasonable time might be your best bet.

	find_path_dfs(): Short for depth first search. This is generally the fastest function to return any path, but it makes no gaurentees about finding a good path. To change the number of paths returned, put a higher limit on the length of "final_schedules" in the while statement.

	find_path_random_old(): This is similar to the previous function, but introduces an element of randomness in extending paths that varies the schedules returned. Random paths will be returned, and the algorithm will select and return the shortest of those. To change the number of paths returned, put a higher limit on the length of "final_schedules" in the while statement OUTSIDE the helper() function.

	find_path_random(): This is a small improvement on the previous function (only one path is added to the queue after extension rather than all) that usually runs slightly faster. Adjust as with above function. This is the search function the algorithm currently uses.

Hardcoding Data Input
	Rather than use the input functionality, you may want to hardcode file and column names to avoid typing them in when running the code. When the program asks whether your data is loaded, rather than typing "y" or "n", type "admin." This will allow you to skip entering file names, and instead use the names coded in. The lines that you'll have to hard code are all in the User Input section, tagged with the comment "# hardcoded". (Note that you will still have to manually translate all the data from the spreadsheet - if you want to skip this as well, enter "y" at the beginning.)


POTENTIAL IMPROVEMENTS:

Input Data Format
	The data directly from the serenades questionnaire Google form is bad. Unusably bad. If you want to make life easier for future users, you might think about standardizing this data format and writing a parser to automate converting the data from the form output to something this program can use.

Improve BFS/BB
	As I wrote in the Search Functions section, the bfs_bb function is the only one that truly finds the optimal path, which is really the goal. Improving this function would do the most toward improving the overall functionality of the algorithm.

Constraint Propagation
	You might want to make more use of the strategy of constraint propagation in the search algorithm. For example, schedule a serenade if there's only one possible time left.

Post-Search Optimization
	In lieu of creating a search algorithm that finds an optimal path, you may want to try adjusting the path after you find one. For instance, strategically or randomly switching serenades time slots around to see if it improves the overall distance.