import datetime
import tkinter as tk

# 새 창 만들기
root = tk.Tk()

# 새 창에서 날짜 입력 받기
def get_date():
    # 새 창 생성
    date_window = tk.Toplevel(root)
    date_window.title("날짜 입력")
    
    # 라벨 생성
    label = tk.Label(date_window, text="날짜를 입력하세요 (YYYY, MM, DD 순서대로 입력)")
    label.pack(pady=10)

    # 입력 필드 생성
    year_entry = tk.Entry(date_window)
    year_entry.pack()
    month_entry = tk.Entry(date_window)
    month_entry.pack()
    day_entry = tk.Entry(date_window)
    day_entry.pack()

    # 확인 버튼 생성
    def submit_date():
        # 입력 받은 날짜로 D-day 설정
        year = int(year_entry.get())
        month = int(month_entry.get())
        day = int(day_entry.get())
        global d_day
        d_day = datetime.datetime(year, month, day)
        # 새 창 닫기
        date_window.destroy()

        # 메인 창에서 D-day 출력 함수 호출
        print_d_day()

    submit_button = tk.Button(date_window, text="확인", command=submit_date)
    submit_button.pack(pady=10)

# 메인 창에서 날짜 입력 버튼 생성
date_button = tk.Button(root, text="날짜 입력", command=get_date)
date_button.pack(pady=20,side= "bottom")

# 이미지 불러오기
image = tk.PhotoImage(file="haha.png")

# 이미지 라벨 생성
image_label = tk.Label(root, image=image)
image_label.pack()

# 디데이 설정 (YYYY, MM, DD 순서대로 입력)
d_day = datetime.datetime(2023, 5, 12)

# 디데이까지 남은 일 수 계산
days_left = (d_day - datetime.datetime.now()).days

# 디데이 출력 함수
def print_d_day():
    # 현재 시각 계산
    now = datetime.datetime.now()
    # 디데이까지 남은 일 수 계산
    days_left = (d_day - now).days
    # 라벨에 출력
    d_day_label.config(text="D - {}".format(days_left),font=("Helvetica", 60))
    # 1초마다 반복 호출
    d_day_label.after(1000, print_d_day)

# 라벨 생성
d_day_label = tk.Label(root, font=("Helvetica", 30), pady=20)
d_day_label.pack()

# 디데이 출력 함수 호출
print_d_day()

# 종료 시각 설정 (시간과 분은 자유롭게 변경 가능)
end_time = d_day.replace(hour=23, minute=59, second=59)

# 남은 시간 계산
remaining_time = end_time - datetime.datetime.now()

# 남은 시간을 시간, 분, 초로 나누기
hours, remainder = divmod(remaining_time.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# 남은 시간과 일 수를 출력하는 함수
def print_remaining_time():
    # 현재 시각 계산
    now = datetime.datetime.now()
    # 남은 시간 계산
    remaining_time = end_time - now
    # 남은 시간을 시간, 분, 초로 나누기
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # 디데이까지 남은 일 수 계산
    days_left = (d_day - now).days
    # 라벨에 출력
    remaining_time_label.config(text="남은 시간: {}시간 {}분 {}초 남았습니다.".format(hours, minutes, seconds, ),font =("Verdana",20))
    # 1초마다 반복 호출
    remaining_time_label.after(1000, print_remaining_time)

# 라벨 생성
remaining_time_label = tk.Label(root, font=("Helvetica", 20), pady=20)
remaining_time_label.pack()

# 남은 시간 출력 함수 호출
print_remaining_time()

# 창 실행
root.mainloop()