from UI.console import Console
#----
from Controller.student_service import ServiceStudent
from Controller.discipline_service import ServiceDiscipline
from Controller.note_service import ServiceNote
#----
from Repository.student_repo import StudentRepo
from Repository.discipline_repo import DisciplineRepo
from Repository.note_repo import NoteRepo
#----
from Controller.Validators.student_validator import ValidatorStudent
from Controller.Validators.discipline_validator import ValidatorDiscipline
from Controller.Validators.note_validator import ValidatorNota
# TEST
from Test.testStudent import TestStudent
from Test.testDisciplina import TestDiscipline
from Test.testNote import TestNote

stud_repo_test = StudentRepo()
disc_repo_test = DisciplineRepo()
note_repo_test = NoteRepo()

stud_valid_test = ValidatorStudent()
disc_valid_test = ValidatorDiscipline()
note_valid_test = ValidatorNota()

stud_srv_test = ServiceStudent(stud_valid_test , stud_repo_test)
disc_srv_test = ServiceDiscipline(disc_valid_test , disc_repo_test)
nota_srv_test = ServiceNote(note_valid_test , note_repo_test)

stud_test = TestStudent(stud_srv_test)
stud_test.test_all()

disc_test = TestDiscipline(disc_srv_test)
disc_test.test_all()

note_test = TestNote(nota_srv_test , stud_srv_test , disc_srv_test)
note_test.test_all()

# MAIN

#Clear the screen
print("\033c", end="")

stud_repo = StudentRepo()
disc_repo = DisciplineRepo()
note_repo = NoteRepo()

stud_valid = ValidatorStudent()
disc_valid = ValidatorDiscipline()
note_valid = ValidatorNota()

stud_srv = ServiceStudent(stud_valid , stud_repo)
disc_srv = ServiceDiscipline(disc_valid , disc_repo)
nota_srv = ServiceNote(note_valid, note_repo)

ui = Console(stud_srv,disc_srv,nota_srv)
ui.run()