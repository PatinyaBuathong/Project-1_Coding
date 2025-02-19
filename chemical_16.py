def calculate_chemical():
    print("โปรแกรมคำนวณความเข้มข้นของสารละลาย")
    print("1.weight/volume (g/L)")
    print("2.weight/weight (% w/w)")
    print("3.molar (M)")
    choice = input("กรุณาเลือกชนิดคำนวณ (1-3): ")
    if choice == "1" :
        w = float(input("กรอกน้ำหนักตัวละลาย (g): "))
        v = float(input("กรอกปริมาณสารละลาย (L)"))
        c = (w*100)/v
        print(f"สารละลายนี้ความเข้มข้น:{c:.2f} g/L")
    elif choice == "2" :
        w1 = float(input("กรอกน้ำหนักตะวละลาย (g): "))
        w2 = float(input("กรอกน้ำหนักของสารละลาย (g): "))
        c = (w1*100)/w2
        print(f"สารละลายนี้มีความเข้มข้น:{c:.2f} g")
    elif choice == "3" :
        m = float(input("กรอกจำนวนโมลตัวละลาย (mol): "))
        v = float(input("กรอกปริมาตรสารละลาย (L: )"))
        c = m/v
        print(f"สารละลายนี้มีความเข้มข้น:{c:.2f} mol/g")
    else :
        print("ตัวเลือกไม่ถูกต้อง")
def main():
    for _ in range(3):  
        calculate_chemical()
        repeat = input("\nต้องการคำนวณอีกครั้งหรือไม่? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Thank you for use my program!❤")
            break
if __name__ == "__main__":
    main()