# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        # We store the passed-in list as an attribute
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # We use a loop to iterate through the list attribute
        for line in self.lyrics:
            print(line)

# Step 2: Instantiate the object
stairway = Song([
    "leo ni leo asemaye kesho ni muongo", 
    "Manzi nipe mkono,tembea nami cheza nami", 
    "leo warudi nyumbani bila mkono"
])

# Step 3: Call the method
stairway.sing_me_a_song()