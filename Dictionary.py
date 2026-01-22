marks = {}
x = int(input("Enter  marks of phy:"))
marks.update({"phy":x})
x = int(input("Enter marks of math:"))
marks.update({"maths":x})
x = int(input("Enter the marks of chem:"))
marks.update({"chem":x})
print(marks)