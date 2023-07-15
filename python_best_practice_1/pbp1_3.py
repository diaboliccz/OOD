print(" *** String count ***")
val = input("Enter message : ")
lower_count=0
upper_count=0
lower_list = []
upper_list = []
for i in val:
      if(i.islower()):
            lower_count+=1
            lower_list.append(i)
      elif(i.isupper()):
            upper_count+=1
            upper_list.append(i)

lower_list = set(lower_list)
upper_list = set(upper_list)
lower_list = sorted(lower_list)
upper_list = sorted(upper_list)
print('No. of Upper case characters : ' + str(upper_count))
print('Unique Upper case characters : ' + '  '.join(upper_list))
print('No. of Lower case Characters : ' + str(lower_count))
print('Unique Lower case characters : ' + '  '.join(lower_list))