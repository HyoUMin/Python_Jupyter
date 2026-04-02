# To Do List

# 전체 리스트 확인하기
# 주별 리스트 확인하기
# 날짜별 리스트 확인하기
# 리스트 추가 하기
# 기존 리스트 삭제하기
# 기존 리스트 수정하기
# ==========================

from datetime import datetime, timedelta

todo_list = []

# 투두리스트 입력 
def add_task():
    date_str = input("날짜를 입력하세요(예: 2026-04-02)")
    todo = input("할 일을 입력하세요:")

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    todo_list.append({"detail": todo, "date": date_obj})

    print("할 일이 추가되었습니다.")

# 저장된 투두리스트 모두 출력
def view_all():
    print("==== 전체 할 일 목록 ====")

    if len(todo_list) == 0:
        print("저장된 할 일이 없습니다.")
        return
    for task in todo_list:
        date_str = task["date"].strftime("%Y-%m-%d")
        print(f"날짜: {date_str}\n할 일 : {task['detail']}")

# 조회하고 싶은 날짜의 투두리스트 출력
def view_daily():
    date_str = input("조회하고 싶은 날짜를 입력하세요(예: 2026-04-02):")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
    print(f"\n==== {date_str} 할 일 목록 ====")
    
    count = 0

    for task in todo_list:
        if date_obj == task["date"]:
            print(f" 날짜: {task['date'].strftime('%Y-%m-%d')}\n 할 일: {task['detail']}")
            count += 1
    
    if count == 0:
        print("해당 날짜는 등록되지 않았습니다.")

# 조회하고 싶은 날짜 기준으로 월 ~ 일 투두리스트 출력
def view_weekly():
    today_str = input("조회하고 싶은 날짜를 입력하세요(예: 2026-04-02):")
    today_obj = datetime.strptime(today_str, "%Y-%m-%d")

    start_of_week = today_obj - timedelta(days=today_obj.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    print(f"\n==== {start_of_week.strftime('%Y-%m-%d')} ~ {end_of_week.strftime('%Y-%m-%d')} 주간 일정 ====")
    
    count = 0

    for task in todo_list:
        if start_of_week <= task["date"] <= end_of_week:
            print(f" 날짜: {task['date'].strftime('%Y-%m-%d')}\n 할 일: {task['detail']}")
            count += 1
    
    if count == 0:
        print("해당 주간에는 등록된 일정이 없습니다.")

# 투두리스트 수정 - 1. 수정하고 싶은 날짜 선택 2. 수정하고 싶은 내용 선택 3. 내용 수정
def edit_task():
    edit_date = input(" 수정하고 싶은 날짜를 입력하세요(예: 2026-04-02):")
    edit_obj = datetime.strptime(edit_date, "%Y-%m-%d")

    print(f"\n==== 할 일 목록 수정 ====")
    matches = []

    for task in todo_list:
        if edit_obj == task["date"]:
            matches.append(task)
    
    if len(matches) == 0:
            print("해당 날짜에 등록된 할 일이 없습니다.")
            return
    
    print(f"\n==== {edit_date} 검색 결과 ====")
    for i, task in enumerate(matches, 1):
        print(f"{i}. 할 일: {task['detail']}")


    change = int(input("\n수정할 항목의 번호를 입력하세요: ")) - 1
    if 0 <= change < len(matches):     
        new_todo = input("새로운 할 일을 입력하세요: ")
        matches[change]["detail"] = new_todo
        print("수정이 완료되었습니다.")
    else:
        print("잘못된 번호입니다.")


# 투두리스트 삭제 - 1. 삭제하고 싶은 날짜 선택 2. 삭제하고 싶은 내용 선택 3. 내용 삭제 
def delete_task():
    del_date = input("삭제하고 싶은 날짜를 입력하세요(예: 2026-04-02):")
    del_obj = datetime.strptime(del_date, "%Y-%m-%d")
    print(f"\n==== 할 일 목록 삭제 ====")
    
    matches = []
    for task in todo_list:
        if del_obj == task["date"]:
            matches.append(task)

    if not matches:
        print("해당 날짜는 등록되지 않았습니다.")
        return
    
    print(f"\n==== {del_date} 검색 결과 ====")
    for i, task in enumerate(matches, 1):
        print(f"{i}. 할 일: {task['detail']}")


    change = int(input("\n삭제할 항목의 번호를 입력하세요: ")) - 1
    if 0 <= change < len(matches):     
        target_task = matches[change]
        todo_list.remove(target_task)
        print(f"'{target_task['detail']}' 항목이 삭제되었습니다.")
    else:
            print("잘못된 번호입니다.")

        
# To Do List 조작하기
def main():
    while True:
        print("\n--- To Do List ---")
        print("1. 전체 리스트 확인")
        print("2. 주별 리스트 확인")
        print("3. 날짜별 리스트 확인")
        print("4. 할 일 추가")
        print("5. 할 일 수정")
        print("6. 할 일 삭제")
        print("7. 종료")
        
       
        choice = int(input("원하는 메뉴 번호를 입력하세요: "))
        
        match choice:
            case 1:
                view_all()
            case 2:
                view_weekly()
            case 3:      
                view_daily()
            case 4:
                add_task()
            case 5:
                edit_task()
            case 6:
                delete_task()
            case 7:
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()