

def course_average(lst, num):
    certain_course = []
    for num1 in range (0, len(lst)):
        certain_course.append(lst[num1][num])
    ave_mark = round(sum(certain_course)/student_num, 1)
    return ave_mark


#read content from the file

with open("project 1.txt", encoding= 'UTF-8') as data:
    content = data.readlines()

#set basic variables
student_num = len(content) - 1
title_row = content[0]
lst_title_row = title_row.split()
num_of_course = len(lst_title_row) - 1

#create a new list exluding the title row but including total marks and average marks
new_lst = []
for num in range (1, len(content)):
    line = content[num]
    lst_line = line.split()
    total = 0
    for num2 in range (1, len(lst_line)):
        lst_line[num2] = int(lst_line[num2])
        mark = lst_line[num2]
        total += mark
    lst_line.append(total)
    average = round(total / num_of_course, 1)
    lst_line.append(average)
    new_item = lst_line
    new_lst.append(new_item)

#create another list for average/total marks of each course
ave_marks = []
for num4 in range (1,10):
    ave_mark = course_average(new_lst, num4)
    ave_marks.append(ave_mark)

total_ave = round(sum(ave_marks), 1)
ave_total_ave = round(total_ave/num_of_course, 1)

ave_marks.append(total_ave)
ave_marks.append(ave_total_ave)
ave_marks.insert(0, '平均')
ave_marks.insert(0, 0)

#modifies the title row (note that this one can affect the process of calculateing ave/tot for each course as the indexes are changed )
lst_title_row.insert(0, '名次')
lst_title_row.append ('总分')
lst_title_row.append ('平均分')

#replace marks below 60 with words
for num5 in range (0, len(new_lst)):
    for num6 in range (0, len(new_lst[num5])):
        mark1 = new_lst[num5][num6]
        if isinstance(mark1, int):
            if mark1 < 60:
                new_lst[num5][num6] = '不及格'
        else:
            pass

#sort sub-lists based on the second to last value
new_lst.sort(key = lambda x: x[-2], reverse = True)

#add ranking number
number = 1
for a_sublist in new_lst:
    a_sublist.insert(0, number)
    number += 1

#convert existing contents into writable format i.e. string
#1.title row
for i in range (0, len(lst_title_row)):
    lst_title_row[i] = str(lst_title_row[i])

print (lst_title_row)

#2. average mark row
for j in range (0, len(ave_marks)):
    ave_marks[j] = str(ave_marks[j])

print (ave_marks)

#3. content rows
for m in range (0, len(new_lst)):
    for n in range (0, len(new_lst[m])):
        new_lst[m][n] = str(new_lst[m][n])


print (new_lst)

#write in a new file
with open('mark.txt', 'w', encoding='utf-8') as f:
    for title in lst_title_row:
        f.write(title.ljust(6))
    f.write('\n')

    for mark in ave_marks:
        f.write(mark.ljust(6))
    f.write('\n')

    for items in new_lst:
        for j in items:
            f.write(j.ljust(6))
        f.write('\n')


