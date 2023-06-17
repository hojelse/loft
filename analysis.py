import json

data_file = open("data.txt", "r")
analysis_file = open("analysis.json", "w")

current_date = {}
current_date["day"] = 0
current_date["month"] = "month"
current_date["year"] = 0

data = []

while True:
  line = data_file.readline().strip()
  print(line)
  if not line:
    print("eof")
    break
  day,month,year = line.split()
  current_date["day"] = int(day)
  current_date["month"] = month
  current_date["year"] = int(year)

  while True:
    line = data_file.readline().strip()
    print(line)
    if not line:
      print("end of block")
      break

    exercise,weight,reps,rating = line.split()

    entry = {}
    entry["exercise"] = exercise
    entry["weight"] = float(weight)
    entry["reps"] = int(reps[:-1])
    entry["rating"] = int(rating)
    entry["date"] = current_date.copy()
    data.append(entry.copy())

data_file.close()

analysis_file.write(json.dumps(data))
