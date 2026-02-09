minor_grades = []
major_grades = []


def input_grades():
    """
    This function is gathering the grades (both minor and major) from the user in a list.
    """
    ask_grade = input(
        "Would you like to input your grades into this for minor: type 'N', and for major grades - type 'J'  ")
    if ask_grade.lower() == "n":
        put_grades_in_minor()
        ask_major = input("Got it, would you like to input your Major grades? Enter Y / N: ")
        if ask_major.lower() == "y":
            put_grades_in_major()
        else:
            print("Okay, we will generate your grade and GPA for your minor grades.")
    elif ask_grade.lower() == "j":
        put_grades_in_major()
        ask_minor = input("Got it, would you like to input your Minor grades? Enter Y / N: ")
        if ask_minor.lower() == "y":
            put_grades_in_minor()
        else:
            print("Okay, we will generate your grade and GPA for your major grades.")
    else:
        print("Sorry, I don't understand that option. Please try again.")
        exit()


def put_grades_in_minor():
    """
    Prompts the user to input minor grades and appends them to the minor_grades list until 'done' is entered.
    """
    print("Please enter your Minor grades. When you are finished, type 'D'. ")
    min_grd = ""
    while (min_grd.lower() != "d"):
        min_grd = input("")
        if validate_input(min_grd) == 'valid':
            minor_grades.append(min_grd)
        else:
            print("Try with valid input")
    minor_grades.pop()
    print(" ")


def put_grades_in_major():
    """
    Prompts the user to input minor grades and appends them to the major_grades list until 'done' is entered.
    """
    print("Please enter your Major grades. When you are finished, type 'D'. ")
    maj_grd = ""
    while (maj_grd.lower() != "d"):
        maj_grd = input("")
        if validate_input(maj_grd) == 'valid':
            major_grades.append(maj_grd)
        else:
            print("Try with valid input")
    major_grades.pop()
    print(" ")


def average_minor_grades(minor_grades):
    """
    Calculates the average of the minor grades list and applies a 40% weight.

    Agrs: A list of numerical grades as strings or integers

    Returns: The 40% of the average grade, which can be a float.
    """
    average_minor = 0
    if is_list_empty(minor_grades) == "valid":
        raw_minor = sum_list(minor_grades) / len(minor_grades)
        average_minor = (raw_minor) * 0.4
    return average_minor


def average_major_grades(major_grades):
    """
    Calculates the average of the major grades list and applies a 60% weight.

    Agrs: A list of numerical grades as strings or integers

    Returns: The 60% of the average grade, which can be a float.
    """
    average_major = 0
    raw_major = 0
    if is_list_empty(major_grades) == "valid":
        raw_major = sum_list(major_grades) / len(major_grades)
        average_major = (raw_major) * 0.6
    return average_major


def overall_grade(average_minor, average_major):
    """
    Calculates the total grade of the course by adding the average of the minor grades and the average of the major grades.

    Agrs: The weighted minor and major averages.

    Returns: The total grade of the course.
    """
    overall_grade_of_course = average_minor + average_major
    return float(overall_grade_of_course)


def sum_list(grade_list):
    """
    Calculates the sum of all the numerical values in the list.

    Agrs: A list of grades.

    Returns: The total sum of the grades in the list.
    """
    sum_list = 0

    for i in grade_list:
        sum_list = int(sum_list) + int(i)

    return int(sum_list)


def validate_input(grade):
    """
    Validates if the user input is 'done' or a grade between 0 and 100

    Agrs: The user input of grades or 'done' to be validated

    Returns: Returns valid or invalid depending on the user's input.
    """
    try:
        if grade.lower() == "d" or (int(grade) >= 0 and int(grade) <= 100):
            return "valid"
        else:
            return "Invalid"
    except ValueError:
        return "Invalid"


def is_list_empty(grade_list):
    """
    Checks if the list contains any elements to prevent calculation errors.

    Agrs: A list

    Returns: 'valid' if the string has values in it, otherwise 'invalid'
    """
    if len(grade_list) == 0:
        return "invalid"
    else:
        return "valid"


def type_class():
    """
    Prompts the user to input a shortened class type and converts it to a string.

    Returns: The full name of the class ("OL" -> "On-Level")
    """
    type_class = input("What is your class type? type OL or HN (Honors) or AP or DC or IB: ").upper()
    if type_class == 'OL':
        tc = 'On-Level'
    elif type_class == 'HN':
        tc = 'Honors'
    elif type_class == "AP":
        tc = "AP"
    elif type_class == "DC":
        tc = "Dual Credit (DC)"
    elif type_class == "IB":
        tc = "IB"
    else:
        tc = 'Invalid'
    return tc


def calculate_unweighted_gpa(overall_grade_of_course):
    """
    Calculates the Unweighted GPA based on the standard 4.0 Scale.

    Args: The final unweighted gpa of the course.

    Returns: The unweighted GPA Value (0.0 - 4.0)
    """
    if overall_grade_of_course >= 90:
        return 4.0
    elif 80 <= overall_grade_of_course < 90:
        return 3.0
    elif 70 <= overall_grade_of_course < 80:
        return 2.0
    elif 60 <= overall_grade_of_course < 70:
        return 1.0
    else:
        return 0.0


def calculate_weighted_gpa(grade, level):
    """
    Calculates the weighted GPA based on the standard 6.0 Scale.

    Args: The final weighted gpa of the course.

    Returns: The weighted GPA Value (0.0 - 6.0)
    """
    if grade < 70:
        return 0.0

    base_gpa = 5.0 - ((100 - grade) * 0.1)

    if level == "AP" or level == "Dual Credit (DC)" or level == "IB":
        w_gpa = float(base_gpa) + 1.0
    elif level == "Honors":
        w_gpa = float(base_gpa) + 0.5
    else:
        w_gpa = float(base_gpa)
    return round(w_gpa, 2)


def print_list(all_grade_rec):
    """
    This function gives the organized result in printable format
    Args: List of Dictionary that holds the
    """
    print("")
    print("################################")
    print("######## GPA CALCULATOR ########")
    print("################################")
    print("")
    print("--------------------------------")
    for item in all_grade_rec:
        for key in item:
            print(key + " : " + str(item[key]))
        print("--------------------------------")


print("Hello! Welcome to the Grade Calculator! ")
print("")
print("")
user_want_more = "Y"
all_grade_rec = []

while user_want_more.upper() == "Y":
    subject_course = input("What is the name of your Course? ")
    tc = type_class()
    if tc == "Invalid":
        print("Your input is invalid, and grade will be calculated as On-Level. ")
        tc = "On-Level"
    input_grades()
    average_minor = average_minor_grades(minor_grades)
    average_major = average_major_grades(major_grades)
    overall_grade_of_course = round(overall_grade(average_minor, average_major))
    uw_gpa = calculate_unweighted_gpa(overall_grade_of_course)
    w_gpa = calculate_weighted_gpa(overall_grade_of_course, tc)

    record = {
        "Subject": subject_course,
        "Grade": overall_grade_of_course,
        "Unweighted GPA": uw_gpa,
        "Weighted GPA": w_gpa
    }
    all_grade_rec.append(record)
    minor_grades.clear()
    major_grades.clear()
    user_want_more = input("Do you want to calculate for another subject? Type Y or N.")

    if user_want_more.lower() != "y":
        print_list(all_grade_rec)
        print("")
        print("Thank you for using GPA Calculator! ")
        exit()