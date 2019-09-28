# This code is intended to find the optimal path for the MIT Muses to use for Valentines' Day Serenades.
# written by Christina Warren, 11.9.18

import random

# # # # # # # # # # # # # # # #
# User Input And Instructions #
# # # # # # # # # # # # # # # #

def get_time(inp):
	""" translate regular time format to the format required for the algorithm """
	parts = inp.split(":")
	if not len(parts) == 2:
		return inp
	dic = {"9":"09", "10":"10", "11":"11", "12":"12", "1":"13", "2":"14", "3":"15", "4":"16", "5":"17"}
	return dic[parts[0]] + parts[1]

print("\n\nThis code was written by Christina Warren and is intended to find an optimal path for the MIT Muses to use for Valentines' Day Serenades.")
inp = ""
while not inp == "y" and not inp == "n" and not inp == "admin":
	inp = input("Is your data already loaded in the correct format to serenades_data.csv? (y/n)\n")
skipped = []
if inp == "n" or inp=="admin":
	testing = False#test1
	if inp == "admin":#test1
		testing = True #test1
	print("\nThen I'll help you load the data. You'll only have to do this once, so if you run the algorithm again, skip this step.")
	print("Unfortunately, my creator didn't write a proper parser. So if you want this done automatically, standardize the data format for the serenades form.")
	print("For now, please download the serenades response form as a .csv file (make sure to remove extra commas), then put it in the same folder as this file.")
	if testing:
		inp = "form_responses.csv" # hardcoded
	else:
		inp = input("What's the name of the file?\n")
	while True:
		try:
			file = open(inp)
		except FileNotFoundError:
			print("\nI can't find that file. Re-enter the name or put the file in the correct location.")
			inp = input("What's the name of the file?\n")
			continue
		data = file.read()
		file.close()
		lists = data.split("\n")
		out = open("serenades_data.csv", "w")
		while True:
			if testing:
				des_col_name = "In-Person or Phone Serenade?" # hardcoded
			else:
				des_col_name = input("What is the heading text for the column that dictates what type of serenade this is? (ex. 'In person or phone serenade?)'\n")
			done = False
			for i in range(len(lists)):
				if des_col_name in lists[i].split(","):
					headings = lists[i].split(",")
					lists = lists[i+1:]
					done = True
					break
			if done:
				break
			print("\nThat's not an option. Here are some potential headings I can find:\n")
			for i in lists[:6]:
				for j in i.split(","):
					if not j == "":
						print(j)
			print("\n")
		des_col_ind = headings.index(des_col_name)

		while True:
			if testing:
				in_person_name = "In-Person ($15)" # hardcoded
			else:
				in_person_name = input("What is the designation in the column that it's an in person serenade? (ex. 'In person')\n")
			done = False
			for i in range(len(lists)):
				if in_person_name in lists[i].split(","):
					done = True
					break
			if done:
				break
			print("That's not an option. Here are the options I can find (if you don't see the correct input, maybe you entered an incorrect input for the previous question):")
			for i in lists[:15]:
				print(i.split(",")[des_col_ind])

		while True:
			if testing:
				loc_col_name = "What times and places work for this person on Wednesday 2/14?" # hardcoded
			else:
				loc_col_name = input("What is the heading text for the column that specifies the time and place of the serenade? (ex. 'What times/places work?')\n")
			if loc_col_name in headings:
				break
			print("That's not an option. Here are some potential headings I can find.")
			for i in headings:
				print(i)
		loc_col_ind = headings.index(loc_col_name)

		while True: #change1 whole loop
			if testing:
				name_col_name = "Recipient Name" # hardcoded
			else:
				name_col_name = input("What is the heading of the text for the column that speciefies who the serenade is for? (ex. 'Recipient name')\n")
			if name_col_name in headings:
				break
			print("That's not an option. Here are some potential headings I can find.")
			for i in headings:
				print(i)
		name_col_ind = headings.index(name_col_name)

		print("\nInstructions: You will be shown the options each person has selected as available for the serenade. Type the data in the specified format, and the program will write it to the file 'serenades_data.csv'. Remember, this is easier than manually scheduling.")
		print("Specified format: For each class the person is available: Specify the start and end times. Then specify the room. This must be a building number, then a dash, then a room number. If there's no room number, just put '-X'. Seperate these three values by spaces. If the person has specified multiple time slots, seperate them by commas (no spaces).\n")
		print("An example:\n\tGiven data: 9:30-11: 4-370; 1-2: Lobby 7\n\tWhat you should write: 9:30 11:00 4-370,1:00 2:00 7-X\n\nIf you get a flawed entry that you can't use, enter 'skip.' Now let's get started.")
		
		out_str = ""
		first = True
		for order in lists[22:]: #change1 testing (added indecies) #unchanged
			columns = order.split(",")
			if len(columns) > des_col_ind and len(columns) > loc_col_ind and len(columns) > name_col_ind:
				if columns[des_col_ind] == in_person_name:
					inp = input(columns[loc_col_ind] + "\n")
					if inp == "skip":
						skipped.append(columns)
						continue
					locations = inp.split(",")
					things = locations[0].split(" ")
					out_str = columns[name_col_ind] + "," + get_time(things[0]) + " - " + get_time(things[1]) + ": " + things[2] #change1
					for location in locations[1:]:
						things = location.split(" ")
						out_str = out_str + "," + get_time(things[0]) + " - " + get_time(things[1]) + ": " + things[2]
					if not first:
						out_str = "\n" + out_str
					first = False
					out.write(out_str)
		out.close()
		break
