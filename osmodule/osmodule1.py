import os

# here we check that data folden already exists or not :
# if(not (os.path.exists("data"))):
# mkdir: take the path and used to create a folder or directory:
    # os.mkdir("data")
    # for i in range(1,101):
    #     os.mkdir(F'data/day {i}')
#  this will rename all days folder to tutorials
# for i in range(1,101):
#     os.renames(F'data/day {i}',f"data/tutorial {i}")
# this will give a list of names of all folders present in data folder
# this will return all foldern which have inside folder
# folders=os.listdir("data")
# print("Number of Folders in Data",folders)
# for folder in folders:
#     print(folder , os.listdir(f"data/{folder}"))

print(os.getcwd())


