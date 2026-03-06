# The sub() function replaces the matches with the text of your choice:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)