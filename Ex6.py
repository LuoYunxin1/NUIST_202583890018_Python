# Ex6.py
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# 输出全名
for name in studentNames:
    print(f"{name} Evans")

# 添加新姓名
new_name = input("please enter a new name：")
studentNames.append(new_name)

# 再次输出全名
print("the updated list：")
for name in studentNames:
    print(f"{name} Evans")
