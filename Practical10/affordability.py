def buy_house(salary, price):
    """
    input:
    salary - the	purchaser’s	 annual	 salary
    price -  the total value of the	house
    if 5*salary >= price , return true
    otherwise, return false
    """
    if 5*salary >= price:
        print("Yes")
    else:
        print("No")
# an example
buy_house(10000, 999)
#Yes
