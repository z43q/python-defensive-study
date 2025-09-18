#检测用户输入的合法性
def is_positive_input(case,value_input):
    if case == "1":
        if int(value_input) >= -273.15:
            return True,int(value_input)
        else:
            return False,"输入错误，摄氏度不能低于-273.15"
    elif case == "2":
        if int(value_input) >= -459.67:
            return True,int(value_input)
        else:
            return False,"输入错误，华氏度不能低于-459.67"
    else:
        return False,"输入错误，未知的转换类型"
#获取用户输入，来进行温度转换服务及温度表参考
def get_user_input():
    print("请选择想要进行的温度转换：\n1.摄氏度转华氏度\n2.华氏度转摄氏度")
    choice = input("请输入你的选择（1/2）：")
    while choice not in ["1","2"]:
        print("输入错误，请输入1或2")
        choice = input("请输入你的选择（1/2）：")
    return choice
#根据用户选择，进行温度转换,并返回摄氏度结果

def convert_temperature(choice):
    #global celsius
    if choice == "1":
        celsius = float(input("请输入摄氏度："))
        while True:
            result = is_positive_input(choice,int(celsius))
            if result[0]:
                celsius = result[1]
                break
            else:
                print(result[1])
                celsius = float(input("请输入摄氏度："))
        fahrenheit = celsius * 9/5 + 32
        print("转换后的温度为：%.2f" % fahrenheit,"F")
        return celsius
    elif choice == "2":
        fahrenheit = float(input("请输入华氏度："))
        while True:
            result = is_positive_input(choice,int(fahrenheit))
            if result[0]:
                fahrenheit = result[1]
                break
            else:
                print(result[1])
                fahrenheit = float(input("请输入华氏度："))
        celsius = (fahrenheit - 32) * 5/9
        print("转换后的温度为：%.2f" % celsius,"C")
        return celsius
    return None
#根据用户输入的温度进行温度表参考
#build_table.py：一次性脚本，生成 desc_table.py
import textwrap


def classify(t: float) -> str:
    """生活场景分界，单位 ℃"""
    if t <= -40: return "极寒，南极级别"
    if t <= -20: return "严寒，羽绒服+羽绒裤"
    if t <= -10: return "很冷，毛衣+外套"
    if t <= 0: return "冰点，路面可能结冰"
    if t <= 10: return "凉爽，单长袖"
    if t <= 22: return "舒适，短袖/晴天"
    if t <= 30: return "热，需防晒"
    if t <= 35: return "炎热，官方高温日"
    if t <= 40: return "酷热，减少外出"
    return "极热，沙哈拉级别"


step = 0.5
start, end = -60, 80
n = int((end - start) / step) + 1
table = [classify(start + i * step) for i in range(n)]

with open("desc_table.py", "w", encoding="utf-8") as f:
    f.write("# 自动生成，别手动改\n")
    f.write(f"START={start}\nSTEP={step}\n")
    f.write("TABLE=" + textwrap.wrap(repr(table),width=10000)[0] + "\n")
#温度表参考输出
# temp_desc.py
from desc_table import START, STEP, TABLE

def temp_desc(t: float) -> str:
    """
    输入：任意摄氏温度（float）
    返回：一句人话描述
    """
    idx = int(round((t - START) / STEP))
    # 边界保护
    idx = max(0, min(idx, len(TABLE) - 1))
    return TABLE[idx]
#主函数，用于控制程序流程
def main():
    choice = get_user_input()
    t = convert_temperature(choice)
    print("此温度描述为：",temp_desc(t),"，哦！")
if __name__ == "__main__":
    main()

