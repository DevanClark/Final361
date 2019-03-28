class CourseEdit:
    def __init__(self):
        self = self

    def view_all_courses(self, loggedinuser):
        return "yes"

    def assign_ta(self, tausername, courseid, labsection, loggedinuser):
        return "yes"

    def create_course(self, instructor, courseid, classname, studentlist, labsection, talist, loggedinuser):
        return "yes"

    def view_course_assignments(self, courseid, loggedinuser):
        return "yes"

    def delete_course(self, courseId, loggedinuser):
        return "yes"
