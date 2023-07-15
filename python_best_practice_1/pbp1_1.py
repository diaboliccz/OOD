# #  *** BMI ***
# # Enter your weight(kg) and height(m) : 48 1.68
# # Your status is : Below normal weight.

# จงคำนวณค่า BMI โดยมีสูตรการคำนวณดังนี้

# BMI = น้ำหนักหน่วย (kg) / ( ความสูงหน่วย (m) * ความสูงหน่วย (m))

# โดยมีเกณฑ์ดังต่อไปนี้

# ค่า                             สถานะ

# BMI < 18.5               Below normal weight

# 18.5 <= BMI < 25     Normal weight

# 25 <= BMI < 30        Overweight

# 30 <= BMI < 35        Case I Obesity

# 35 <= BMI < 40        Case II Obesity

# BMI >= 40                Case III Obesity

# โดยให้แสดงผลลัพธดังตัวอย่าง
print(" *** BMI ***")
value = input("Enter your weight(kg) and height(m) : ").split()
weight = float(value[0])
height = float(value[1])

bmi = weight / (height * height)
if bmi < 18.5:
    print("Your status is : Below normal weight.")
elif bmi < 25:
    print("Your status is : Normal weight.")
elif bmi < 30:
    print("Your status is : Overweight.")
elif bmi < 35:
    print("Your status is : Case I Obesity.")
elif bmi < 40:
    print("Your status is : Case II Obesity.")
else:
    print("Your status is : Case III Obesity.")