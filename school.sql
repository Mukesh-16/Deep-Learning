/* Creating tables in database in PostgreSQL*/
CREATE TABLE Students (
  student_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  date_of_birth DATE,
  parent_name VARCHAR(100),
  address VARCHAR(100),
  city VARCHAR(50),
  phone_number VARCHAR(20)
);

CREATE TABLE Subjects (
  subject_id SERIAL PRIMARY KEY,
  subject_name VARCHAR(50)
);

CREATE TABLE Grades (
  grade_id SERIAL PRIMARY KEY,
  grade_name VARCHAR(10)
);

CREATE TABLE Marks (
  mark_id SERIAL PRIMARY KEY,
  student_id INTEGER REFERENCES Students(student_id),
  subject_id INTEGER REFERENCES Subjects(subject_id),
  grade_id INTEGER REFERENCES Grades(grade_id),
  score DECIMAL(5, 2)
);
/*adding values to tables*/
INSERT INTO Subjects(subject_name) VALUES('Telugu');
INSERT INTO Subjects(subject_name) VALUES('Hindi');
INSERT INTO Subjects(subject_name) VALUES('Maths');
INSERT INTO Subjects(subject_name) VALUES('Science');

INSERT INTO Grades(grade_name) VALUES(4);
INSERT INTO Grades(grade_name) VALUES(7);
INSERT INTO Grades(grade_name) VALUES(1);
INSERT INTO Grades(grade_name) VALUES(3);
drop table Marks

INSERT INTO Marks (student_id, subject_id, grade_id ,score) VALUES(2, 1, 2, 75);
INSERT INTO Marks (student_id, subject_id, grade_id ,score) VALUES(3, 2, 3, 55);
INSERT INTO Marks (student_id, subject_id, grade_id ,score) VALUES(1, 4, 1, 95);
INSERT INTO Marks (student_id, subject_id, grade_id ,score) VALUES(1, 3, 1, 55);
INSERT INTO Marks (student_id, subject_id, grade_id ,score) VALUES(2, 4, 2, 25);
INSERT INTO Marks (student_id, subject_id, grade_id ,score) VALUES(2, 2, 2, 95);

/*report of students who scored more than 60%*/

SELECT s.first_name, s.last_name FROM Students s JOIN (SELECT student_id, AVG(score) AS average_score
    FROM Marks GROUP BY student_id) AS avg_scores ON s.student_id = avg_scores.student_id
	WHERE avg_scores.average_score > 60;