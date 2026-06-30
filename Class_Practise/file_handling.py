emp_list=["aman","shivam","shubham","anshu","kamal"]

for emp in emp_list:
    with open(f"{emp}.txt", "w") as file:
        pass
print("File created successfully.")