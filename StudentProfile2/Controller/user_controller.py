from urllib import request
from app import app
from Model.user_model import user_model
from flask import request
obj=user_model()
@app.route("/user/getall")                 
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone", methods=["POST"])                 
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/update", methods=["PUT"])                 
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route("/user/delete/<stud_Rollno>", methods=["DELETE"])                 
def user_delete_controller(stud_Rollno):
    return obj.user_delete_model(stud_Rollno)

@app.route("/user/patch/<stud_Rollno>", methods=["PATCH"])                 
def user_patch_controller(stud_Rollno):
    return obj.user_patch_model(request.form,stud_Rollno)