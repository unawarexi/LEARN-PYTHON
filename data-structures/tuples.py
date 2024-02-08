filename = "Downloads/music/swift.mp3"

# this isn't dynamic
print(filename.split(".")[0].split("/")[2]) 

#this is dynamic
print(filename.split("/")[-1].split(".")[0])