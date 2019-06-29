# # 编程打印互粉关系
# data = ['章子怡','黄晓明','张震','王力宏']
#
# for i in data:
#     for k in data:
#         if i != k:
#             print(i+"和"+k+'是互粉关系')

# # 批量处理商品价格
# data = [120, 90, 150, 200, 80]
# data_new=[]
# for i in data:
#     if i < 100:
#         i=i*0.9
#         data_new .append(i)
#     else:
#         i=i*0.8
#         data_new.append(i)
# for a in data_new:
#         print(a)

# 这段代码无法正常在线运行，因为包含 input() ，在线环境不支持，请到本地环境运行这段代码
# 编程判断一个人是否是微博活跃用户
# x = int(input("最近三天登录次数是？"))
# y = int(input("最近三天发微博数是？"))

# X > 20或者Y > 10 ---> 非常活跃用户
# 10 <= X < 20或者5 <= Y < 10 ---> 活跃用户
# X < 3 并且 Y <= 1 ---> 消极用户
# 其他 ---> 普通用户

# # 判断是否是非常活跃用户
# if x>20 or y>10:
#     print('非常活跃用户')
# # 判断是否是活跃用户
# if 10 <= x < 20 or 5 <= y < 10:
#     print('活跃用户')
# # 判断是否是消极用户
# if x < 3 and y <= 1:
#     print('消极用户')
# # 判断是否是普通用户
# else:
#     print('普通用户')

# # 编程判断是否含有Trump这个词
# string = "The high-profile engagement between Chinese President Xi Jinping and his U.S. counterpart Donald Trump on Thursday has caught the spotlight globally. Experts said their meeting has borne remarkable fruit, and the forward-looking attitude of the two heads of state towards bilateral cooperation will bring benefits to the two countries, the Asia-Pacific and the world at large."
# if 'Trump' in string:
#     print('This article maybe about Trump.')
# else:
#     print("This article maybe not about Trump.")

# # 这段代码无法正常在线运行，因为包含 input() ，在线环境不支持，请到本地环境运行这段代码
# # 编程判断某演员是否出演了某电影
# data = {
#   '芳华' : ['黄轩','苗苗'],
#   '战狼2' : ['吴京','吴刚','卢婧姗'],
#   '无问西东' : ['章子怡','黄晓明','张震','王力宏'],
#   '大兵小将' : ['成龙', '王力宏', '刘承俊']
# }
# name=input("请输入演员名字：")
# for movie in data:
#     actors = data[movie]
#     if name in actors:
#         print(name + "出演了电影" + movie )

# 编程判断年终考勤是否合格
# data = [21, 22, 22, 20, 23, 19, 20, 21, 23, 20, 22, 20]
# for i in data:
#     if i < 20:
#         print("年终考勤不合格")

# # 编程判断年终考勤是否合格
# data = [21, 22, 22, 20, 23, 19, 20, 21, 23, 20, 22, 20]
# NotPassDay=[]
# for i in data:
#     if i < 20:
#         NotPassDay.append(i)
# if NotPassDay:
#     print("年终考勤不合格")
# else:
#     print("年终考勤合格")


