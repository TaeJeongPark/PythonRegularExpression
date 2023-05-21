## 파이썬 정규 표현식

# 정규 표현식(Regular Expression)은 문자열의 패턴을 찾거나 조작하기 위한 강력한 도구로, 파이썬에서도 널리 사용됩니다. 정규 표현식은 re 모듈을 사용하여 작성하고 적용할 수 있습니다.

# 파이썬에서 정규 표현식을 사용하기 위해 re 모듈을 import해야 합니다.

import re

# 패턴 매칭하기: re.match() 함수를 사용하여 문자열의 시작부터 패턴이 일치하는지 확인할 수 있습니다.
pattern = r"hello"
string = "hello world"
result = re.match(pattern, string)
if result:
    print("일치합니다.")
else:
    print("일치하지 않습니다.")

# 문자열에서 패턴 찾기: re.search() 함수를 사용하여 문자열 전체에서 패턴이 일치하는지 확인할 수 있습니다.
pattern = r"world"
string = "hello world"
result = re.search(pattern, string)
if result:
    print("일치합니다.")
else:
    print("일치하지 않습니다.")

# 패턴으로 문자열 분할하기: re.split() 함수를 사용하여 패턴을 기준으로 문자열을 분할할 수 있습니다.
pattern = r"\s+"  # 공백을 기준으로 분할
string = "hello     world"
result = re.split(pattern, string)
print(result)  # ['hello', 'world']

# 패턴으로 문자열 대체하기: re.sub() 함수를 사용하여 패턴과 일치하는 문자열을 대체할 수 있습니다.
pattern = r"apple"
string = "I like apple"
result = re.sub(pattern, "orange", string)
print(result)  # "I like orange"

# 패턴 그룹화하기: ()를 사용하여 패턴을 그룹화하고, 그룹화된 부분을 추출하거나 조작할 수 있습니다.
pattern = r"(\d+)-(\d+)-(\d+)"
string = "2023-05-21"
result = re.match(pattern, string)
if result:
    year = result.group(1)
    month = result.group(2)
    day = result.group(3)
    print(f"날짜: {year}년 {month}월 {day}일")

# 그룹화하기: ()을 사용하여 패턴을 그룹화할 수 있습니다. 그룹화된 패턴은 추출하거나 더 복잡한 정규 표현식에서 사용할 수 있습니다.
pattern = r"(\d+)-(\d+)-(\d+)"
string = "2023-05-21"
result = re.match(pattern, string)
if result:
    year = result.group(1)
    month = result.group(2)
    day = result.group(3)
    print(f"날짜: {year}년 {month}월 {day}일")
