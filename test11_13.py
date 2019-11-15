'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
'''
# ->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型，从而方便开发人员使用。

def addTwoNumbers( l1, l2):
    carryNum = 0 
    l3 = []
    print(l1)
    print(l2)
    while( len(l1) > len(l2) ):
        l2.append(0)
    while(len(l2) > len(l1)):
        l1.append(0)
    for i in range( len(l1) ):
        if l1[i] + l2[i] + carryNum >= 10:
            l3.append  ( (l1[i] + l2[i] + carryNum) % 10 )
            carryNum = 1
        else:
            l3.append( (l1[i] + l2[i] + carryNum) )
            carryNum = 0
    return l3

def main():
    l1 = [2,4,3]
    l2 = [5,6,4]
    l3 = addTwoNumbers(l1,l2)
    print(l3)
if __name__ == '__main__':
    main()
    print('over')

