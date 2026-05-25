from playwright.sync_api import sync_playwright
import time

def automate_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        print("جاري الدخول للموقع...")
        page.goto("https://www.lynkco.com/en/create-account")
        
        # الانتظار حتى تظهر خانة الاسم قبل الكتابة فيها
        # هذا يحل مشكلة أن الموقع "لا يفعل شيئاً"
        page.wait_for_selector('input[placeholder="First name"]', timeout=30000)
        
        print("تم تحميل الصفحة، جاري الكتابة...")
        
        # الكتابة ببطء (حرفاً حرفاً) لجعل البرنامج يبدو مثل البشر
        page.get_by_placeholder("First name").type("Mohamed", delay=100)
        page.get_by_placeholder("Last name").type("Magdy", delay=100)
        page.get_by_placeholder("Phone number").type("01012345678", delay=100)
        page.get_by_placeholder("Email").fill("your_email@example.com")
        
        print("تم كتابة البيانات، أنتظر 60 ثانية...")
        time.sleep(60) 
        
        page.get_by_placeholder("Password").fill("StrongPassword123!")
        
        # إذا واجهت مشكلة في الضغط على الموافقة، جرب استخدام التحديد حسب الدور
        page.get_by_label("I confirm that I am 18 years or older").click()
        
        print("تمت العملية.")
        input("اضغط Enter للإغلاق...")
        browser.close()

if __name__ == "__main__":
    automate_form()