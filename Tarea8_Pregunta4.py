def sumatoria(num):
    if num>1:
        num=num+sumatoria(num-1)
    return num
print(sumatoria(5))