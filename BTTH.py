num_of_employees = int(input("Nhập số lượng nhân viên: "))

for i in range(num_of_employees):
    name = input("Nhập tên nhân viên: ")
    num_of_days = int(input("Nhập số ngày làm: "))

    if num_of_days < 0 or num_of_days > 22:
        print("Dữ liệu không hợp lệ.")
        continue

    if num_of_days == 0:
        print("Nhân viên nghỉ toàn bộ tháng.")
        continue

    print(name + ": ", end = "")
    for j in range(num_of_days):
        print("*", end = "")
    print()

    if num_of_days >= 18:
        print("Làm việc chăm chỉ")
    elif num_of_days < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")

    print()