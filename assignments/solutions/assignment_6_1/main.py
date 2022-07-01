import requests
import File_wClass as FileClass

input_Value = 0
used_url = "http://localhost:5000/students/"


def print_Main_Menu():
    print(f'1.Read all students\n'
          f'2.Get student by id\n'
          f'3.Add student\n'
          f'4.Edit student\n'
          f'5.Remove student\n'
          f'6.Exit')


def printAllStudent():
    response = requests.get(used_url)  # Sending a get-request to given url

    if response.status_code == 200:  # if status code received is 200, preceding with extraction of data
        student_list = response.json()  # transforming data (in json format) into an unorganized list

        for item in student_list:  # loop that goes through the whole list
            temp_id = item['id']  # defining temp variable with value with the given "item"
            temp_name = item['name']
            temp_email = item['email']
            temp_year = item['year']
            # using Student Class to organized data into a new list
            print(f'id: {temp_id}, name: {temp_name}, email: {temp_email}, year: {temp_year}')

    else:  # if response code is not 200, printing an error message
        print(f'Error code: {response.status_code}')
        print('Unable to print all students.')


def student_by_ID():
    student_list = []
    # getting all of the students and as in function above organizing them into a list
    response = requests.get(used_url)

    if response.status_code == 200:
        buffer_list = response.json()

        for item in buffer_list:
            id = item['id']
            name = item['name']
            email = item['email']
            year = item['year']
            student_list.append(FileClass.Student(id, name, email, year))

        # asking the user for input that we transform into an int
        student_id = int(input('Enter student ID: '))

        # if user input matches any id (is in given parameters) we will print the student with that id
        if 0 <= student_id <= len(student_list):
            print('200 OK')
            print(f'id: {student_list[student_id - 1].id}, '  # We have to subtract 1, because the list starts at zero 
                  f'name: {student_list[student_id - 1].name}, '  # We are printing not student with corresponding id,
                  f'email: {student_list[student_id - 1].email}, '  # but rather correspond position on the list
                  f'year: {student_list[student_id - 1].year}')
            # The data is organized so that the lowest id comes first
        else:
            print('400 NOT FOUND')  # Error massage if given id does not exist
            print('Student not found')
    else:  # Error message if something wrong with request
        print(f'Error code {response.status_code}')


def add_student():
    # requesting information about student that will be added
    add_name = input('Add student name: ')
    add_email = input('Add Student email:')
    add_year = int(input('Add year:'))

    #  defining a python dictionary where we add user input data
    new_Student = {
        "name": f"{add_name}",  # has to format them this way so that it can be later send in json format
        "email": f"{add_email}",
        "year": add_year
    }

    # sending a post-request that adds new objects to the server
    request_add_student = requests.post(used_url, json=new_Student)
    print(request_add_student)

    # if response code is 200 will get the updated information from the server
    if request_add_student.status_code == 201:

        second_Request = requests.get(used_url)
        id_request = second_Request.json()
        buffer_list = []

        for item in id_request:
            id = item['id'],
            name = item['name']
            email = item['email'],
            year = item['year']
            # organizing data into a list
            buffer_list.append(FileClass.Student(id, name, email, year))

        # The server adds its own id that comes in tuple-format
        # In tuple-format values that parenthesis and ending with a comma
        # Using .join to get them into string format
        std_id_str = ', '.join(map(str, buffer_list[-1].id))

        print(f'Added student: id: {std_id_str}, '
              f'name: {add_name}, '
              f'email: {add_email}, '
              f'year: {add_year}')

    else:  # if response code is incorrect printing an error massage
        print('404 Bad Request\n')


def edit_student():
    # requesting user for data
    add_id = int(input('ID:'))
    add_name = input('Name: ')
    add_email = input('Email:')
    add_year = int(input('Year:'))

    edited_student = {  # creating a python dictionary with information given bt the user
        "id": add_id,
        "name": f"{add_name}",
        "email": f"{add_email}",
        "year": add_year
    }

    # modifying the url since to edit an object, url has to contain id of that object
    url_withID = f"{used_url}{add_id}"
    # Sending a put-request that edits existing data
    request_edit_student = requests.put(url_withID, json=edited_student)

    # if response code is 200, printing a success-massage
    if request_edit_student.status_code == 200:
        print(f'200 OK')
        print(f'Student was edited successfully')
    # if response code is incorrect, print an error message
    else:
        print(f'404 Not Found')
        print(f'Student not found')


def remove_student():
    delete_id = int(input('ID:'))

    # to delete an object url has to contain its id
    # modifying url so it contained id of the object that the user wants to delete
    url_with_delete_ID = f"{used_url}{delete_id}"

    # Sending a delete-request with modified url
    request_delete = requests.delete(url_with_delete_ID)

    # whe deleted status code is 204
    # if status code is correct when print a success-massage
    if request_delete.status_code == 204:
        print('204 No Content')
        print('Student was removed successfully')

    # if status code is incorrect print an error massage
    else:
        print('404 Not Found')
        print('Student not found')


if __name__ == '__main__':

    while 1:
        # With every spin print menu
        print_Main_Menu()
        # with every spin stop and ask for user input
        input_Value = int(input('\nEnter a value:'))

        # each user input is assigned a function that performs an action
        if input_Value == 1:
            printAllStudent()
        elif input_Value == 2:
            student_by_ID()
        elif input_Value == 3:
            add_student()
        elif input_Value == 4:
            edit_student()
        elif input_Value == 5:
            remove_student()
        elif input_Value == 6:
            break
        else:
            print('400 Bad Request')