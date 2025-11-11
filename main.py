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
#----

stud_repo = StudentRepo()
disc_repo = DisciplineRepo()
note_repo = NoteRepo()

stud_valid = ValidatorStudent()
disc_valid = ValidatorDiscipline()

stud_srv = ServiceStudent(stud_valid , stud_repo)
disc_srv = ServiceDiscipline(disc_valid , disc_repo)

ui = Console(stud_srv,disc_srv,ServiceNote)
ui.run()