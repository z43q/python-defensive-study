
def test_is_positive_integer():
    #测试正常输入，整型，正整数
    assert is_positive_integer("10") == (True,10)
    assert is_positive_integer("43") == (True,43)
    #测试异常输入，非整型，负整数
    assert is_positive_integer("-10") == (False,-10,"输入必须为正整数")
    assert is_positive_integer("-43") == (False,-43,"输入必须为正整数")
    #测试异常输入，非整型，零
    assert is_positive_integer("0") == (False,0,"输入必须为正整数")
    #测试异常输入，浮点型
    assert is_positive_integer("3.14") == (False,"3.14","输入无效，请输入正整数")
    assert is_positive_integer("10.12") == (False,"10.12","输入无效，请输入正整数")
    #测试异常输入，字符串
    assert is_positive_integer("a") == (False,"a","输入无效，请输入正整数")
    assert is_positive_integer("ab") == (False, "ab", "输入无效，请输入正整数")
    assert is_positive_integer("=") == (False, "=", "输入无效，请输入正整数")
    #测试异常输入，空字符串
    assert is_positive_integer("") == (False, "", "输入无效，请输入正整数")
    #测试异常输入，None
    assert is_positive_integer(None) == (False, None, "输入无效，请输入正整数")
    #测试异常输入，列表
    assert is_positive_integer([1, 2, 3]) == (False, [1, 2, 3], "输入无效，请输入正整数")
    #测试异常输入，元组
    assert is_positive_integer((1, 2, 3)) == (False, (1, 2, 3), "输入无效，请输入正整数")
    #测试异常输入，字典
    assert is_positive_integer({"a":1, "b":2, "c":3}) == (False, {"a":1, "b":2, "c":3}, "输入无效，请输入正整数")
    #测试异常输入，集合
    assert is_positive_integer({1, 2, 3}) == (False, {1, 2, 3}, "输入无效，请输入正整数")
    print("所有测试成功通过")
if __name__ == '__main__':
    test_is_positive_integer()
