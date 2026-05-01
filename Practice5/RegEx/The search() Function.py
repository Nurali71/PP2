# The search() function searches the string for a match, and returns a Match object if there is a match.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
