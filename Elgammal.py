import random
import os
from hashlib import sha256
import tkinter as tk
from tkinter import messagebox
import math
import tkinter.filedialog as filedialog

# --- Phần toán học và xử lý logic ---
# Sinh số ngẫu nhiên
def generate_large_prime(start, end):
    while True:
        prime = random.randint(start, end) #n
        if miller_rabin(prime): #check số nto n
            return prime
        
# Tìm phần tử sinh g
def find_generator(p):
    for g in range(2, p):
        if pow(g, (p - 1), p) == 1: 
            return g  
    raise ValueError("Không tìm thấy phần tử sinh")  

def miller_rabin(n, k=10):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Viết n-1 = 2^r * d với d lẻ
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    # Thực hiện k lần kiểm tra với các giá trị ngẫu nhiên a
    for _ in range(k):
        # Chọn ngẫu nhiên a từ 2 đến n-2
        a = random.randint(2, n-2) #lấy a=2,3,5,7,11,13
        # Tính a^d % n
        x = modular_exponentiation(a, d, n)
        # Nếu x == 1 hoặc x == n-1, tiếp tục với lần kiểm tra tiếp theo
        if x == 1 or x == n - 1:
            continue
        # Kiểm tra nếu x^2, x^4, ..., x^(2^(r-1)) có bằng n-1 không
        for _ in range(r - 1):
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Tạo p và g
def generate_parameters():
    while True:
        p = generate_large_prime(10000000, 30000000) 
        #k = random.randint(2, 10)
        g = find_generator(p)  # tìm căn nguyên thủy g 
        if g:
            break
    return p, g

