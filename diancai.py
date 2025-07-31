menu = {
    "宫保鸡丁": 28,
    "鱼香肉丝": 25,
    "麻婆豆腐": 18,
    "回锅肉": 32
}
order_list = {}


def order_dishes():
    dish_name = input("请输入要点的菜名（输入 q 结束点菜）：")
    while dish_name != 'q':
        if dish_name in menu:
            num = int(input("请输入该菜的数量："))
            order_list[dish_name] = order_list.get(dish_name, 0) + num
            print(f"{dish_name} 已点 {num} 份")
        else:
            print("抱歉，菜单中无此菜品，请重新输入")
        dish_name = input("请输入要点的菜名（输入 q 结束点菜）：")


def back_dishes():
    dish_name = input("请输入要退的菜名：")
    if dish_name in order_list:
        num = int(input("请输入要退的数量："))
        if num <= order_list[dish_name]:
            order_list[dish_name] -= num
            if order_list[dish_name] == 0:
                del order_list[dish_name]
            print(f"成功退掉 {num} 份 {dish_name}")
        else:
            print("退菜数量不能超过已点数量")
    else:
        print("您未点过该菜品")


def sum_dishes():
    total_price = sum(menu[dish] * num for dish, num in order_list.items())
    print("\n===== 点单详情 =====")
    for dish, num in order_list.items():
        print(f"{dish}：{num} 份，单价 {menu[dish]} 元，小计 {menu[dish] * num} 元")
    print(f"总价：{total_price} 元")
    discount = float(input("请输入折扣率（如 0.8 表示 8 折）："))
    actual_pay = total_price * discount
    print(f"实付金额：{actual_pay} 元")


def main():
    print("===== 欢迎使用点菜系统 =====")
    while True:
        print("\n请选择操作：")
        print("1. 点菜")
        print("2. 退菜")
        print("3. 结账")
        print("4. 退出")
        choice = input("请输入操作序号：")
        if choice == '1':
            order_dishes()
        elif choice == '2':
            back_dishes()
        elif choice == '3':
            sum_dishes()
            break  # 结账后退出系统
        elif choice == '4':
            print("退出系统，欢迎下次光临！")
            break
        else:
            print("无效操作，请重新选择")

if __name__ == "__main__":
    main()