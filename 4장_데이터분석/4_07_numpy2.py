#Numpy 배열의 생성과 변형

#numpy의 자료형 : numpy의 ndarray클래스는 포함하는 모든 데이터가 같은 자료형이어야 한다.


#  dtype접두사	 설명	        사용 예
#   t       	비트 필드   	t4 (4비트)
#   b	        불리언	        b (참 혹은 거짓)
#   i	        정수	        i8 (64비트)
#   u	        부호 없는 정수	u8 (64비트)
#   f	        부동소수점	    f8 (64비트)
#   c	        복소 부동소수점	c16 (128비트)
#   O	        객체	        0 (객체에 대한 포인터)
#   S, a	    문자열	        S24 (24 글자)
#   U       	유니코드 문자열	U24 (24 유니코드 글자)
#   V	        기타	        V12 (12바이트의 데이터 블럭)
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
print(x.dtype)

print(np.exp(-np.inf))

#배열 생성
a = np.zeros(5)
print(a)
b = np.zeros((5,2), dtype="f8")
print(b)

c = np.zeros(5, dtype="S4") #모든 원소의 문자열 크기가 같아야함
c[0] = "abcd"
c[1] = "ABCDE"              #더 큰 크기의 문자열을 할당하면 잘릴 수 있음.
print(c)

d = np.ones((2,3,4), dtype="i8")  #1로 초기화된 배열
print(d)

e = range(10)
print(e)
f = np.ones_like(e, dtype="f")
print(f)

g = np.empty((4,3))   #random 값
print(g)

print(np.arange(10)) # 0.. n-1
print(np.arange(3, 21, 2)) #시작, 끝(-1)까지, 간격
print(np.linspace(0, 100, 5)) #시작, 끝까지, 갯수 (선형 구간 혹은 로그 구간을 지정한 구간의 갯수만큼 분할)
print(np.logspace(0, 4, 4, endpoint=False)) # 1, 10, 100, 1000
print(np.random.seed(0))
print(np.random.rand(4)) #uniform 분포 따르는 난수생성
print(np.random.randn(3, 5)) #가우시안 정규분포 따르는 난수생성

# 전치연산 : 2차원 배열의 전치(transpose) 연산은 행과 열을 바꾸는 것(T)

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.T)

# 배열의 크기 변형

a = np.arange(12)
print(a)
b = a.reshape(3, 4)
print(b)
c = a.reshape(2, 2, -1) # -1 전체
print(c)
d = a.reshape(2, -1, 2)
print(d)


print(a.flatten())  # 무조건1차원으로 펼침
x = np.arange(5)
print(x)
y = x.reshape(1,5)
print(y)
z = x.reshape(5,1)
print(z)
print(x[:, np.newaxis])  #같은 배열에 대해 차원만 1차원 증가 시킴


#배열 연결

a1 = np.ones((2, 3))
print(a1)
a2 = np.zeros((2, 2))
print(a2)
a3 = np.hstack([a1, a2])  #행의 수가 같은 두개 이상의 배열을 옆으로 연결해 열의 수가 더 많은 배열을 만듬
print(a3)

b1 = np.ones((2,3))
print(b1)
b2 = np.zeros((3,3))
print(b2)

b3 = np.vstack([b1, b2])  # 열의 수가 같은 두개 이상의 배열을 위아래로 연결(연결할 배열은 하나의 리스트에 담아야함)
print(b3)

c1 = np.ones((3,4))
print(c1)
c2 = np.zeros((3,4))
print(c2)
c3 = np.dstack([c1, c2])    #행이나 열이 아닌 depth 방향으로 배열을 합침. 가장 안쪽의 원소의 차원이 증가함. 즉 가장 내부의 숫자 원소가 배열이 됨.
print(c3)    # 2개의 (3X4) -> 1개의 (3X4X2)가 됨
c4 = np.dstack([c1, c2]).shape
print(c4)

r = np.r_[np.array([1,2,3]), np.array([4,5,6])] #메소드지만 소괄호를 사용하지 않고 인덱싱과 같이 대괄호를 사용(이런 특수 메소드를 인덱서라고 함)
print(r)

c = np.c_[np.array([1,2,3]), np.array([4,5,6])]  # 배열의 차원을 증가시킨 후 좌우로 연결.
print(c)

a = np.array([0,1,2])
a_tile = np.tile(a,2) # 동일한 배열을 반복해 연결
print(a_tile)
print(np.tile(a, (3, 2)))

#그리드 생성
x = np.arange(3)
print(x)
y = np.arange(5)
print(y)

X, Y = np.meshgrid(x, y)
print(X)
print(Y)

print([zip(x, y) for x, y in zip(X, Y)])

print(plt.scatter(X, Y, linewidths=10))
print(plt.show())






