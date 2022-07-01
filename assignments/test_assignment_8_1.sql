CREATE TABLE students
(
    id integer
        constraint students_pk
            primary key autoincrement,
    name text,
    email text,
    year integer
);

CREATE TABLE courses
(
    id integer
        constraint courses_pk
            primary key autoincrement,
    name text,
    max_students integer
);

CREATE TABLE tests
(
    id integer
        constraint tests_pk
            primary key autoincrement,
    course_id integer
        constraint tests_courses_id_fk
            references courses,
    name text,
    date_time text
);

CREATE TABLE students_courses
(
student_id integer
    references students,
course_id  integer
    references courses
);
