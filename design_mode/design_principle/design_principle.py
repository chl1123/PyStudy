"""
封装变化的内容
design mode before: 税率计算和订单总额计算混在一起，税率硬编码
"""


def get_order_total0(order):
    total = 0
    for item in order:
        total += item["price"] * item["quantity"]

    if order.country == "USA":
        total -= total * 0.07  # USA营业税7%
    elif order.country == "EU":
        total -= total * 0.2  # 欧盟营业税20%

    return total


"""
design mode after: 税率计算和订单总额计算分开，调用指定方法获取税率
税率相关的修改被隔离在单个方法内。如果税率计算逻辑过于复杂，也能更方便地将其移动到独立的类中
"""


def get_order_total(order):
    total = 0
    for item in order["line_items"]:
        total += item["price"] * item["quantity"]

    total += total * get_tax_rate(order["country"])

    return total


def get_tax_rate(country):
    if country == "USA":
        return 0.07
    elif country == "EU":
        return 0.2


if __name__ == "__main__":
    order = {
        "line_items": [{"price": 50, "quantity": 1}, {"price": 20, "quantity": 2}],
        "country": "USA"
    }
    print(get_order_total(order))

    order["country"] = "EU"
    print(get_order_total(order))
