import os

# Đường dẫn đến thư mục chứa các tệp tin ảnh
folder_path = "E:/AIRC2024/CLIP_prefix_caption/data/coco/val"

# Lặp qua tất cả các tệp tin trong thư mục
for filename in os.listdir(folder_path):
    if filename.startswith("COCO_train2014"):
        # Tạo tên mới bằng cách thay thế phần đầu của tên tệp tin
        new_filename = filename.replace("COCO_train2014", "COCO_val2014")

        # Đường dẫn đến tệp tin gốc và tệp tin mới
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)

        # Đổi tên tệp tin
        os.rename(old_filepath, new_filepath)
