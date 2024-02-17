from models import db, Groups, Students, Teachers, Subjects, Grages
from peewee import *


def task_7():
    avg_score = (Grages.select(fn.AVG(Grages.score).alias("AVG_Score")).get())
    print(avg_score.AVG_Score)
    return avg_score



def top_5_students_by_subject(subject_id):
    """
    -- Топ 5 студенів з найвищим середнім балом з певного предмета

    select s.student_name, s2.name_subject, avg(score) as avg_score
    from students s
    	join grades g on s.id = g.students_id
    	join subjects s2 on g.subjects_id = s2.id
    where s2.id = 1
    group by s.student_name, s2.name_subject
    order by avg(score) desc
    limit 5
    """

    top_students = Students.select(
        Students.student_name,
        Subjects.name_subject,
        fn.AVG(Grages.score).alias("AVG_Score"))\
            .join(Grages)\
            .join(Subjects)\
        .where(Subjects.id == subject_id)\
        .group_by(Students.student_name, Subjects)\
        .order_by(fn.AVG(Grages.score).desc())\
        .limit(5)

    for student in top_students.objects():
        print(student.student_name, student.name_subject, student.AVG_Score)
