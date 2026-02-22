import foo

# 예시
vector = [float(x) for x in range(1, 10)]  # [1.0, 2.0, 3.0, ...]
vector = [x for x in range(1, 10)]  # [1.0, 2.0, 3.0, ...]
vector = list(range(1, 10))

print(vector)  # [1.0, 2.0, 3.0, ...]

result = foo.foo(vector)
print(result)  # 285.0