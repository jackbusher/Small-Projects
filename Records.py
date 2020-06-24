import numpy as np
choice = input("Do you want to add an album?(yes/no)")
arr2 = np.array(["Artist", "Album", "Format", "Genre"])
while choice == "yes":
    artist = input("Input artist")
    album = input("Input album name")
    format = input("Input format")
    genre = input("Input genre")
    newarr = np.array([artist, album, format, genre])
    arr2 = np.vstack(((arr2, newarr)))
    print("Your collection currently contains:")
    print(arr2)

    print("Do you want to add another record?")
    addAnother = input()
    if addAnother == "no":
        print("No problem. This is your finished collection")
        print(arr2)
        break


else:
    print("Ok")
