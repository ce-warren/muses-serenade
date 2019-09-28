# myfile = open("random.txt")
# filecontents = myfile.read()
# myfile = open("random.txt", "w")
# myfile.write(filecontents.replace("i", "I"))
# myfile.close()

file = open("form_responses.csv")
data = file.read()
out = open("serenades_data.csv")

data_ = data.split("\n")
data = []
for i in data_[3:]:
	row = i.split(",")
	print(row, "\n")
	if row[7] == "In-Person ($15)":
		data.append(row[10])

#print(data)

file.close()
out.close()