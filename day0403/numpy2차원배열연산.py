import numpy as np
'''
       월    화    수    목    금
딸기  1000  1100  1000  900  1500
수박  80     80    100   50   40
포도  60     70    40    50   60
'''
qty = np.array([[1000,1100,1000,900,1500],[80,80,100,50,40],[60,70,40,50,60]])
print(qty)

# 전체 판매량
print(np.sum(qty))
'''
6130
'''

# 과일별 전체판매량
print(np.sum(qty,axis=0))
'''
[1140 1250 1140 1000 1600]
'''

# 요일별 전체판매량
print(np.sum(qty,axis=1))
'''
[5500  350  280]
'''

# 과일별 max값
print(np.max(qty,axis=0))
'''
[1000 1100 1000  900 1500]
'''


# 요일별 max값
print(np.max(qty,axis=1))
'''
[1500  100   70]
'''