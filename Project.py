import json
import sys

# قائمة لتخزين جهات الاتصال
contacts = {}

def show_menu():
    print("\n=== نظام إدارة جهات الاتصال ===")
    print("1. إضافة جهة اتصال جديدة")
    print("2. عرض جميع جهات الاتصال")
    print("3. البحث عن اسم")
    print("4. الخروج")

def add_contact():
    name = input("ادخل الاسم: ").strip().capitalize()
    phone = input("ادخل رقم الهاتف: ").strip()
    
    if name and phone:
        contacts[name] = phone
        print(f"تم حفظ جهة الاتصال لـ {name} بنجاح!")
    else:
        print("خطأ: يرجى إدخال بيانات صحيحة.")

def view_contacts():
    if not contacts:
        print("لا توجد جهات اتصال مسجلة حالياً.")
    else:
        print("\n--- قائمة جهات الاتصال ---")
        for name, phone in contacts.items():
            print(f"الاسم: {name} | الهاتف: {phone}")

def main():
    while True:
        show_menu()
        choice = input("اختر من القائمة (1-4): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_name = input("ادخل الاسم للبحث: ").strip().capitalize()
            if search_name in contacts:
                print(f"رقم هاتف {search_name} هو: {contacts[search_name]}")
            else:
                print("الاسم غير موجود.")
        elif choice == "4":
            print("شكراً لاستخدامك البرنامج. وداعاً!")
            sys.exit()
        else:
            print("خيار غير صحيح، حاول مرة أخرى.")

if __name__ == "__main__":
    main()
