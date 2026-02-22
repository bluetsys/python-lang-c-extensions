import math
from typing import List, Union

def cosine_similarity(vector_a: List[Union[int, float]], vector_b: List[Union[int, float]]) -> float:
    """
    두 벡터 간의 코사인 유사도를 계산합니다.
    
    Args:
        vector_a: 첫 번째 벡터
        vector_b: 두 번째 벡터
    
    Returns:
        코사인 유사도 값 (-1 ~ 1 사이)
    
    Raises:
        ValueError: 벡터의 길이가 다르거나 0인 경우
    """
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

# 벡터 생성
vector1 = list(range(1, 5))
vector2 = list(range(4, 8))

# 벡터 출력
print(vector1)  # [1, 2, 3, 4]
print(vector2)  # [4, 5, 6, 7]

# 코사인 유사도 계산
similarity = cosine_similarity(vector1, vector2)

# 유사도 출력
print(similarity)