name1 = ["java", "C", "python"]
name2 = ["go", "web"]

# print((name1 + name2))
name2.append("a")
name2.extend(name1)
print("name1:%s" % name1)
print("name2:%s" % name2)
print("统计某个元素在列表中出现的次数：", end="")
print(name2.count("a"))
print("从列表中找出某个值第一个匹配项的索引位置，索引从0开始:", end="")
print(name2.index("a"))