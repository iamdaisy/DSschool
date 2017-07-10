import numpy as np

#1차원 배열 만들기
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)
print(type(a))

#벡터화 연산
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
for ai in a:
    b.append(ai * 2)
print(b)
x = np.array(a)
print(x)
print(x * 2)
L=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(2 * L)  # 리스트 객체에 정수를 곱하면 객체의 크기가 정수배 만큼 증가

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(2 * a + b) #벡터화 연산은 모든 수학 연산에 대해 적용

print(np.exp(a))
print(np.exp(a))
print(np.log(b))
print(np.sin(a))

#2차원 배열 만들기
b = np.array([[0, 1, 2], [3, 4, 5]])  # 2 X 3 array
print(b)
print(len(b))     #2
print(len(b[0]))  #3

#연습문제1

prac1 = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(prac1)


#3차원 배열 만들기
c = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[11,12,13,14],[15,16,17,18],[19,20,21,22]]])   # 2 x 3 x 4 array
print(c)

print(len(c))       #2
print(len(c[0]))    #3
print(len(c[0][0])) #4

#배열의 차원과 크기 알아내기 : ndim 속성과 shape 속성으로 알수 있음

print(a.ndim)   #1 [1, 2, 3]
print(a.shape)  #(3,)
print(b.ndim)   #2
print(b.shape)  #(2, 3)
print(c.ndim)   #2
print(c.shape)  #(2, 3, 4)

#배열의 인덱싱 : 배열 객체로 구현한 다차원 배열의 원소 하나 하나는 콤마를 사용해 접근가능함. 콤마로 구분된 차원을 축(axis).

a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)
print(a[0,0])  #첫번째 행의 첫번째 열
print(a[0,1])  #첫번째 행의 두번째 열
print(a[-1, -1]) #마지막 행의 마지막 열

#배열 슬라이싱

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(a)
print(a[0, :])   #첫번째 행 전체
print(a[:, 1])   #두번째 열 전체
print(a[:2, :2]) #첫번째 행에서 2열까지, 두번째 행에서 2열까지

#연습문제2
m = np.array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])

print(m[1, 2])   #7 인덱싱
print(m[2, 4])   # 14 인덱싱
print(m[1, 1:3]) # [6, 7] 슬라이싱
print(m[1:, 2])  # [7, 12] 슬라이싱
print(m[:2, 3:]) # [[3,4], [8, 9]] 슬라이싱

#배열 인덱싱

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True, False, True, False, True, False])
print(a[idx])












