str1 = "134613461"

sum = str1.count('1')  # str.count(sub, start= 0,end=len(string))
print(sum)

# capitalize:将字符串的第一个字符转换为大写(同title()方法)
str2 = "adafrgrad"
print(str2.capitalize())
print(str2.title())

# center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
str3 = "zhong"
print(str3.center(30, '*'))

# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str4 = "fsgrtehewgwT"

print(str4.find('gw'))
print(str4.replace('g', 'x', 1))  # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
str5 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str5.split())  # 以空格为分隔符，包含 \n
print(str5.split(' ', 1))  # 以空格为分隔符，分隔成两个

str1 = "this is string example....wow!!!";
str2 = "exam";

print(str1.index(str2));
print(str1.index(str2, 10));
print(str1.index(str2, 40));
