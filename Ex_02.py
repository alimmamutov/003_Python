# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
odd_to_15 = (num for num in range(1, 16, 2))
print(*odd_to_15)
