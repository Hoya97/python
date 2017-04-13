###튜플 자료형
#튜플(tuple)은 몇가지 점을 제외하고는 리스트와 거의 비슷함
"""
리스트와 다른점은
-리스트는 [과 ]으로 둘러 싸는데 튜플은 (과 )으로 둘러싼다.
-리스트는 그 값의 생성,삭제,수정이 가능하지만 튜플은 그 값을 바꿀수 없다

튜플의 모습
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1, 2, 3
t5 = ('a','b',('ab','cd'))
리스트와 차이점은 튜플에서는 t2 = (1,)처럼 단지 1개의 요소만을 가질때 요소 뒤에 콤마(,)를 반드시 붙여야 한다는 점과
t4 = 1,2,3처럼 괄호()를 생략해도 무방하다는 점이다

튜플과 리스트의 큰 차이는 값을 변화시킬 수 있는가 없는가이다
즉, 튜플은 값이 항상 변이지 않기를 바랄때 사용하고
리스트는 수시로 그 값을 변화 시켜야 할때 사용해야된다.
"""

##튜플의 요소값을 지우거나 변경하려고 하면 오류가 발생한다

##튜플의 인덱싱과 슬라이싱, 더하기(+)와 곱하기(*)
#인덱싱
t1 = (1,2,'a','b')
print(t1[0]) # 1
print(t1[3])

print('ㅡ'*50) # 구분선

#슬라이싱
t1 = (1,2,'a','b')
print(t1[1:]) # (2, 'a', 'b')

print('ㅡ'*50) # 구분선

#튜플 더하기
t2 = (3,4)
print(t1 + t2) # (1, 2, 'a', 'b', 3, 4)  ### (1,2,'a','b') + (3,4)

print('ㅡ'*50) # 구분선

#튜플 곱하기
print(t2*3) # (3, 4, 3, 4, 3, 4) # (3,4)*3 