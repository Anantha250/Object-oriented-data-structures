

# ฟังก์ชัน Binary Search แบบเรียกใช้ซ้ำ (Recursive)
def bi_search(l, r, arr, x):
    # ตรวจสอบกรณีที่ขอบเขตซ้ายและขวาเท่ากัน
    if l == r:
        if arr[l] == x:
            return True  # พบค่า x ในอาร์เรย์
        else:
            return False  # ไม่พบค่า x ในอาร์เรย์
    # ตรวจสอบกรณีที่ขอบเขตซ้ายเกินขอบเขตขวา
    elif l > r:
        return False  # ไม่พบค่า x ในอาร์เรย์
    
    # คำนวณตำแหน่งกลางของขอบเขตปัจจุบัน
    mid = (l + r) // 2
    a = arr[mid]  # ดึงค่าที่ตำแหน่งกลาง
    
    # เปรียบเทียบค่าที่ตำแหน่งกลางกับ x
    if a > x:
        # ถ้าค่าในตำแหน่งกลางมากกว่า x ให้ค้นหาในครึ่งซ้าย
        return bi_search(l, mid, arr, x)
    elif a < x:
        # ถ้าค่าในตำแหน่งกลางน้อยกว่า x ให้ค้นหาในครึ่งขวา
        return bi_search(mid + 1, r, arr, x)
    elif a == x:
        return True  # พบค่า x ในอาร์เรย์
    
    return False  # กรณีอื่นๆ (ไม่ควรเกิดขึ้น)

# รับข้อมูลจากผู้ใช้ โดยแยกค่าจาก '/' 
inp = input('Enter Input : ').split('/')
# แยกข้อมูลส่วนแรกเป็นอาร์เรย์ของจำนวนเต็ม และส่วนที่สองเป็นค่าที่ต้องการค้นหา
arr, k = list(map(int, inp[0].split())), int(inp[1])
# เรียงอาร์เรย์ก่อนทำการค้นหา
sorted_arr = sorted(arr)
# เรียกใช้ฟังก์ชัน Binary Search เพื่อตรวจสอบว่ามีค่า k อยู่ในอาร์เรย์หรือไม่
result = bi_search(0, len(sorted_arr) - 1, sorted_arr, k)
# พิมพ์ผลลัพธ์ (True หรือ False)
print(result)

# Enter Input : 33 2 11 82 77 28 15 76 9 64/28
# True
