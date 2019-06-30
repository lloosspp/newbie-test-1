import random

#convert the file into a suitable format to avoid any possible repetitions
def acquire_existing_records():
    with open('result.txt', 'r', encoding='utf-8') as f:
        records1 = f.read()
    lst_total_records = records1.split()

    with open('result.txt', 'r', encoding='utf-8') as f:
        records2 = f.readlines()
    lst_separate_records = []
    for record in records2:
        record = record.split()
        lst_separate_records.append(record)

    return lst_total_records, lst_separate_records


def check_record(name, lst_total_records):
    if name in lst_total_records:
        print ('欢迎回来%s, 祝你游戏愉快！' % name)
    else:
        print ('欢迎来到游戏%s!' % name)
        name = name
        return name


def acquire_guess():
    guess = input('请输入10以内的数字： ')
    try:
        guess = int(guess)
    except:
        while True:
            print('这不是一个数字')
            guess = input('请重新输入： ')
            try:
                guess = int(guess)
                break
            except:
                pass
    if int(guess) in range(0, 11):
        pass
    else:
        while True:
            print('数字不在范围内')
            guess = input('请重新输入： ')
            if int(guess) in range(0, 11):
                break
            else:
                pass
    return int(guess)


def number_guess():
    generated_number = random.randint(1, 10)
    round = 1
    while True:
        print('第%d次' % round)
        guess = acquire_guess()
        if guess == generated_number:
            print('猜对啦！')
            break
        elif guess < generated_number:
            print('太小啦！')
        elif guess > generated_number:
            print('太大啦！')
        round += 1
    print('你用了%d次猜对的' % round)
    return round


def add_new_record(new_name, total_game_time,lst_total_round):
    lst_new_record = []
    lst_new_record.append(name)
    lst_new_record.append(str(total_game_time))
    if total_game_time != 0:
        ave_round = sum(lst_total_round)/total_game_time
    else:
        ave_round = 0
    lst_new_record.append(str(ave_round))
    min_round = min(lst_total_round)
    lst_new_record.append(str(min_round) + '\n')
    with open('result.txt', 'a', encoding='utf-8') as f:
        for i in lst_new_record:
            f.write(i.ljust(6))
    return total_game_time, ave_round, min_round

def change_original_records(name, lst_separate_records, total_game_time, lst_total_round):
    for record in lst_separate_records:
        if record[0] == name:
            final_record1 = int(record[1]) + total_game_time
            final_record2 = (int(record[1]) * float(record[2]) + sum(lst_total_round)) / (int(record[1]) + total_game_time)
            final_record3 = min(lst_total_round)
            record[1] = final_record1
            record[2] = final_record2
            if final_record3 < int(record[3]):
                record[3] = final_record3
            else:
                final_record3 = int(record[3])
        else:
            pass
    with open('result.txt', 'w', encoding='utf-8') as f:
        for record in lst_separate_records:
            for word in record:
                f.write(str(word).ljust(6))
            f.write('\n')
    return final_record1, final_record2, final_record3



(lst_total_records, lst_separate_records) = acquire_existing_records()

name = input("请输入姓名: ")
new_name = check_record(name, lst_total_records)
total_game_time = 0
lst_total_round = []

while True:
    startup = int(input('是否开始游戏？ 1.是 2.退出' ))
    if startup == 1:
        print('猜猜数字是几？')
        round = number_guess()
        lst_total_round.append(round)
        total_game_time += 1
    else:
        if total_game_time == 0:
            if new_name:
                lst_total_round = [0]
                (total_game_time, ave_round, min_round) = add_new_record(new_name, total_game_time, lst_total_round)
            else:
                for record in lst_separate_records:
                    if record[0] == name:
                        total_game_time = int(record[1])
                        ave_round = float(record[2])
                        min_round = int(record[3])
        else:
            if new_name:
                (total_game_time, ave_round, min_round) = add_new_record(new_name, total_game_time,lst_total_round)
            else:
                (total_game_time, ave_round, min_round) = change_original_records(name, lst_separate_records, total_game_time, lst_total_round)

        print('你一共游戏了%d次' % total_game_time)
        print('你平均%.2f次猜中答案' % ave_round)
        print('你最好成绩是%d次猜中' % min_round)
        print('下次再见！')
        break
