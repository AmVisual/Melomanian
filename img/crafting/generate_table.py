import os

PATH = "./creator_music_box/"

files = os.listdir(PATH)

file = open("table.txt", "w")

for f in files:
    item = f.split("_crafting")[0].replace('_', ' ').capitalize()
    print(item)
    file.write("   * - " + item + "\n")
    file.write("     - \n")
    file.write("        .. image:: ../../../img/crafting/creator_music_box/" + f + "\n")

file.close()