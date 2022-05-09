from flask import *
from dbrk import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")

@app.route("/welcomepage")
def welcomepage():
    return render_template("home.html")

@app.route('/showaccounts')
def accounts():
    alist=acc()
    return render_template("accounts.html",alist=alist)


@app.route('/reg')
def reg():
    return render_template("register.html")
    
@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/passengerlist")
def passengerlist():
    plist = all()
    return render_template("passengerlist.html",plist=plist)

@app.route("/passengerdelete/<int:pnrno>")
def deletepassenger(pnrno):
    deletep(pnrno)
    return redirect(url_for("passengerlist"))

@app.route("/accountdelete/<int:id>")
def deleteaccount(id):
    delete(id)
    return redirect(url_for("accounts"))

@app.route("/register", methods=["POST"])
def add_user():
    ID = request.form["id"]
    fname = request.form["fullname"]
    Username = request.form["username"]
    passwo = request.form["password"]
    EMail = request.form["email"]

    t = (ID, fname, Username, passwo,EMail)
    register(t)
    return redirect("/")


@app.route("/passengeradd", methods=['POST','GET'])
def passengeradd():
    if request.method=='GET':
        return render_template("addpassengers.html")
    elif request.method=='POST':
        pnr= request.form["pnrno"]
        name = request.form["pname"]
        agee = request.form["age"]
        trainno = request.form["ptrainno"]
        trainname = request.form["ptrainname"]
        classs = request.form["pclass"]
        sour = request.form["psource"]
        dest = request.form["pdest"]
        amt = request.form["pamt"]
        status = request.form["pstatus"]
        doj = request.form["pdoj"]

        insert(pnr,name,agee,trainno,trainname,classs,sour,dest,amt,status,doj)
      #  insert(t)
        return redirect(url_for("passengerlist"))

@app.route("/passengerupdate/<int:pnrno>", methods=['POST','GET'])
def updatepassenger(pnrno):
        if request.method=='GET':
            passenger=get_single_passenger(pnrno=pnrno)
            return render_template("updatepassengers.html",passenger=passenger)

        elif request.method=='POST':
            name = request.form["pname"]
            agee = request.form["age"]
            trainno = request.form["ptrainno"]
            trainname = request.form["ptrainname"]
            classs = request.form["pclass"]
            sour = request.form["psource"]
            dest = request.form["pdest"]
            amt = request.form["pamt"]
            status = request.form["pstatus"]
            doj = request.form["pdoj"]

            t=(name,agee,trainno,trainname,classs,sour,dest,amt,status,doj,pnrno)
            update(t)
            return redirect(url_for("passengerlist"))

@app.route("/loginpage", methods=["post"])
def login_page():
    Username = request.form["username"]
    passw = request.form["password"]
 #   t=(name,passw)
    r=loginpage()
    if (Username,passw) in r:
        
        return redirect("/welcomepage")
    else:
        return redirect("/")

@app.route("/accountupdate/<int:id>", methods=['POST','GET'])
def updateaccount(id):
        if request.method=='GET':
            account=get_single_account(id=id)
            return render_template("updateaccount.html",account=account)

        elif request.method=='POST':
            Fname = request.form["fullname"]
            Uname = request.form["username"]
            Pswd = request.form["password"]
            Email = request.form["email"]

            p=( Fname, Uname, Pswd, Email, id )
            updateacc(p)
            return redirect(url_for("accounts"))



if __name__ == '__main__':
    app.run(debug=True)
