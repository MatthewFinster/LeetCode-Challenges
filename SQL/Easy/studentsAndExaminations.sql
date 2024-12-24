-- Problem: Students and Examinations (LeetCode #1280)
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/students-and-examinations/

-- Select studentID, studentName, subjectName and attendedExams
SELECT 
    s.student_id,
    s.student_name,
    su.subject_name,
    COUNT(e.subject_name) AS attended_exams
-- From Students table
FROM Students s
-- CROSS joint with subjects to provide every possible combination (every student takes every subject)
CROSS JOIN Subjects su
-- LEFT join with the examination table to include everything from the CROSS joint table, even if the exam wasnt taken
LEFT JOIN Examinations e 
-- ensure studentID matches in both and subjectName matches in both
    ON s.student_id = e.student_id AND su.subject_name = e.subject_name
-- GROUP by ID, name and subject name so that a COUNT is produced for each e.subjectName per group
GROUP BY s.student_id, s.student_name, su.subject_name
ORDER BY s.student_id, su.subject_name;