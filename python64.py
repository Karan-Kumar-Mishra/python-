class student:
    def __init__(self):
        print("constructor is call")
    def info(self):
        return f"name=>{self.name}.Salary is {self.std} and role is {self.section}"
karan=student()
mishra=student()

karan.name="karan"
karan.std=12
karan.section=1
mishra.name="mishar"
mishra.std=12
mishra.section=1
print(karan.name)
print(karan.std)
print(karan.section)
print(mishra.name)
print(mishra.std)
print(mishra.section)
print(karan.__dict__)
print("info => ",karan.info())

