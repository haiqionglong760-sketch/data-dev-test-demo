
# 模拟数据处理函数
def process_test_data():
    # 初始逻辑：仅打印提示
    print("开始处理自测数据...")
    # 模拟返回测试数据
    test_data = {"id": 1, "value": 100}
    # 新增：数据校验
    if test_data["value"] < 0:
        raise ValueError("自测数据value不能为负数")
    return test_data

# 执行函数
if __name__ == "__main__":
    result = process_test_data()
    print("处理结果：", result)

# 保存文件，这一步就模拟了你「修改 / 编写代码」的操作。

# 修改data_process.py（比如新增数据校验逻辑） 
    

