#  Using input function ask user to enter a song name.
# 1. Print the first charachter of given song name.
# 2. Print the last charachter of given song name.
# 3. Print the length of the given song name.
# 4. Print the index number of "k" in this song name. 
# 5. Print the charachter from an index number of 3.
# 6. Print the song name in upper case.
# 7. Print the song name in lower case.
# Example: 
# Input: Mockingbird
# Output:
# M
# d
# 10
# 3
# k
# MOCKINGBIRD
# mockingbird


print("Enter your song name")
s =input()
print(s[:1])
print(s[-1])
print(len(s))
print(s.find ("k"))
print(s[3:4])
print(s.upper())
print(s.lower())

# Yusuf Solution

print("Enter your song name")
song_name = input()
print(song_name[0])
print(song_name[-1])
print(song_name[len(song_name)-1])
print(len(song_name))
print(song_name.find("k"))
print(song_name[3])
print(song_name.upper())
print(song_name.lower())
