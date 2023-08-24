# your code goes here!
class Anagram:
    #Initailize the class with a character sequence
    def __init__(self, character):
        self._character = character

#Method match to find anagrams in a list of characters
    def match(self, char_list):
        #converts the initialized sequence into a list of characters
        char = [characters for characters in self._character]
        #Initialize an empty list that will store the matching characters
        match_char = []
        #Loop through each character in the list
        for character in char_list:
            #Convert the current character from the list into a list of characters
            chars  = [characters for characters in character]
            #Check if the sorted characters of the current list match the sorted characters of the initialized character
            match = sorted(chars) == sorted(char)
            #If there is a match add the current character to the list of matching characters
            if match:
                match_char.append(character)
        return (match_char)