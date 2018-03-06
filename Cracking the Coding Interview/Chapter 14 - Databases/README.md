# Databases

## Denormalized vs. Normalized
**Denormalized databases** are designed to minimized read time (due to redundancy)
+ CONS
  + Updates and inserts are more expensive
  + Denormalization can make update and insert code harder to write
  + Data may be inconsistent. Which is the 'correct' value of a piece of data?
  + Data redundancy necessitates more storage
+ PROS
  + Retrieving data is faster, since fewer Joins
  + Queries to retrieve can be simpler (and therefor less likely to have bugs),
  we need to look at fewer tables
**Normalized databases** are designed to minimize redundancy
+ benefits: reduce space
+ drawbacks: common queries will require expensive joins

## SQL Statements (* means primary key)
`
Courses: CourseID*, CourseName, TeacherID
Teachers: TeacherID*, TeacherName
Students: StudentID*, StudentName
StudentCourses: CourseID*, StudentID
`

**Implement a query to get a list of all students and how many courses they are in**
`SQL
SELECT StudentName, Students.StudentID, count
FROM (
  SELECT Students.StudentID, count(StudentCourses.CourseID) as [CNT]
  FROM StudentCourses LEFT JOIN Students
  ON Student.StudentID = StudentCourses.StudentID
  GROUPBY Student.StudentID
) T INNER JOIN Students on T.StudentID = Students.StudentID
`
**OR**
`SQL
SELECT max(StudentName) as [StudentName], Students.StudentID,
       count(StudentCourses.CourseID) as [Count]
FROM Students LEFT JOIN StudentCourses
ON Student.StudentID = StudentCourses.StudentID
GROUPBY Student.StudentID
`

**Implement a query to get a list of all teachers and how many students they
each teach. If a teacher teaches the same student in two courses, you should
double count the student. Sort the list in descending order of the number of
students a teacher teaches.**
`SQL
SELECT Teachers.TeacherName, isNull(C.NumStudents, 0)
From Teachers LEFT JOIN (
  SELECT Courses.TeacherName, Courses.TeacherID, count(StudentID) as [NumStudents]
  FROM Courses INNER JOIN StudentCourses
  ON Courses.CourseID = StudentCourses.CourseID
  GROUPBY Courses.TeacherID, NumStudents
)
ORDER BY C.NumStudents DESC
`

## Small Database Design
**STEPS**
1. Handle Ambiguity - rare conditions may be best through a work around
2. Define the Core Objects (and typically each should be a table)
3. Analyze Relationships (one-to-one relationship? one-to-many? many-to-many?)
4. Investigate Actions - walk through common actions to store and retrieve data

## Large Database Design
*NEED TO DENORMALIZE DATA**
