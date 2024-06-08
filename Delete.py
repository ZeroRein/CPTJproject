import os

def delete_local_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted successfully.")
        else:
            print(f"{file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用例
file_path = 'path/to/your/file.txt'  # 削除したいファイルのパス
delete_local_file(file_path)