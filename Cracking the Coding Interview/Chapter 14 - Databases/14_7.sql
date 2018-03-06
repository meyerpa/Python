/*
14.7 Design Grade Database
Imagine a simple database storing information for students' grades.
Design what this database might look like and provide a SQL query to
return a list of the honor roll students (top 10%), sorted by their
grade point average
*/

DECLARE @GpaCutOff float;
@GpaCutOff = (
  --calculate GPA for each student
  SELECT min(
    TOP 10 PERCENT (
      4.0 * sum(grade * credits) / ISZERO(sum(credits), 1) as [GPA]
    )
  )
  FROM grades
  GROUP BY studentID
)

SELECT TOP Students.Name
FROM Students INNER JOIN
(
  --calculate GPA for each student
  SELECT studentID, 4.0 * sum(grade * credits) / ISZERO(sum(credits), 1) as [GPA]
  FROM grades
  GROUP BY studentID HAVING GPA >= @GpaCutOff
) as Gpa