print("\nThe program will find as many paths as possible and return the shortest (written into a file called 'serenades_schedules.txt').")
print("It will keep a running count of how many paths it's found.")
print("Press 'Control C' at any time to stop the program and return the found paths. (Otherwise it will stop after 100.) For optimal results, let the program run to completion.")
print("Paths Found: ", 0)

# # # # # # # # # # # # # # # # # # #
# PART 1: Creating Data Structures  #
# # # # # # # # # # # # # # # # # # #

id_counter = 1

added_locations = {}

class Serenade(object):
	def __init__(self, places, n): #change1
		# places is list of tuples (time, room, classID)
		global id_counter
		self.ID = id_counter
		id_counter += 1
		self.name = n #change1

		self.possible_times_dic = {}
		for place in places:
			self.possible_times_dic[place[0]] = (place[1], place[2])

		self.time_assignment = None

	def get_location_coords(self, time):
		""" returns the coordinates of the location of a serenade given a specific time """
		try:
			return place_dic[self.possible_times_dic[time][0][:self.possible_times_dic[time][0].index('-')]]
		except KeyError:
			print("I don't know the location " + self.possible_times_dic[time][0] + ". Please find its coordinates using the instructions in the README (under the heading 'Missing Locations from Place_Dic').")
			inp = input("What is it's location? Format: x,y\n")
			coords = inp.split(",")
			added_locations[self.possible_times_dic[time][0][:self.possible_times_dic[time][0].index('-')]] = (int(coords[0]), int(coords[1]))
			place_dic[self.possible_times_dic[time][0][:self.possible_times_dic[time][0].index('-')]] = (int(coords[0]), int(coords[1]))
			return (int(coords[0]), int(coords[1]))

	def get_str(self, time):
		return time[:2] + ":" + time[2:] + "\t" + str(self.ID) + "\t" + self.possible_times_dic[time][0]

	def __str__(self):
		return str(self.possible_times_dic)

# maps each building to coordinates - from pixel coordinates of mit_map.jpg
place_dic = {'1':(466,432), '2':(590,393), '3':(474,386), '4':(540,353), '6':(565,345), '7':(441,369), '9':(419,332), '10':(492,335), '14N':(616,357),
	'16':(560,289), '24':(492,277), '26':(530,261), '32':(559,215), '34':(495,245), '36':(509,225), '37':(436,273), '38':(477,250), '46':(507,169),
	'50':(665,356), '54':(619,296), '56':(593,272), '66':(629,259), 'E15':(698,263), 'E25':(728,212), 'E51':(849,281), 'E52':(876,269)}

