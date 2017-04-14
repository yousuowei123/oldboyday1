# Author:ctwo b
# user logining

# 把用户和密码放到字典结构中
user_file = open("e://oldboyhomework//day1//userlist.txt", 'rb')

user_file.readline()
users_dict = {}
lines = user_file.readlines()

for line in lines:
    elements = line.split()
    users_dict[str(elements[0].decode('gbk'))] = str(elements[1].decode('gbk'))

# 黑名单
blacklist_dict = {}
count = 0
while count < 3:
    global username
    global password

    username = input('please input username:')
    password = input('please input password:')

    if username in users_dict and users_dict.get(username) == password:
        print('welcome logining')
        break
    else:
        print('input error, please input again:')
    count += 1

else:
    blacklist_dict[username] = password
    print('your name in add to blacklist')

# 存储黑名单
with open('e://oldboyhomework//day1//blacklist.txt', 'w') as f:
    for each in blacklist_dict:
        f.write('用户名' + '\t' + '用户密码' + '\n')
        f.write(str(each) + '\t' + str(blacklist_dict[each]) + '\n')

user_file.close()