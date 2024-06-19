def largest_by_sliding_window(n: list[int], k: int) -> list[int]:
    return [max(n[i:i+k]) for i in range(len(n)-k+1)]

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3

largest_by_sliding_window(num_list,k)