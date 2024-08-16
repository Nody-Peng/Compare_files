import os
import tkinter as tk
from tkinter import filedialog, messagebox

def compare_and_remove_unmatched_files(folder_1, folder_2):
    folder_1_files = {os.path.splitext(f)[0] for f in os.listdir(folder_1) if os.path.isfile(os.path.join(folder_1, f))}

    for file_name in os.listdir(folder_2):
        file_path = os.path.join(folder_2, file_name)
        if os.path.isfile(file_path):
            file_name_without_ext = os.path.splitext(file_name)[0]
            if file_name_without_ext not in folder_1_files:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"Kept: {file_path}")

    messagebox.showinfo("完成", "檔案比對與刪除已完成！")

def select_folder_1():
    folder = filedialog.askdirectory()
    folder_1_entry.delete(0, tk.END)
    folder_1_entry.insert(0, folder)

def select_folder_2():
    folder = filedialog.askdirectory()
    folder_2_entry.delete(0, tk.END)
    folder_2_entry.insert(0, folder)

def run_compare():
    folder_1 = folder_1_entry.get()
    folder_2 = folder_2_entry.get()

    if not folder_1 or not folder_2:
        messagebox.showerror("錯誤", "請選擇兩個資料夾路徑！")
        return

    compare_and_remove_unmatched_files(folder_1, folder_2)

# 建立主視窗
root = tk.Tk()
root.title("檔案比對與刪除工具")
root.geometry("900x200")  # 調整視窗寬度，防止元件被擋住
root.resizable(False, False)  # 禁用視窗大小調整
root.configure(bg="#f0f0f0")

# 設定字體
label_font = ("Arial", 12)
button_font = ("Arial", 10, "bold")

# 設定框架 (Frame) 來整理佈局
frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
frame.pack(fill="both", expand=True)

# 新增說明文字和資料夾選擇的輸入框
tk.Label(frame, text="請選擇要比對的主要資料夾 (folder_1)：", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=10, sticky="w")
folder_1_entry = tk.Entry(frame, width=50, font=("Arial", 10))  # 增加輸入框的寬度
folder_1_entry.grid(row=0, column=1, padx=5, pady=10)
folder_1_button = tk.Button(frame, text="選擇資料夾", command=select_folder_1, font=button_font, bg="#4CAF50", fg="white")
folder_1_button.grid(row=0, column=2, padx=5, pady=10)

tk.Label(frame, text="請選擇要進行比對與刪除檔案的資料夾 (folder_2)：", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=10, sticky="w")
folder_2_entry = tk.Entry(frame, width=50, font=("Arial", 10))  # 增加輸入框的寬度
folder_2_entry.grid(row=1, column=1, padx=5, pady=10)
folder_2_button = tk.Button(frame, text="選擇資料夾", command=select_folder_2, font=button_font, bg="#4CAF50", fg="white")
folder_2_button.grid(row=1, column=2, padx=5, pady=10)

# 建立執行按鈕
run_button = tk.Button(frame, text="開始比對與刪除", command=run_compare, font=button_font, bg="#2196F3", fg="white", padx=10, pady=5)
run_button.grid(row=2, column=1, padx=5, pady=20)

# 啟動 GUI 主迴圈
root.mainloop()