time_hours = ["09", "10", "11", "12", "13", "14", "15", "16", "17"]
time_minutes = ["05", "12", "19", "26", "32", "39", "46", "53"]
time_dic = {} # maps times to schedule indecies
reverse_time_dic = {} # maps schedule indecies to times
count = 0
for hour in time_hours:
	for minute in time_minutes:
		time_dic[hour + minute] = count
		reverse_time_dic[count] = hour + minute
		count += 1

def time_row():
	new = []
	for hour in time_hours:
		for minute in time_minutes:
			new.append(hour + minute)
	return new

class_dic = {} # maps class time/location to IDs to track duplicate classes
classID_count_dic = {}
classID_count = 0

serenade_list = []
serenade_dic = {} # maps IDs to corrisponding Serenade objects

# create Serenade objects
file = open('serenades_data.csv')
data = file.read()
file.close()
lists = data.split("\n")
for i in lists[:]: # adjust number of serenades used (for testing)
	tup_list = []
	if len(i.split(",")) < 1:
		continue
	for item in i.split(",")[1:]: #change1
		if item in class_dic:
			classID = class_dic[item]
		else:
			classID = classID_count
			class_dic[item] = classID
			classID_count += 1
		for time in time_dic:
			if int(item[:4]) <= int(time) <= int(item[6:11]):
				tup_list.append((time, item[13:], classID))
	serenade_list.append(Serenade(tup_list, i.split(",")[0])) #change1

for i in serenade_list:
	serenade_dic[i.ID] = i

# in the schedule:
# _ means cannot be this time
# O means could possibly be this time
# X means scheduled at this time

schedule = {}
for serenade in serenade_list:
	schedule[serenade.ID] = []
	for i in time_row():
		if i in serenade.possible_times_dic:
			schedule[serenade.ID].append("O")
		else:
			schedule[serenade.ID].append("_")

def print_schedule(schedule):
	""" returns a printable (string) visualization of the schedule """
	s = ""
	for k, v in schedule.items():
		s += str(k)
		s += "\t"
		for i in v:
			s += i
		s += "\n"
	return s

# # # # # # # # # # # # # # # # # # # # # # #
# PART 2: Constraints and Helper Functions  #
# # # # # # # # # # # # # # # # # # # # # # #

def find_all_unscheduled(schedule):
	""" returns a list of all unscheduled serenades, sorted by most constrainted """
	unscheduled = []
	for ID, serenade in schedule.items():
		if not "X" in serenade:
			unscheduled.append((ID, serenade))
	return sorted(unscheduled, key = lambda tup: tup[1].count('O'))

def schedule_serenade(schedule, ID, serenade, time):
	""" schedules a serenade at a certain time, creating and returning a new schedule (original unmodified) """
	if not serenade[time] == "O":
		raise ValueError("incorrect input for schedule_serenade()")
	new_serenade = []
	for i in range(len(serenade)):
		if i == time:
			new_serenade.append("X")
		else:
			new_serenade.append("_")
	new_schedule = {}
	for i in schedule:
		if i == ID:
			new_schedule[i] = new_serenade
		else:
			other_serenade = []
			for j in range(len(schedule[i])):
				if j == time:
					other_serenade.append("_")
				else:
					other_serenade.append(schedule[i][j])
			new_schedule[i] = other_serenade
	return new_schedule

