#通过用户的输入来绘制同切圆
#导入turtle绘图模块
import turtle
#检测用户输入是否合法
def is_positive_input(input_value):
    try:
        number = int(input_value)
        if number > 0:     #检测是否为正数
            return True,number#返回验证结果和转换
        else:
            return False,number,"输入必须为正整数"
    except ValueError:
        return False,input_value,"输入无效，请输入正整数"
#检测用户输入是否合理
def is_valid_input(type_number,input_value):
    if type_number == 1:
        #检测半径是否合理
        if input_value < 300:
            return True
        else:
            print("输入的半径不合理，失去绘图意义，建议圆的半径小于300")
            case = input("是否重新输入？yes/no")
            if case == "yes":
                return False
            else:
                return True
    elif type_number == 2:
        #检测速度是否合理
        if 0 <= input_value <= 10:
            return True
        else:
            print("输入的速度不合理，建议速度在0-10之间")
            case = input("是否重新输入？yes/no")
            if case == "yes":
                return False
            else:
                return True
    elif type_number == 3 :
        #检测颜色是否合理
        if 0 <= input_value <= 255:
            return True
        else:
            print("输入的颜色不合理，建议颜色在0-255之间")
            case = input("是否重新输入？yes/no")
            if case == "yes":
                return False
            else:
                return True
    elif type_number == 4:
        #检测画笔的大小是否合理
        if 0 <= input_value <= 10:
            return True
        else:
            print("输入的画笔大小不合理，建议画笔大小在0-10之间")
            case = input("是否重新输入？yes/no")
            if case == "yes":
                return False
            else:
                return True
    return None


#获取用户操作
def main():
    case = input("是否更改画笔设置？yes/no")
    if case == "yes":
        set_pen_size()
        set_pen_color()
        set_pen_speed()
    else:
        print("默认画笔大小为：3")
        turtle.pensize(3)
        print("默认画笔颜色为：黑色")
        turtle.pencolor("black")
        print("默认画笔速度为：10")
        turtle.speed(10)
#全屏窗口
def draw_windows():
    #设置turtle窗口大小
    screen = turtle.Screen()
    #设置turtle窗口标题
    screen.title("同切圆的绘制")
    #设置turtle窗口为全屏
    screen.setup(width=1.0, height=1.0)
def set_pen_color():
    #设置turtle画笔颜色
    print("是否通过RGB值设置画笔颜色？")
    case = input("yes/no")
    if case == "yes":
        color_rgb = []
        for i in range(3):
            rgb = input("请输入画笔颜色RGB（0-255）：")
            #检测用户输入的合法性与合理性
            while True:
                result = is_positive_input(rgb)
                if result[0] and is_valid_input(3,int(rgb)) == True:
                    print("输入有效，画笔颜色RGB为：",result[1])
                    break
                elif result[0] == False:
                    print("输入无效，错误信息：",result[1])
                    rgb = input("请重新输入画笔颜色RGB（0-255）：")
            color_rgb.append(int(rgb))
        turtle.pencolor((int(color_rgb[0]), int(color_rgb[1]),int(color_rgb[2])))
    else:
        print("默认画笔颜色为：黑色")
        turtle.pencolor("black")
def set_pen_speed():
    #设置turtle画笔速度
    print("是否通过设置画笔速度？")
    case = input("yes/no")
    if case == "yes":
        speed_number = input("请设置画笔速度（0-10）：")
        while True:
            result = is_positive_input(speed_number)
            if result[0] and is_valid_input(2,int(speed_number)) == True:
                print("输入有效，画笔速度为：",result[1])
                break
            elif result[0] == False:
                print("输入无效，错误信息：",result[1])
                speed_number = input("请重新设置画笔速度（0-10）：")
        turtle.speed(int(speed_number))
    else:
        print("默认画笔速度为：10")
        turtle.speed(10)
def set_pen_size():
    #设置turtle画笔大小
    print("是否设置画笔大小？")
    case = input("yes/no")
    if case == "yes":
        size_number = input("请设置画笔大小（0-10）：")
        while True:
            result = is_positive_input(size_number)
            if result[0] and is_valid_input(4,int(size_number)) == True:
                print("输入有效，画笔大小为：",result[1])
                break
            elif result[0] == False:
                print("输入无效，错误信息：",result[1])
                size_number = input("请重新设置画笔大小（0-10）：")
        turtle.pensize(int(size_number))
    else:
        print("默认画笔大小为：3")
        turtle.pensize(3)
def draw_circle():
    circle_r_number = []
    circle_number = input("你想画几个同切圆：")
    while True:
        result = is_positive_input(circle_number)
        if result[0] == True:
            print("输入有效，圆的数量为：",result[1])
            break
        elif result[0] == False:
            print("输入无效，错误信息：",result[1])
            circle_number = input("请重新输入圆的数量：")
    for i in range(int(circle_number)):
        radius = input("请输入第"+str(i+1)+"个圆的半径：")
        while True:
            result = is_positive_input(radius)
            if result[0] and is_valid_input(1,int(radius)) == True:
                print("输入有效，圆的半径为：",result[1])
                break
            elif result[0] == False:
                print("输入无效，错误信息：",result[1])
                radius = input("请重新输入圆的半径：")
        circle_r_number.append(radius)
    for r in range(int(circle_number)):
        turtle.circle(int(circle_r_number[r]))
    print("绘制完成")
    turtle.done()
if __name__ == "__main__":
    main()
    draw_windows()
    draw_circle()

