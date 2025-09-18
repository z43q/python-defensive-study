#圆的面积计算及对于用户输入的合理性检测
#描述：通过获取圆的半径（r）计算面积（s）
#测试输入：输入圆的半径r
def is_positive_integer(input_value):       #创建验证函数，检测用户输入的合理性
    try:
        number = int(input_value)
        print(number)
        if number > 0:     #检测是否为正数
            return True,number#返回验证结果和转换
        else:
            return False,number,"输入必须为正整数"
    except ValueError:
        return False,input_value,"输入无效，请输入正整数"
def calculate_area():
    print("圆的面积计算,圆的半径应为正整数")
    r = input("请输入圆的半径：")
    while True:
        result = is_positive_integer(r)
        if result[0] == True:
            print("输入有效，圆的半径为：",result[1])
            print("圆的面积为：",3.14 * result[1] * result[1])
            break
        elif result[0] == False:
            print("输入无效，错误信息：",result[1])
            r = input("请重新输入圆的半径：")
if __name__ == "__main__":
    calculate_area()
