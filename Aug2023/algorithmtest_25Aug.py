# Q1. 딕셔너리 구조에서 Value 값이 25 이상 필터링 후 출력

# answer1
d = {'a': 25, 'b': 2, 'c': 45, 'd': 21, 'e': 44, 'f': 99}
new_d = {key: d[key] for key in d if d[key] >= 25}
print(new_d)

# answer2
result = {}
for k, v in d.items():
    if v >= 25:
        result[k] = v
print(f'ex1 결과 : {result}')

# Q2. 딕셔너리를 활용하여 아래와 같이 출력해주세요
# key "one" has values [1, 2, 3, 4, 5, 6, 7, 8, 9] -> total : 9 key "two" has values [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] -> total : 23 key "three" has values [44, 45, 46, 47, 48] -> total : 5

# answer1
d = dict(one=list(range(1, 10)), two=list(
    range(11, 34)), three=list(range(44, 49)))

for k, v in d.items():
    print(f'key "{k}" has values {v} -> total : {len(v)}')

# answer2
d = {
    'one': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'two': [i for i in range(11, 34)],
    'three': [44, 45, 46, 47, 48]
}

for key in d.keys():
    print(f"key\"{key}\" has values {d[key]}->total:{len(d[key])}")

# Stack 구현하기


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# method
# __init__: magic method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}살입니다.")


# Person 클래스의 인스턴스 생성 및 초기화
person1 = Person("kw.im", 22)
person2 = Person("ch.lee", 20)

# 인스턴스 변수에 접근하여 정보 출력
person1.introduce()  # 출력: 안녕하세요, 제 이름은 kw.im이고, 나이는 22살입니다.
person2.introduce()  # 출력: 안녕하세요, 제 이름은 ch.lee이고, 나이는 20살입니다.

# 문자열 -> 리스트
# 힌트: split()
# 결과: ['a', ' b', ' c', ' d']
str_ = 'a, b, c, d'
['a', ' b', ' c', ' d']
x = str_.split(", ")
print(x)

# 리스트 -> 문자열
# 힌트: join()
# 결과: str_ = abcd, str_2 = a& b& c& d
list_ = ['a', 'b', 'c', 'd']

x = "".join(list_)
y = "&".join(list_)
print(x, y)

# N개의 단위로 아래와 같이 리스트로 출력(함수)
# - 결과: [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R'], ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z']]
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

def split_n_list(split_size=3):
    answer = list()

    for i in range(0, len(alphabet_list), split_size):
        # 인덱스 확인
        # print(i, i+split_size)

        answer.append(alphabet_list[i:i + split_size])

    return answer

print(f'결과: {split_n_list(3)}')

# 키보드 Backspace 기능 구현
# input_string = '123//45/6789///'
# /를 만나면 앞의 값을 삭제
# 참고 - 맨앞에 /만나면 어떻게 처리해야 되는지 생각 해보기
# answer = '146'

# answer

input_string = '123//45/6789///'

def backspace_string(input_string):
    stack = []
    for x in input_string:
        if x == "/":
            if len(stack) > 0:
                # if stack:
                stack.pop()
        else:
            stack.append(x)
    return "".join(stack)


print(backspace_string("123//45/6789///"))  # 146

# Q. 괄호 문법 검사기
# bracket1: [[[[]]]][] → answer ‘YES’
# bracket2: [[[[[[[[[[[[[[[[]] → answer ‘NO’
# [[[[]]]][]
# [[[[[[[[[[[[[[[[]]

# 기본틀
def is_bracket(b):
    answer = "YES"

    return answer

# 정답
def is_bracket(b):
    answer = "YES"
    stack = []
    for x in b:
        if x == "]":
            if len(stack) == 0:
                return "NO"
            stack.pop()
        else:
            stack.append(x)

    if len(stack) > 0:
        return "NO"

    return answer


# YES
print(is_bracket("[[[[]]]][]"))

# No
print(is_bracket("[[[[[[[[[[[[[[[[]]"))


# 문제: 아래와 같이 홀수는 그대로, 짝수는 x 10을하여 리스트로 출력해주세요.
# 정답: [1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15, 160, 17, 180, 19, 200]

# 문제: Hyundai, Kia를 추출하여 대문자 리스트로 출력하세요.
# 힌트: lower(), upper()
# 출력 : ['HYUNDAI', 'KIA']

car_brands = ["Tesla", "BMW", "Audi", "Hyundai", "Ferrari", "Kia"]

# 문제
# 20 ~ -15 출력하되 -2 씩 감소 
# range 함수 활용


