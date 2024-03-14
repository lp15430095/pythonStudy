def main():
    try:
        a=int(input('请输入两第一个数：'))
        b=int(input('请输入两第二个数：'))
        result=cal(a,b)
    except:
        print("您的输入有误，请重新输入！")
        return
    print(f'{a}+{b}={result}')
def cal(a,b):
    return a+b
if __name__ == '__main__':
    main()