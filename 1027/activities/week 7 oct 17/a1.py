def print_grades():
    f = open("grades.tsv", "r")
    print(f.read())
    f.close()

def read_grades():
    student_list = []
    f = open("grades.tsv", "r")
    skip_first_line = 1
    for line in f:
        if skip_first_line == 1:
            skip_first_line -= 1
            continue
        values = line.strip().split('\t')
        student_list.append(values)
    f.close()
    return student_list

def calc_final_grade(student_list):
    weighted_grades = []
    for line in student_list:
        name = line[0]
        assignment1 = float(line[1])
        assignment2 = float(line[2])
        final_exam = float(line[3])
        final_grade = (assignment1 * 0.2) + (assignment2 * 0.25) + (final_exam * 0.55)
        weighted_grades.append([name, final_grade])
    return weighted_grades

def write_grades(filename, final_list):
    f = open(filename, "a")
    f.write("Student Name, Final Grade")
    for line in final_list:
        f.write(f"{line[0]}, {round(line[1],2)}\n")
    f.close()

def main():
    print_grades()
    student_list = read_grades()
    final_list = calc_final_grade(student_list)
    write_grades("final_grades.csv", final_list)
    print(final_list)

main()
