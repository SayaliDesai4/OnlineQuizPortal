import json
from locust import HttpUser, task

class Testing(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/admin")

        self.client.get("/student")
        # self.client.get("/student/calculate-marks")
        # self.client.get("/student/view-result")
        # self.client.get("/student/student-marks")
        # self.client.get('/student/studentclick')
        # self.client.get('/student/studentlogin')
        # self.client.get('/student/studentsignup')
        # self.client.get('student/student-dashboard')
        # self.client.get('student/student-exam')

        # self.client.get('teacher/teachersignup')
        # self.client.get('teacher/teacher-dashboard')
        # self.client.get('teacher/teacher-exam')
        # self.client.get('teacher/teacher-add-exam')
        # self.client.get('teacher/teacher-view-exam')
        

    