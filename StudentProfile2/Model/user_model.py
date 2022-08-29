import mysql.connector
from flask import make_response
import json
class  user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Pk_123456",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("some error")


    def user_getall_model(self):
        self.cur.execute("SELECT * FROM student")
        result =self.cur.fetchall()
        if len(result)>0:
            res= make_response({"payload":result},200)
            res.headers['Access - Control - Allow - Origin'] ="*"
            return res
        else:
            return make_response({"message": "No Data found"},204)
    
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO student(stud_Rollno, First_name, Last_name, email, phone) VALUES('{data['stud_Rollno']}','{data['First_name']}','{data['Last_name']}','{data['email']}', '{data['phone']}')")
        return make_response({"message":"User Created Successfully"},201)
    
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE student SET  First_name='{data['First_name']}', Last_name='{data['Last_name']}', email='{data['email']}', phone='{data['phone']}' WHERE stud_Rollno={data['stud_Rollno']}")
        if self.cur.rowcount>0:
            return make_response({"message":"User Update Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"},202)
    
    def user_delete_model(self,stud_Rollno):
        self.cur.execute(f"DELETE FROM student WHERE stud_Rollno={stud_Rollno}")
        if self.cur.rowcount>0:
            return make_response({"message":"User Delete Successfully"},200)
        else:
            return make_response({"message":"Nothing to Delete"},202)
    
    def user_patch_model(self,data, stud_Rollno):
        qry ="UPDATE student SET"
        # print(data)
        for key in data:
            qry= qry +f"{key}='{data[key]}' ,"
        qry = qry[:-1] + f"WHERE stud_Rollno={stud_Rollno}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return make_response({"message":"User Update Successfully"},201)
        else:
            return make_response({"message":"Nothing to Update"},202)
       