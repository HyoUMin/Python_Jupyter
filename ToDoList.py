# To Do List

# 전체 To Do List 확인하기
# 조회하고 싶은 날짜의 To Do List 확인하기
# To Do List 추가 하기
# 기존 To Do List 수정하기
# 기존 To Do List 삭제하기
# ======================================================

todo_list = []

# 저장된 To Do List 모두 출력
def view_all():
    print("======== 전체 할 일 목록 ========")

    if not todo_list:
        print("저장된 할 일이 없습니다.")
        return
    
    for task in todo_list:
        print(f"날짜: {task['date']}\n할 일 : {task['detail']}")


# 조회하고 싶은 날짜의 To Do List 출력
def view_daily():
    while True:
        date_choose = input("조회하고 싶은 날짜를 입력하세요(예: 2026-04-02):")
        
        if len(date_choose) == 10 and date_choose[4] == "-" and date_choose[7] == "-" and date_choose.replace("-", "").isdigit():
            break

        else:
            print("형식이 잘못되었습니다. '2026-04-02' 형태로 다시 입력해주세요.\n") 

    print(f"\n======== {date_choose} 할 일 목록 ========")
    
    count = 0

    for task in todo_list:
        if date_choose == task["date"]:
            print(f" 날짜: {task['date']}\n 할 일: {task['detail']}")
            count += 1
    
    if count == 0:
        print("해당 날짜는 등록되지 않았습니다.")


# To Do List 입력 
def add_task():
    while True:
        date_ = input("날짜를 입력하세요(예: 2026-04-02)")
        
        if len(date_) == 10 and date_[4] == "-" and date_[7] == "-" and date_.replace("-", "").isdigit():
            break

        else:
            print("형식이 잘못되었습니다. '2026-04-02' 형태로 다시 입력해주세요.\n") 

    todo = input("할 일을 입력하세요:")
    todo_list.append({"date": date_, "detail": todo})

    print("할 일이 추가되었습니다.")


# To Do List 수정 - 1. 수정하고 싶은 날짜 선택 2. 수정하고 싶은 항목 선택 3. 항목 수정
def edit_task():
    while True:
        edit_date = input("수정하고 싶은 날짜를 입력하세요(예: 2026-04-02):")

        if len(edit_date) == 10 and edit_date[4] == "-" and edit_date[7] == "-" and edit_date.replace("-", "").isdigit():
            break

        else:
            print("형식이 잘못되었습니다. '2026-04-02' 형태로 다시 입력해주세요.\n") 
    
    print(f"\n======== 할 일 목록 수정 ========")
    
    matches = []

    for task in todo_list:
        if edit_date == task["date"]:
            matches.append(task)
    
    if not matches:
        print("해당 날짜에 등록된 할 일이 없습니다.")
        return
    
    print(f"\n======== {edit_date} 검색 결과 ========")
    
    for i, task in enumerate(matches, 1):
        print(f"{i}. 할 일: {task['detail']}")

    change = int(input("\n수정할 항목의 번호를 입력하세요: ")) - 1

    if 0 <= change < len(matches):     
        new_todo = input("새로운 할 일을 입력하세요: ")
        matches[change]["detail"] = new_todo
      
        print("수정이 완료되었습니다.")
    
    else:
        print("잘못된 번호입니다.")


# To Do List 삭제 - 1. 삭제하고 싶은 날짜 선택 2. 삭제하고 싶은 항목 선택 3. 항목 삭제 
def delete_task():
    while True:    
        del_date = input("삭제하고 싶은 날짜를 입력하세요(예: 2026-04-02):")
        
        if len(del_date) == 10 and del_date[4] == "-" and del_date[7] == "-" and del_date.replace("-", "").isdigit():
            break
        
        else:
            print("형식이 잘못되었습니다. '2026-04-02' 형태로 다시 입력해주세요.\n") 
    
    print(f"\n======== 할 일 목록 삭제 =========")
    
    matches = []

    for task in todo_list:
        if del_date == task["date"]:
            matches.append(task)

    if not matches:
        print("해당 날짜는 등록되지 않았습니다.")
        return
    
    print(f"\n======== {del_date} 검색 결과 ========")

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
        print("\n======== To Do List ========")
        print("1. 전체 리스트 확인")
        print("2. 날짜별 리스트 확인")
        print("3. 할 일 추가")
        print("4. 할 일 수정")
        print("5. 할 일 삭제")
        print("6. 종료")
        
        choice = int(input("원하는 메뉴 번호를 입력하세요: "))
        
        match choice:
            case 1:
                view_all()
            case 2:      
                view_daily()
            case 3:
                add_task()
            case 4:
                edit_task()
            case 5:
                delete_task()
            case 6:
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()
