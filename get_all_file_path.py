import os

def get_all_file_paths(directory):
    """
    指定されたディレクトリ内のすべてのファイルのパスを再帰的に取得する関数
    """
    file_paths = []

    # ディレクトリを再帰的に探索
    for root, _, files in os.walk(directory):
        for file in files:
            # ファイルのフルパスを取得
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    
    return file_paths

