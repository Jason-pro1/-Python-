def github_content(content1, head, tail):
    """在README中目录不能自动换行，在编辑目录时，
    需要在每一行后面添加一个tab(四个空格)，
    再一个enter才能做到真正换行"""
    count_1 = count_2 = 0
    content = content1.replace(tail, "    ")
    n = len(content)
    print('Standard Content:')
    for _ in range(n):
        if content[_] == head:
            count_2, count_1 = _, count_2
            print(content[count_1:count_2])
    print(content[count_2:_+1])
    
if __name__ == "__main__":
    content1 = input("Please Input Your Content:")
    head = input("Please Input Your Head:")
    tail = input("Please Input Your Tail:")
    github_content(content1, head, tail)
