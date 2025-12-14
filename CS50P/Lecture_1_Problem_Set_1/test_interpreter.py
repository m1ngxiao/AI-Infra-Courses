import pytest
from interpreter import eval


class TestEvalFunction:
    """测试eval函数的各种场景"""
    
    def test_addition_positive_numbers(self):
        """测试正数加法"""
        result = eval("2", "+", "3")
        assert result == 5.0
        assert isinstance(result, float)
    
    def test_addition_negative_numbers(self):
        """测试负数加法"""
        result = eval("-2", "+", "-3")
        assert result == -5.0
        assert isinstance(result, float)
    
    def test_addition_mixed_numbers(self):
        """测试混合符号加法"""
        result = eval("-5", "+", "10")
        assert result == 5.0
        assert isinstance(result, float)
    
    def test_addition_decimal_numbers(self):
        """测试小数加法"""
        result = eval("2.5", "+", "3.7")
        assert result == 6.2
        assert isinstance(result, float)
    
    def test_subtraction_positive_numbers(self):
        """测试正数减法"""
        result = eval("10", "-", "3")
        assert result == 7
        assert isinstance(result, int)
    
    def test_subtraction_negative_numbers(self):
        """测试负数减法"""
        result = eval("-5", "-", "-2")
        assert result == -3
        assert isinstance(result, int)
    
    def test_subtraction_zero(self):
        """测试包含零的减法"""
        result = eval("5", "-", "0")
        assert result == 5
        assert isinstance(result, int)
    
    def test_subtraction_negative_result(self):
        """测试结果为负数的减法"""
        result = eval("3", "-", "10")
        assert result == -7
        assert isinstance(result, int)
    
    def test_multiplication_positive_numbers(self):
        """测试正数乘法"""
        result = eval("4", "*", "5")
        assert result == 20
        assert isinstance(result, int)
    
    def test_multiplication_negative_numbers(self):
        """测试负数乘法"""
        result = eval("-3", "*", "-2")
        assert result == 6
        assert isinstance(result, int)
    
    def test_multiplication_mixed_signs(self):
        """测试混合符号乘法"""
        result = eval("-3", "*", "2")
        assert result == -6
        assert isinstance(result, int)
    
    def test_multiplication_zero(self):
        """测试零乘法"""
        result = eval("100", "*", "0")
        assert result == 0
        assert isinstance(result, int)
    
    def test_multiplication_large_numbers(self):
        """测试大数乘法"""
        result = eval("1000", "*", "1000")
        assert result == 1000000
        assert isinstance(result, int)
    
    def test_division_exact(self):
        """测试整除"""
        result = eval("10", "/", "2")
        assert result == 5.0
        assert isinstance(result, float)
    
    def test_division_decimal(self):
        """测试产生小数的除法"""
        result = eval("7", "/", "2")
        assert result == 3.5
        assert isinstance(result, float)
    
    def test_division_negative_numbers(self):
        """测试负数除法"""
        result = eval("-10", "/", "-2")
        assert result == 5.0
        assert isinstance(result, float)
    
    def test_division_mixed_signs(self):
        """测试混合符号除法"""
        result = eval("-10", "/", "2")
        assert result == -5.0
        assert isinstance(result, float)
    
    def test_division_by_zero(self):
        """测试除零错误 - 应该抛出异常"""
        with pytest.raises(ZeroDivisionError):
            eval("10", "/", "0")
    
    def test_invalid_operator(self):
        """测试无效操作符"""
        result = eval("2", "^", "3")
        assert result == "Error: Invalid operator"
    
    def test_empty_operator(self):
        """测试空操作符"""
        result = eval("2", "", "3")
        assert result == "Error: Invalid operator"
    
    def test_special_characters_as_operator(self):
        """测试特殊字符作为操作符"""
        result = eval("2", "@", "3")
        assert result == "Error: Invalid operator"
    
    def test_addition_with_non_numeric_input(self):
        """测试加法中使用非数字输入"""
        with pytest.raises(ValueError):
            eval("abc", "+", "3")
        
        with pytest.raises(ValueError):
            eval("2", "+", "xyz")
        
        with pytest.raises(ValueError):
            eval("abc", "+", "xyz")
    
    def test_subtraction_with_non_numeric_input(self):
        """测试减法中使用非数字输入"""
        with pytest.raises(ValueError):
            eval("abc", "-", "3")
        
        with pytest.raises(ValueError):
            eval("2", "-", "xyz")
    
    def test_multiplication_with_non_numeric_input(self):
        """测试乘法中使用非数字输入"""
        with pytest.raises(ValueError):
            eval("abc", "*", "3")
        
        with pytest.raises(ValueError):
            eval("2", "*", "xyz")
    
    def test_division_with_non_numeric_input(self):
        """测试除法中使用非数字输入"""
        with pytest.raises(ValueError):
            eval("abc", "/", "3")
        
        with pytest.raises(ValueError):
            eval("2", "/", "xyz")
    
    def test_float_in_subtraction(self):
        """测试减法中使用浮点数 - 注意这里有个bug，因为函数期望int"""
        # 这个测试会失败，因为int("2.5")会抛出ValueError
        with pytest.raises(ValueError):
            eval("2.5", "-", "1")
    
    def test_float_in_multiplication(self):
        """测试乘法中使用浮点数"""
        # 这个测试会失败，因为int("2.5")会抛出ValueError
        with pytest.raises(ValueError):
            eval("2.5", "*", "3")
    
    def test_float_in_division(self):
        """测试除法中使用浮点数"""
        # 这个测试会失败，因为int("2.5")会抛出ValueError
        with pytest.raises(ValueError):
            eval("2.5", "/", "3")
    
    def test_edge_case_large_numbers(self):
        """测试边界情况：大数字"""
        # 测试加法大数
        result = eval("999999999", "+", "1")
        assert result == 1000000000.0
        
        # 测试乘法大数（可能溢出，但在Python中int是无限精度的）
        result = eval("1000000", "*", "1000000")
        assert result == 1000000000000
    
    def test_edge_case_small_numbers(self):
        """测试边界情况：小数字"""
        result = eval("1", "/", "1000000")
        assert result == 0.000001
        
        result = eval("0", "+", "0")
        assert result == 0.0
    
    def test_edge_case_single_digit_numbers(self):
        """测试边界情况：单位数"""
        result = eval("1", "+", "1")
        assert result == 2.0
        
        result = eval("9", "*", "9")
        assert result == 81
        
        result = eval("5", "-", "5")
        assert result == 0
        
        result = eval("1", "/", "1")
        assert result == 1.0


