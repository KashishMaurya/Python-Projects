# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
    
    # to store only temp row :
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# convert csv to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# temp col to list 
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# avg of temp col
# temp_list_avg = sum(temp_list) / len(temp_list)
# print(int(temp_list_avg))

# avg of temp col using pandas
# print(data["temp"].mean())
# print(data["temp"].max())

# same
# print(data["condition"])
# print(data.condition)

# get data in row 
# print(data[data.temp])
# get data   max temp     ==  from temp col
# print(data[data.temp.max() == data["temp"]])


# monday = data[data.day == 'Monday']
# print(monday.condition)
# mondayF = monday.temp * 9/5 + 32
# print(monday.temp)
# print(mondayF)


# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")




# create squirel dataframe
data = pandas.read_csv("Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
print(gray)
black = len(data[data["Primary Fur Color"] == "Black"])
print(black)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon)


data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")