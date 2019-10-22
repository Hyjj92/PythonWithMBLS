30、不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明。
31、使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，
	可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
	我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算，详见5）
32、字符串函数介绍
	str.lower()，str.upper()   将一个字符串中的字母变成全部小写  或者  全部大写
	str.split(sep)  返回一个列表  eg："A,B,C".split(,)  结果为 [ 'A'，'B' ，'C' ]
	str.count(sub)  返回字串sub在str中出现的次数
	str.replace(old，new)  将str中的 全部 old替换为 new
	str.strip(chars)  去除掉str左右两边的chars中列出的字符
	str.join(iter)  在iter字符串中每个元素中间加入 str  eg："，".join("123")  结果为1，2，3
	str(s) 将s变成字符串
	hex(x)  将整数x变成16进制小写字符串
	oct(x)  将整数x变成8进制小写字符串
	chr（U）返回U的Unicode对应的字符     
	ord(s) 返回s对应的Unicode编码    使用Unicode16
33、字符串格式化使用 槽 和 fomat方法
	Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母f，我们可以使用下面的语法糖来简化代码。
	正常方式：a, b = 5, 10   
		print('{0} * {1} = {2}'.format(a, b, a * b))
	简化方式：a, b = 5, 10
		print(f'{a} * {b} = {a * b}')


34、列表（list），是值的有序序列，每个值都可以通过索引进行标识，定义列表可以将列表的元素放在[]中，多个元素用,进行分隔。
35、列表的遍历
	可以使用for循环对列表元素进行遍历，也可以使用[]或[:]运算符取出列表中的一个或多个元素。
	① 通过循环用下标遍历列表元素： for index in range(len(list1)): 
					print(list1[index])
	② 通过for循环遍历列表元素： for elem in list1:
				print(elem)
	③ 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值：for index, elem in enumerate(list1):
								print(index, elem)
36、增删改查：  list1 = [1, 3, 5, 7, 100]
	添加元素：list1.append(200) 或者 list1.insert(1, 400)  #[1, 400, 3, 5, 7, 100, 200]
	删除元素：if 3 in list1:
		    list1.remove(3)
	       或者从指定位置删除：list1.pop(0)
	清空列表元素：list1.clear()
37、列表的切片操作：	fruits = ['grape', 'apple', 'strawberry', 'waxberry']		fruits += ['pitaya', 'pear', 'mango']
	列表切片：fruits2 = fruits[1:4]		# apple strawberry waxberry
	通过完整切片操作来复制列表：fruits3 = fruits[:]	# ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
	通过反向切片操作来获得倒转后的列表的拷贝：fruits5 = fruits[::-1]	# ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
38、列表的排序
	list2 = sorted(list1)		sorted函数返回列表排序后的拷贝不会修改传入的列表
	list3 = sorted(list1, reverse=True)	按字典逆序排列
	list4 = sorted(list1, key=len)		通过key关键字参数指定，根据字符串长度进行排序
	list1.sort(reverse=True)		直接在列表对象上进行排序