def distance_between(seren1, seren2, schedule):
	""" return the distance between two serenades in a given schedule (only usable on scheduled serenades) """
	coords1 = seren1.get_location_coords(reverse_time_dic[schedule[seren1.ID].index("X")])
	coords2 = seren2.get_location_coords(reverse_time_dic[schedule[seren2.ID].index("X")])
	return ((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)**0.5

def total_len(schedule):
	""" returns the total path walking length through the schedule """
	total = 0
	schedule_list = []
	for k, v in schedule.items():
		schedule_list.append((k,v))
	for i in range(len(schedule_list)-1):
		total += distance_between(serenade_dic[schedule_list[i][0]], serenade_dic[schedule_list[i+1][0]], schedule)
	return total

def partial_len(schedule):
	""" returns the average path walking length of a partially made schedule """
	partial_schedule = {}
	for k, v in schedule.items():
		if "X" in v:
			partial_schedule[k] = v
	try:
		return total_len(partial_schedule)/(len(partial_schedule)-1) # last part makes it return ave. distance between classes (instead of total distance)
	except ZeroDivisionError:
		return 0

def check_validity(schedule):
	""" returns false if any serenade is impossible to schedule """
	for serenade in schedule.values():
		if not "O" in serenade and not "X" in serenade:
			return False
	return True

def check_lunch_constraint(schedule):
	""" checks whether a schedule has sufficient time alloted for lunch (6 consecutive slots between 12:30 and 2:35) """
	count = 0
	max_count = 0
	start = '1230'
	end = '1435'
	times = []
	for i in time_row():
		if int(start) <= int(i) <= int(end):
			times.append(i)
	for time in times:
		for serenade in schedule.values():
			if serenade[time_dic[time]] == 'X':
				max_count = max(max_count, count)
				count = 0
				break
		count += 1
	return max(max_count, count) >= 6

def check_class_constraint_single(schedule):
	""" checks whether a schedule has two serenades scheduled for the same class """
	classes = []
	for i in schedule.keys():
		if "X" in schedule[i]:
			time = reverse_time_dic[schedule[serenade_dic[i].ID].index("X")]
			class_ID = serenade_dic[i].possible_times_dic[time][1]
			if class_ID in classes:
				return False
			classes.append(class_ID)
	return True

def check_class_constraint_double(schedule):
	""" checks whether a schedule has more than two serenades scheduled for the same class """
	classes = []
	double_classes = [] # sketchy (allowing double-classes)
	for i in schedule.keys():
		if "X" in schedule[i]:
			time = reverse_time_dic[schedule[serenade_dic[i].ID].index("X")]
			class_ID = serenade_dic[i].possible_times_dic[time][1]
			if class_ID in double_classes: # sketchy
				return False # sketchy
			elif class_ID in classes:
				double_classes.append(class_ID) # sketchy
				#return False # sketchy
			classes.append(class_ID)
	return True

check_class_constraint = check_class_constraint_double

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PART 3: Scheduling with Search Tree and Constraint Propagation  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def find_path_exaustive(schedule):
	""" returns all possible paths """
	final_schedules = []
	queue = [schedule]
	while not queue == []:
		sched = queue.pop(0)
		unscheduled = find_all_unscheduled(sched)
		if unscheduled == []:
			final_schedules.append((sched, total_len(sched)))
			continue
		for ID, serenade in unscheduled:
			for time in range(len(serenade)):
				if serenade[time] == "O":
					new_sched = schedule_serenade(sched, ID, serenade, time)
					if check_validity(new_sched) and check_lunch_constraint(new_sched) and check_class_constraint(new_sched):
						queue.append(new_sched)
	return final_schedules

def find_path_bfs_bb(schedule):
	""" returns shortest path """
	final_schedules = []
	queue = [schedule]
	while len(final_schedules) < 1:
		queue.sort(key = lambda schedule: partial_len(schedule))
		sched = queue.pop(0)
		unscheduled = find_all_unscheduled(sched)
		if unscheduled == []:
			final_schedules.append((sched, total_len(sched)))
			continue
		for ID, serenade in unscheduled:
			for time in range(len(serenade)):
				if serenade[time] == "O":
					new_sched = schedule_serenade(sched, ID, serenade, time)
					if check_validity(new_sched) and check_lunch_constraint(new_sched) and check_class_constraint(new_sched):
						queue.append(new_sched)
	return final_schedules

def find_path_dfs(schedule):
	""" returns a path """
	final_schedules = []
	queue = [schedule]
	while len(final_schedules) < 1:
		sched = queue.pop(-1)
		unscheduled = find_all_unscheduled(sched)
		if unscheduled == []:
			final_schedules.append((sched, total_len(sched)))
			continue
		(ID, serenade) = unscheduled[0]
		for time in range(len(serenade)):
			if serenade[time] == "O":
				new_sched = schedule_serenade(sched, ID, serenade, time)
				if check_validity(new_sched) and check_lunch_constraint(new_sched) and check_class_constraint(new_sched):
					queue.append(new_sched)
	return final_schedules

def find_path_random_old(schedule):
	""" returns a random path, with a limit on timesteps """
	def helper(schedule):
		queue = [schedule]
		count = 0
		while count < 100:
			count += 1
			sched = queue.pop(-1)
			unscheduled = find_all_unscheduled(sched)
			if unscheduled == []:
				return [(sched, total_len(sched))]
			(ID, serenade) = random.choice(unscheduled)
			for time in range(len(serenade)):
				if serenade[time] == "O":
					new_sched = schedule_serenade(sched, ID, serenade, time)
					if check_validity(new_sched) and check_lunch_constraint(new_sched) and check_class_constraint(new_sched):
						queue.append(new_sched)
		return []
	final_schedules = []
	while len(final_schedules) < 1:
		try:
			new = helper(schedule)
			final_schedules.extend(new)
			if not new == []:
				print('Paths Found: ', len(final_schedules))
		except KeyboardInterrupt:
			break
	return final_schedules

def find_path_random(schedule):
	""" returns a random path, with a limit on timesteps """
	def helper(schedule):
		queue = [schedule]
		count = 0
		while count < 100:
			count += 1
			try:
				sched = queue.pop(-1)
			except IndexError:
				return []
			#print(print_schedule(sched))
			unscheduled = find_all_unscheduled(sched)
			if unscheduled == []:
				return [(sched, total_len(sched))]
			(ID, serenade) = random.choice(unscheduled)
			possible_times = []
			for i in range(len(serenade)):
				if serenade[i]=='O':
					possible_times.append(i)
			while not possible_times == []:
				time = random.choice(possible_times)
				possible_times.pop(possible_times.index(time))
				new_sched = schedule_serenade(sched, ID, serenade, time)
				if check_validity(new_sched) and check_lunch_constraint(new_sched) and check_class_constraint(new_sched):
					queue.append(new_sched)
					break
			if len(queue) < 3:
				while not possible_times == []:
					time = random.choice(possible_times)
					possible_times.pop(possible_times.index(time))
					new_sched = schedule_serenade(sched, ID, serenade, time)
					if check_validity(new_sched) and check_lunch_constraint(new_sched) and check_class_constraint(new_sched):
						queue.append(new_sched)
						break
		return []
	final_schedules = []
	while len(final_schedules) < 100:
		try:
			new = helper(schedule)
			final_schedules.extend(new)
			if not new == []:
				print("Paths Found: ", len(final_schedules))
		except KeyboardInterrupt:
			break
	return final_schedules

# use one of the above functions
final_schedules = find_path_random(schedule)

try:
	out = open("serenades_schedules.txt", "w")
	final_schedules.sort(key = lambda serenade: serenade[1])
	schedule = final_schedules[0]
	print("\n")
	print(print_schedule(schedule[0]))
	for time in time_dic:
		for ID, serenade in schedule[0].items():
			if serenade.index("X") == time_dic[time]:
				out.write(serenade_dic[ID].get_str(time) + "\t" + serenade_dic[ID].name + "\n")
				break
	out.write("Total Distance: " + str(schedule[1]) + "\n")
except IndexError:
	print("\nNo paths found.")
out.close()

if not skipped == []:
	print("Skipped serenades:")
	for i in skipped:
		print(i)
if not added_locations == {}:
	print("Added locations (please add to place_dic in the code if you're running it again):")
	for k,v in added_locations.items():
		print(k + ": "+ str(v))