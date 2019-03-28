class CourseEdit:
    def __init__(self):
        self = self

    def viewAllCourses(self, loggedinuser):
        return "yes"

    def assignTA(self, tausername, courseid, labsection, loggedinuser):
        return "yes"

    def createCourse(self, instructor, courseid, classname, studentlist, labsection, talist, loggedinuser):
        return "yes"

    def viewCourseAssignments(self, courseid, loggedinuser):
        return "yes"

    def deleteCourse(self, courseId, loggedinuser):
        return "yes"
