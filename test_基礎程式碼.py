import os

def compare_and_remove_unmatched_files(folder_1, folder_2):
    # 取得 folder_1 所有檔案名稱（不包含副檔名）
    folder_1_files = {os.path.splitext(f)[0] for f in os.listdir(folder_1) if os.path.isfile(os.path.join(folder_1, f))}

    # 遍歷 folder_2 中的檔案
    for file_name in os.listdir(folder_2):
        file_path = os.path.join(folder_2, file_name)
        if os.path.isfile(file_path):
            # 比對檔名（忽略副檔名）
            file_name_without_ext = os.path.splitext(file_name)[0]
            if file_name_without_ext not in folder_1_files:
                # 如果檔名不在 folder_1 中，刪除該檔案
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"Kept: {file_path}")

# 指定資料夾路徑
folder_1 = './folder_1'
folder_2 = './folder_2'

# 執行比對與刪除操作
compare_and_remove_unmatched_files(folder_1, folder_2)
