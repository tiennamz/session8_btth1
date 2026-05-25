menu = '''

+=================================================+
|        HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK         |
+=================================================+
|  1. Nhập và phân tích thông tin video           |
|  2. Chuẩn hóa tên tài khoản                     |
|  3. Kiểm tra tính hợp lệ của hashtag            |
|  4. Tìm kiếm và thay thế từ khóa trong mô tả    |
|  5. Thoát chương trình                          |
+=================================================+
'''
while True:
    print(menu)
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Vui lòng nhập số nguyên")
        continue
    match choice:
        case 1:
            while True:
                user_name = input("Tên tài khoản người đăng video: ").strip()
                if user_name.strip() == "":
                    print("Tên tài khoản không được rỗng")
                else:
                    break
            video_title = input("Tiêu đề video: ").strip().title()
            while True:
                depcription = input("Mô tả video: ").strip()
                if depcription.strip() == "":
                    print("Mô tả không được rỗng")
                else:
                    break
            hashtags = input("Danh sách hashtag, cách nhau bởi dấu phẩy: ")
            list_hashtag = hashtags.split(",")
            list_temp = []
            for hashtag in list_hashtag:
                hashtag = hashtag.strip()
                list_temp.append(hashtag)
            list_hashtag = ", ".join(list_temp) 
            
            print()
            print("=" * 50)
            print(f"Tên tài khoản: {user_name}")
            print(f"Tiêu đề: {video_title}")
            print(f"Mô tả: {depcription.capitalize()}")
            print(f"Độ dài mô tả video: {len(depcription)} ký tự")
            print(f"Số lượng từ trong mô tả video: {len(depcription.split(" "))} từ")
            print(f"Danh sách hashtag: {list_hashtag}")
            print(f"Số lượng hashtag: {len(list_hashtag.split(" "))}")
            print(f"Mô tả video được chuyển toàn bộ sang chữ thường: {depcription.lower()}")
            print(f"Mô tả video được chuyển toàn bộ sang chữ hoa: {depcription.upper()}")
            print("=" * 50)
            
        case 2: 
            print(f"Tên tài khoản ban đầu: {user_name}")
            print(f"Tên tài khoản sau khi được chuẩn hoá: {"@" + user_name.lower()}")
        
        case 3:
            input_hashtag = input("Hãy nhập một hashtag: ")
            is_true = False
            if input_hashtag.strip() == "":
                print("Hashtag trống")
            elif not input_hashtag.startswith("#"):
                print("Hashtag phải bắt đầu bằng #")
            elif len(input_hashtag) < 2:
                print("Hashtag quá ngắn")
            elif not input_hashtag[1:].replace("_","").isalnum():
                print("Hashtag chỉ nên sử dụng chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #")
            else:
                list_hashtag += ", " + input_hashtag
                is_true = True
            
            if is_true == True:
                print(f"Đã thêm hashtag {input_hashtag} thành công!")
                print(list_hashtag)
                
        case 4:
            keyword_search = input("Từ khóa cần tìm: ")
            keyword_replace = input("Từ khóa thay thế: ")
            
            count_keyword = 0
            
            for word in depcription.split(" "):
                if word == keyword_search:
                    count_keyword += 1
            
            if count_keyword > 0:
                depcription = depcription.replace(keyword_search, keyword_replace)
                print("Đã thay đổi mô tả")
                print(depcription)
            else:
                print(f"Không tìm thấy {keyword_search} trong mô tả")
            
        case 5: 
            print("Thoát chương trình")
            break
        
        case _:
            print("Hãy nhập từ 1-5!!!!!")