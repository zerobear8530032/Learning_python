import datetime
print(datetime.datetime.now().strftime('%H:%M:%S'))
hours=int(datetime.datetime.now().strftime('%H'))


if(hours>6 and hours<=12):
    print("good morning")
elif(hours>12 and hours<=18):
    print("good afternoon")
elif(hours>18 and hours<=22):
    print("good evening")
else:
    print("good Night")