# model 模块
# mail 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码层级关系 通过 缩进来表示
# class 类 类型
# str string 字符
# 合法标识符（变更名 方法名）：必须以字母或者 _ 开头，剩下的可以是字母或数字，下划线，大小写敏感，不可用关键字做标识符
# Ctrl+alt+L格式化代码
# Ctrl+K conmit 代码
# Ctrl+alt+K  push 代码

# 声明一个int_demo 的方法
def int_demo():
    # 声明aint_demo 的变量， 并赋值 1
    aint = 1
    #打印 aint 的值
    print(aint)
    #打印 aint 的类型； type（aint）：获取aint的类型
    print(type(aint))

#声明一个 str_demo 的方法
def str_demo():
    # 声明astr 变量 ，并赋值  1
    astr = '1'
    #打印 astr 的值
    print(astr)
    # 打印 astr 的类型， type（astr): 获取astr 的类型
    print(type(astr))

# 演示字符串拼接 ： +
def str_demo():
    a='hello'
    b='world'
    return a+b

# 字符串拼接 ：%s
def str_demo2():
    a='hello'
    b= 250
    #print(a+str(b)
    print('a 是 ： %s;b 是 : %s'%(a,b))












