def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

z = (permute_string('ABCDEF'));
redwins = []
bluewins = []
greenwins = []

for number in range(0,(len(z))):
  if (((z[number].find('A') < z[number].find('B')) or (z[number].find('A') < z[number].find('C'))) and ((z[number].find('A') < z[number].find('D')) or (z[number].find('A') < z[number].find('E')) or (z[number].find('A') < z[number].find('F')))):
    redwins.append(z[number])
  elif (((z[number].find('D') > z[number].find('B')) and z[number].find('D') > z[number].find('C')) or (z[number].find('E') > z[number].find('B') and z[number].find('E') > z[number].find('C')) or ((z[number].find('F') > z[number].find('B')) and (z[number].find('F') > z[number].find('C')))):
    bluewins.append(z[number])
  else:
    greenwins.append(z[number])
print (len(redwins))
print (len(bluewins))
print (len(greenwins))
