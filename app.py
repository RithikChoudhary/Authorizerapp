from flask import Flask, render_template as render, request, redirect
from userDatabaseHandler import insertRow, checkPassword
import re


website = Flask(__name__)

@website.route("/")
def accountsPage():
    return render("accounts.html")


@website.route("/login/", methods=["GET","POST"])
def loginPage():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        userName = checkPassword(email, password)

        if userName:
            return render("userPage.html", userName = userName)
    
    return redirect("/")


@website.route("/register/", methods=["GET", "POST"])
def registerPage():
    if request.method == "POST":
        firstName   = request.form.get("firstName")
        lastName    = request.form.get("lastName")
        email       = request.form.get("email")
        password    = request.form.get("password")
        cpassword   = request.form.get("cpassword")

        #Check Validities
        valid = True

        #email Checks
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,5}$', email):
            valid = True
        else:
            valid = False
            print("email check failed")

        #Password Checks
        if valid and password == cpassword:
            valid = True
        else:
            valid = False
            print(f"passwords not equal, {password}!={cpassword}")
        
        if valid:
            insertRow(firstName, lastName, email, password)
            print("SUCCESS")
    
    return redirect('/')



if __name__ == "__main__":
    website.run()
    
