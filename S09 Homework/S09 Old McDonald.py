# OldMcDonald.py
# Singing OldMcDonald son for 5 different animals with their noises


# The verse that is repeated over and over in the song
def verse():
    print ("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


# Whole song, using animal and noise where needed
def sing(animal,noise):
    print()
    verse()
    print ("And on that farm he had a", animal, ", Ee-igh, Ee-igh, Oh!")
    print ("With a", noise, ",", noise, "here and a", noise, ",", noise, "there")
    print ("Here a", noise, "there a", noise, "everywhere a ", noise, ",", noise, " .")
    verse()


# Main function, invoking the same sing function bus using different parameters
def main():
    sing("cow", "moo")

    sing("horse", "neigh")

    sing("pig", "oink")

    sing("goat","baa")

    sing("hen", "cluck")


#Invoking main
main()
