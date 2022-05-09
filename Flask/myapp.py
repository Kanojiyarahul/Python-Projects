from flask import *
from DBM import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")

@app.route("/reg")
def register():
    return render_template("register.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/emplist")
def emp_list():
    data = selectAllEmp()
    return render_template("emplist.html", elist=data)

@app.route("/addEmp", methods=["POST"])
def add_emp():
    ids = request.form["id"]
    name = request.form["uname"]
    contact = request.form["contact"]
    email = request.form["email"]
    passw = request.form["passw"]

    t = (ids, name, contact, email, passw)
    addEmp(t)
    return redirect("/")

@app.route("/loginpage", methods=["post"])
def login_page():
    name = request.form["uname"]
    passw = request.form["passw"]
##    t=(name,passw)
    r=loginpage()
    if (name,passw) in r:
        
        return redirect("/emplist")
    else:
        return redirect("/")

@app.route("/deleteEmp")
def delete_emp():
    ids=request.args.get("id")
    deleteEmp(ids)
    return redirect("\emplist")

@app.route("/editEmp")
def edit_emp():
    ids=request.args.get("id")
    data=selectEmpById(ids)
    return render_template("update.html",row=data)




    

if(__name__=="__main__"):
    app.run(debug=True)
