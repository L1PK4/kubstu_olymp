op_set = {'[', '{'}
cl_set = {'}', ']'}
# def count_openclose(s):
	# return (s.count('[') - s.count('\\[') + s.count('{') - s.count('\\{'), s.count(']') + s.count('}'))
#definatly bad code, I won't recomend to read it
s = ''
opens, closes = 0, 0
while True:
	temp = input()
	o, c = count_openclose(temp)
	opens += o
	closes += c
	s = s + temp
	if opens == closes:
		break
level = 0
in_str_one = False
in_str_two = False
passing = False
mlvl = -1
for i in s:
	if i == "\\":
		passing = True
		continue
	if passing:
		passing = False
		continue
	if i == '"' :
		in_str_one = not in_str_one
	
	if i == "'" :
		in_str_two = not in_str_two
	if in_str_one or in_str_two:
		continue
	if i in op_set:
		level += 1
	elif i in cl_set:
		level -= 1
	if level > mlvl:
		mlvl = level
print(mlvl)