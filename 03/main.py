import cosine_similarity

# 벡터 생성
vector1 = list(range(1, 5))
vector2 = list(range(4, 8))

# 벡터 출력
print(vector1)  # [1, 2, 3, 4]
print(vector2)  # [4, 5, 6, 7]

# 코사인 유사도 계산
similarity = cosine_similarity.cosine_similarity(vector1, vector2)

# 유사도 출력
print(similarity)