import cosine_similarity as cs
import math
import timeit
import random

def cosine_similarity(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("벡터의 길이가 같아야 합니다.")
    
    if len(vector_a) == 0:
        raise ValueError("벡터는 비어있을 수 없습니다.")
    
    # 내적(dot product) 계산
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    
    # 각 벡터의 크기(magnitude) 계산
    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))
    
    # 0으로 나누는 것을 방지
    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("벡터의 크기가 0일 수 없습니다.")
    
    # 코사인 유사도 계산
    return dot_product / (magnitude_a * magnitude_b)

def cosine_similarity_c(vector_a, vector_b):
    # 코사인 유사도 계산
    return cs.cosine_similarity(vector_a, vector_b)


# 난수 고정
random.seed(123)

# 대규모 벡터 생성
n = int(1e7)

# 큰 랜덤 벡터 생성
vector1 = [random.uniform(0, 1) for _ in range(n)]
vector2 = [random.uniform(0, 1) for _ in range(n)]

# 벡터 출력
print(f"vector1                        : {vector1[:3]}")
print(f"vector2                        : {vector2[:3]}")
print()

result = cosine_similarity(vector1, vector2)
print(f"Python 코사인 유사도 결과      : {result}")
result = cosine_similarity_c(vector1, vector2)
print(f"C 코사인 유사도 결과           : {result}")

print()

# 코사인 유사도 계산 성능 테스트
def measure_performance(func, vector1, vector2, iterations=10):
    # 함수 성능 측정
    times = [timeit.timeit(lambda: func(vector1, vector2), number=1) for _ in range(iterations)]
    return {
        'min': min(times),  # 최소 실행 시간
        'lq': sorted(times)[int(0.25 * iterations)],  # 하위 사분위수
        'mean': sum(times) / iterations,  # 평균 실행 시간
        'median': sorted(times)[iterations // 2],  # 중앙값
        'uq': sorted(times)[int(0.75 * iterations)],  # 상위 사분위수
        'max': max(times),  # 최대 실행 시간
        'neval': iterations  # 평가 횟수
    }

# Python 및 C 구현의 성능 측정
python_performance = measure_performance(cosine_similarity, vector1, vector2)
c_performance = measure_performance(cosine_similarity_c, vector1, vector2)

# 성능 테이블에 사용할 데이터 준비
data = [
    {'expr': 'Python', **python_performance},
    {'expr': 'C', **c_performance},
]

# 성능 테이블 출력
def print_performance_table(data):
    header = f"{'expr':<8}{'min':>10}{'lq':>10}{'mean':>10}{'median':>10}{'uq':>10}{'max':>10}{'neval':>6}"
    print(header)
    print("-" * len(header))

    for row in data:
        print(f"{row['expr']:<8}{row['min']:>10.5f}{row['lq']:>10.5f}{row['mean']:>10.5f}{row['median']:>10.5f}{row['uq']:>10.5f}{row['max']:>10.5f}{row['neval']:>6}")

    # Python과 C 성능 비교
    python_time = next((row['mean'] for row in data if row['expr'] == 'Python'), None)
    c_time = next((row['mean'] for row in data if row['expr'] == 'C'), None)

    if python_time and c_time:
        speedup = python_time / c_time
        print(f"\nC 구현이 Python 구현보다 {speedup:.2f}배 빠릅니다.")

measure_performance = print_performance_table(data)