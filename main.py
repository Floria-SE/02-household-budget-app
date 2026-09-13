incomes = []
expenses = []
select_action = ""

def append_amount(type_, list_):
    try:
        name = input(f"何の{type_}ですか: ")
        amount = int(input("金額を入力してください: "))
        if amount < 1:
            print("1以上の金額を入力してください")
        else:
            list_.append({"name": name, "amount": amount})
    except ValueError:
        print("無効です。金額を入力してください")

def modify_amount(list_, type_): 
    if list_:
        print(f'現在の{type_}')
        for i, type_dict in enumerate(list_):
            print(f'{i}: {type_dict["name"]} {type_dict["amount"]}')

        try:
            index = int(input(f"訂正したい{type_}のインデックスを入力してください: "))
            new_key = input(f"新しい{type_}の項目名を入力してください: ")
            new_value = int(input(f"新しい{type_}の金額を入力してください: "))

            if 0 <= index < len(list_):
                if new_value <= 0:
                    print("\n1以上の金額を入力してください")
                else:
                    list_[index]["name"] = new_key
                    list_[index]["amount"] = new_value
                    print(f"\n{type_}が更新されました。")
            else:
                print("\n無効なインデックスです。")

        except ValueError:
            print("\n無効な入力です。数字を入力してください。")

    else:
        print(f"\n{type_}がまだ入力されていません。")


def sums(type_, list_):
    total = 0
    for type_dict in list_:
        print(f'{type_dict["name"]}: {type_dict["amount"]}')
        total += type_dict["amount"]
    print(f"\n{type_}合計: {total}\n")
    return total

while select_action != "5":
    print("\n1.収入を入力")
    print("2.支出を入力")
    print("3.家計簿を確認")
    print("4.入力を訂正")
    print("5.終了")

    select_action = input("1~5を選んでください: ")

    if select_action == "1":
        append_amount("収入", incomes)

    elif select_action == "2":
        append_amount("支出", expenses)

    elif select_action == "3":
        incomes_total = sums("収入", incomes)
        expenses_total = sums("支出", expenses)
        print(f"\n残高: {incomes_total - expenses_total}")
    
    elif select_action == "4":
        print("\n4. 入力を訂正")
        print(" 1. 収入を訂正")
        print(" 2. 支出を訂正")

        correction_action = input("1または2を選んでください: ")

        if correction_action == "1":
            modify_amount(incomes,"収入")

        elif correction_action == "2":
            modify_amount(expenses,"支出")

        else:
            print("\n無効な選択です。1または2を入力してください。")       
    
    elif select_action == "5":
        print("\n5. 終了")

    else:
        print("\n無効な選択です。1~5の数字を入力してください。")