class TestTypeConsistency:
    """测试函数返回类型的一致性问题"""
    
    def test_addition_returns_float(self):
        """测试加法总是返回float"""
        result1 = eval("2", "+", "3")
        assert isinstance(result1, float)
        
        result2 = eval("2.0", "+", "3.0")
        assert isinstance(result2, float)
    
    def test_subtraction_returns_int(self):
        """测试减法总是返回int"""
        result1 = eval("10", "-", "3")
        assert isinstance(result1, int)
        
        result2 = eval("10", "-", "3")  # 即使输入看起来是整数
        assert isinstance(result2, int)
    
    def test_multiplication_returns_int(self):
        """测试乘法总是返回int"""
        result1 = eval("4", "*", "5")
        assert isinstance(result1, int)
    
    def test_division_returns_float(self):
        """测试除法总是返回float"""
        result1 = eval("10", "/", "2")
        assert isinstance(result1, float)
        
        # 即使是整除，也返回float
        result2 = eval("8", "/", "4")
        assert isinstance(result2, float)


class TestInputValidation:
    """测试输入验证和边界情况"""
    
    def test_empty_strings(self):
        """测试空字符串输入"""
        with pytest.raises(ValueError):
            eval("", "+", "3")
        
        with pytest.raises(ValueError):
            eval("2", "+", "")
    
    def test_whitespace_strings(self):
        """测试只包含空格的字符串"""
        with pytest.raises(ValueError):
            eval("   ", "+", "3")
        
        with pytest.raises(ValueError):
            eval("2", "+", "   ")
    
    def test_string_with_whitespace(self):
        """测试包含空格的字符串"""
        with pytest.raises(ValueError):
            eval(" 2 ", "+", "3")
        
        with pytest.raises(ValueError):
            eval("2", "+", " 3 ")
    
    def test_scientific_notation(self):
        """测试科学计数法输入"""
        with pytest.raises(ValueError):
            eval("1e5", "+", "3")
    
    def test_hexadecimal_input(self):
        """测试十六进制输入"""
        with pytest.raises(ValueError):
            eval("0xFF", "+", "3")
    
    def test_binary_input(self):
        """测试二进制输入"""
        with pytest.raises(ValueError):
            eval("0b101", "+", "3")