import numpy as np

a = [[1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18],
     [19,20,21,22,23,24]]
b = np.array(a)
c = np.array([1,2,3,4,5,6,7,8,9,10])

# 연습) 배열중에 9, 12, 14, 17, 20, 22, 23이 있는 요소의 arrayindex를 만들고 fancy indexting을 사용하여 뽑아 봅니다.
# row
rows = [1,1,2,2,3,3,3]
cols = [2,5,1,4,1,3,4]

print(b[rows,cols])
'''
[ 9 12 14 17 20 22 23]
'''



#
# print(a[1])
# print(b[1])
# print(c[1])
# '''
# a[1] = [7, 8, 9, 10, 11, 12]
# b[1] = [ 7  8  9 10 11 12]
# c[1] = 2
# '''
#
# print(c[1:4])
# print(a[1:4])
# '''
# c[1:4] = [2 3 4]
# a[1:4] = [[7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
# '''
# print('-'*20)
# print(c[:4])
# print(a[:4])
# print(b[:4])
# '''
# c[:4] = [1 2 3 4]
# a[:4] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
# b[:4] = [[ 1  2  3  4  5  6]
#         [ 7  8  9 10 11 12]
#         [13 14 15 16 17 18]
#         [19 20 21 22 23 24]]
# '''
# print('-'*20)
# # 모든 행의 1열만 출력하고싶다.
# # [1, 7, 13, 19]
# print(a[:][1])
# '''
# [7, 8, 9, 10, 11, 12]
# # a[1][2] 값 하나를 뽑아올때는 이와 같은 표현이 가능하지만
#   a[:][1] 범위를 주어서 slicing을 할때는 이렇게 표현할 수 없다.
#     => fancy indexing을 사용해야한다.
# '''
#
# # print(a[1,2])       #파이썬 배열은 fancy indexing을 사용할 수 없다.
# print(b[1,2])
# '''
# 9
# # fancy indexing의 형식   배열명[행,열]
# # 배열명 [[index array],[index array]]
# # 배열명 [[boolean array],[boolean array]]
# '''
#
# print(b[1:3,])
# '''
# [[ 7  8  9 10 11 12]
#  [13 14 15 16 17 18]]
# '''
#
# print(b[[1,2],])
# '''
# [[ 7  8  9 10 11 12]
#  [13 14 15 16 17 18]]
# '''
# # 연습1) 모든 행에 대하여 1열부터 4열까지의 데이터를 출력해 봅니다.
# print('----- 연습1 -----')
# print(b[:,1:5])
# # print(b[[],[1,4]])
# '''
# [[ 2  3  4  5]
#  [ 8  9 10 11]
#  [14 15 16 17]
#  [20 21 22 23]]
#
# '''
#
# # 연습2) 모든 행에 대하여 1열, 3열, 5열의 데이터를 출력해 봅니다.
# print('----- 연습2 -----')
# print(b[: ,[1,3,5]])
# '''
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]
#  [20 22 24]]
# '''
#
# # 연습3) 짝수행만 모두 출력해봅니다.
# print('----- 연습3 -----')
# print(b[::2],)
# print(b[0::2,:])
# '''
# [[ 1  2  3  4  5  6]
#  [13 14 15 16 17 18]]
#  --------------------
# [[ 1  2  3  4  5  6]
#  [13 14 15 16 17 18]]
# '''
#
# # 연습) 짝수행에 대하여 1열부터 4열까지의 데이터를 출력해 봅니다.
# print('----- 연습4 -----')
# print(b[::2,1:5])
# '''
# [[ 2  3  4  5]
#  [14 15 16 17]]
# '''







# a = [0,1,2,3,4,5,6,7,8,9]
# print(a[0])
# print(a[1])
# print(a[0:3])
# print(a[-1])
# print(a[-2])
# print(a[3:])
# print(a[:3])                                                                #시작하는 index는 포함되지만. 끝나는 index는 포함되지 않습니다.
# # print(a[[0,3,4]])                                                         #파이썬 배열에는 index Array를 사용할 수 없다.
# # print(a[False,True,False,False,True,False,False,False,False,False])       #파이썬 배열에는 boolean Array를 사용할 수 없다.
# print(a[0:10:2])
# print(a[::2])
# print(a[::-1])
#
# print('-'*30)
#
# b = np.array(a)
# print(b[0])
# print(b[1])
# print(b[0:3])
# print(b[-1])
# print(b[-2])
# print(b[3:])
# print(b[:3])
# print(b[[0,3,4]])
# print(b[[False,True,False,False,True,False,False,False,False,False]])
# print(b[0:10:2])
# print(b[::2])
# print(b[::-1])
