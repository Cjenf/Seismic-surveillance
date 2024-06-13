class _InternalClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# 这是一个公共类
class PublicClass:
    def __init__(self, value):
        self.internal = _InternalClass(value)

    def show_value(self):
        print(f"The value is: {self.internal.get_value()}")

# 使用示例
if __name__ == "__main__":
    pub = PublicClass(42)
    pub.show_value()  # 输出: The value is: 42

    # 直接使用_InternalClass虽然可以，但不建议
    internal = _InternalClass(100)
    print(internal.get_value())  # 输出: 100