# Hàm lũy thừa a^n % p
def modular_exponentiation(base, exp, mod): 
    if exp == 0:
        return 1
    y = modular_exponentiation(base, exp // 2, mod)
    if exp % 2 == 0:
        return (y * y) % mod #p=p*p
    else:
        return (y * y * base) % mod #p=p*x

# Hàm tính UCLN gcd(a,b)=1  gcd(5,3) r=2 a=3 b=2 r=3%2=1 a=2 b=1  r=2%1=0 a=1 b=0
def gcd(a, b): 
    while True:
        if a == 0:
            return b
        if b == 0:
            return a #trả về 1
        r = a % b
        a = b
        b = r

# Hàm tìm modulo nghịch đảo THEO OCLIT mở rộng
def mod_inverse(a, m): #tính a^-1
    m0 = m
    x = 0
    y = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x
        x = y - q * x
        y = t
    if y < 0:
        y += m0
    return y

# Hàm sinh khóa
def generate_keys(p, g):
    private_key = random.randint(1, p - 1) # sinh ngẫu nhiên
    public_key = modular_exponentiation(g, private_key, p) #Tính khóa công khai yA = g^xA mod p
    return private_key, public_key

# hàm sinh chữ ký
def sign_file(p, g, private_key, file_content):
    h = int.from_bytes(sha256(file_content.encode('utf-8')).digest(), byteorder='big') % p #pthon a34asfsfds 34 chuỗi sẽ được đọc từ trái sang phải (Big Endian), tức là byte có trọng số cao nhất sẽ xuất hiện đầu tiên.
    k = random.randint(1, p-2)
    while gcd(k, p-1) != 1:
        k = random.randint(1, p-2)
    r = modular_exponentiation(g, k, p) #S1 = g^K mod p
    s = (mod_inverse(k, p-1) * (h - private_key * r)) % (p-1) #S2 = K^(-1) * (h - xA * S1) mod (p-1)
    return r, s

#  hàm kiểm tra chữ ký
def verify_signature(p, g, public_key, file_content, r, s):
    if not (0 < r < p and 0 < s < p-1):
        return False
    h = int.from_bytes(sha256(file_content.encode('utf-8')).digest(), byteorder='big') % p #c++ ád82ee2 24
    x1 = modular_exponentiation(g, h, p) #v1 = g^h mod p
    x2 = (modular_exponentiation(public_key, r, p) * modular_exponentiation(r, s, p)) % p #v2 = (yA^S1) * (S1^S2) mod p
    return x1 == x2

# --- Giao diện Tkinter ---
class ElGamalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ElGamal Digital Signature")
        self.p = None
        self.g = None
        self.private_key = None
        self.public_key = None
        self.file_to_sign = None
        self.received_file = None
        self.received_signature = None
        #thiết lập giao diện
        self.setup_ui()
        
    def setup_ui(self):
        frame_left = tk.LabelFrame(self.root, text="Ký văn bản")
        frame_left.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

        tk.Button(frame_left, text="Tạo tham số và sinh khóa", command=self.generate_parameters).pack(pady=2)
        self.entry_p = tk.Entry(frame_left, width=40)
        self.entry_g = tk.Entry(frame_left, width=40)
        self.entry_private = tk.Entry(frame_left, show="*", width=40)
        self.entry_public = tk.Entry(frame_left, width=40)

        file_frame = tk.Frame(frame_left)
        file_frame.pack(pady=2)

        tk.Button(file_frame, text="Chọn file", command=self.select_file).pack(side=tk.LEFT, padx=5)
        self.lbl_file = tk.Label(file_frame, text="Chưa chọn file")
        self.lbl_file.pack(side=tk.LEFT, padx=5)

        tk.Label(frame_left, text="Nội dung văn bản(người gửi):").pack()
        self.text_content = tk.Text(frame_left, height=10, width=50)
        self.text_content.pack(pady=2)

        tk.Button(frame_left, text="Lưu văn bản", command=self.save_file).pack(pady=2)

        tk.Label(frame_left, text=" Tạo chữ ký số:").pack()
        self.text_signature = tk.Entry(frame_left, width=50, show="*")
        self.text_signature.pack(pady=2)
        
        self.show_signature = tk.IntVar()
        tk.Checkbutton(frame_left, text="Hiển thị", variable=self.show_signature, command=self.toggle_signature).pack()

        button_frame = tk.Frame(frame_left)
        button_frame.pack(pady=2)

        tk.Button(button_frame, text="Ký", command=self.sign_file).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Gửi", command=self.send_to_verify).pack(side=tk.LEFT, padx=5)

        #frame right
        frame_right = tk.LabelFrame(self.root, text="Kiểm tra chữ ký")
        frame_right.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")

        file_frame = tk.Frame(frame_right)
        file_frame.pack(pady=2)
        tk.Button(file_frame, text=" File văn bản", command=self.select_verify_file).pack(side=tk.LEFT, padx=5)
        self.lbl_received_file = tk.Label(file_frame, text="Chưa có file")
        self.lbl_received_file.pack(side=tk.LEFT, padx=5)

        tk.Label(frame_right, text="Nội dung văn bản(người nhận):").pack()
        self.text_received_content = tk.Text(frame_right, height=10, width=50)
        self.text_received_content.pack(pady=2)

        tk.Button(frame_right, text="Lưu văn bản", command=self.save_file).pack(pady=2)

        #tạo chữ ký
        file_signature_frame = tk.Frame(frame_right)
        file_signature_frame.pack(pady=2)
        self.lbl_sig_file = tk.Label(file_signature_frame, text="Chưa có file chữ ký")

        tk.Label(frame_right, text="Cặp chữ ký số :").pack()
        self.text_signature_verify = tk.Text(frame_right, height=1, width=50)
        self.text_signature_verify.pack(pady=2)

        tk.Button(frame_right, text="Xác minh", command=self.verify_signature).pack(pady=2)
        self.lbl_verify_result = tk.Label(frame_right, text="Kết quả: ")
        self.lbl_verify_result.pack(pady=2)

    def generate_parameters(self):
        try:
            self.p, self.g = generate_parameters()
            self.entry_p.delete(0, tk.END)
            self.entry_p.insert(0, str(self.p))
            self.entry_g.delete(0, tk.END)
            self.entry_g.insert(0, str(self.g))
            if self.p is None or self.g is None:
                raise ValueError("Vui lòng tạo tham số p và g trước khi sinh khóa")
            p = int(self.entry_p.get())
            g = int(self.entry_g.get())
            self.private_key, self.public_key = generate_keys(p, g)
            self.entry_private.delete(0, tk.END)
            self.entry_private.insert(0, str(self.private_key))
            self.entry_public.delete(0, tk.END)
            self.entry_public.insert(0, str(self.public_key))
            messagebox.showinfo("Thành công", "Đã sinh số thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    #hàm ẩn hiện chữ ký
    def toggle_signature(self):
        if self.show_signature.get():
            self.text_signature.config(show="")
        else:
            self.text_signature.config(show="*")

    def select_file(self):
        self.file_to_sign = filedialog.askopenfilename()
        if self.file_to_sign:
            self.lbl_file.config(text=os.path.basename(self.file_to_sign))
            with open(self.file_to_sign, 'r', encoding='utf-8') as f:
                content = f.read()
                self.text_content.delete(1.0, tk.END)
                self.text_content.insert(tk.END, content)

    def save_file(self):
        if self.file_to_sign:
            with open(self.file_to_sign, 'w', encoding='utf-8') as f:
                f.write(self.text_content.get(1.0, tk.END).strip())
            messagebox.showinfo("Thành công", "Đã lưu nội dung file thành công!")

    def sign_file(self):
        try:
            if not self.file_to_sign:
                raise ValueError("Vui lòng chọn file cần ký")
            file_content = self.text_content.get(1.0, tk.END).strip()
            r, s = sign_file(self.p, self.g, self.private_key, file_content)
            sig = f"{r},{s}"
            self.text_signature.delete(0, tk.END)
            self.text_signature.insert(0, sig)
            with open(self.file_to_sign + ".sig", 'w') as f:
                f.write(sig)
            messagebox.showinfo("Thành công", "Đã ký file thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # hàm gửi file văn bản và file chũ ý
    def send_to_verify(self):
        try:
            if not self.file_to_sign:
                raise ValueError("Vui lòng chọn file cần gửi")
            with open(self.file_to_sign, 'r', encoding='utf-8') as f:
                content = f.read()
            self.lbl_received_file.config(text=os.path.basename(self.file_to_sign))
            self.text_received_content.delete(1.0, tk.END)
            self.text_received_content.insert(tk.END, content)
            self.received_file = self.file_to_sign
            with open(self.file_to_sign + ".sig", 'r', encoding='utf-8') as f:
                self.received_signature = f.read()
            self.lbl_sig_file.config(text=os.path.basename(self.file_to_sign + ".sig"))
            self.text_signature_verify.delete(1.0, tk.END)
            self.text_signature_verify.insert(tk.END, self.received_signature)
            messagebox.showinfo("Thành công", "Đã gửi file thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    # hàm xác minh chữ ký
    def verify_signature(self):
        try:
            if not self.received_file:
                raise ValueError("Vui lòng chọn file cần xác minh")
            if not self.received_signature:
                raise FileNotFoundError("Không tìm thấy file chữ ký tương ứng")
            r, s = map(int, self.text_signature_verify.get(1.0, tk.END).strip().split(','))
            file_content = self.text_received_content.get(1.0, tk.END).strip()
            is_valid = verify_signature(self.p, self.g, self.public_key, file_content, r, s)
            if is_valid:
                self.lbl_verify_result.config(text="Kết quả: Hợp lệ (Dữ liệu không bị thay đổi)", fg="green")
            else:
                self.lbl_verify_result.config(text="Kết quả: Không hợp lệ (Dữ liệu đã bị sửa đổi)", fg="red")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def select_verify_file(self):
        self.received_file = filedialog.askopenfilename()
        if self.received_file:
            self.lbl_received_file.config(text=os.path.basename(self.received_file))
            with open(self.received_file, 'r', encoding='utf-8') as f:
                content = f.read()
                self.text_received_content.delete(1.0, tk.END)
                self.text_received_content.insert(tk.END, content)

    def select_verify_file_sig(self):
        self.received_signature = filedialog.askopenfilename()
        if self.received_signature:
            self.lbl_sig_file.config(text=os.path.basename(self.received_signature))
            with open(self.received_signature, 'r', encoding='utf-8') as f:
                sig_content = f.read()
                self.text_signature_verify.delete(1.0, tk.END)
                self.text_signature_verify.insert(tk.END, sig_content)

# --- Main program ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ElGamalApp(root)
    root.mainloop()
