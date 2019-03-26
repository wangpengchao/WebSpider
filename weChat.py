import itchat

# 登录网页版微信
itchat.login()
# 爬取自己好友的信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]
print(friends)

print(type(friends))


# 分析数据
male = 0
female = 0
other = 0

for i in friends[0:]:
    print(i)

for i in friends[0:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[0:])
print('男性好友：%.2f%%' % (male/total*100))
print('女性好友：%.2f%%' % (female/total*100))
print('不行性别好友：%.2f%%' % (other/total*100))


