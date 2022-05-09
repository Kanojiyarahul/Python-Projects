import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='Rahul@123',database='train')
    
def loginpage():
    db=getConnection()
    sql='select username , password from account'
    cr=db.cursor()
    cr.execute(sql)
    elist1=cr.fetchall()
    db.commit()
    db.close()
    return elist1    

def register(t):
    db=getConnection()
    sql='insert into account values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
    

def insert(pnrno,pname,age,ptrainno,ptrainname,pclass,psource,pdest,pamt,pstatus,pdoj):
    db=getConnection()
    sql='insert into passengers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    i=cr.execute(sql,(pnrno,pname,age,ptrainno,ptrainname,pclass,psource,pdest,pamt,pstatus,pdoj))
    db.commit()
    db.close()
    return i

def update(t):
    db=getConnection()
    sql = 'update passengers set pname=%s,age=%s,ptrainno=%s,ptrainname=%s,pclass=%s,psource=%s,pdest=%s,pamt=%s,pstatus=%s,pdoj=%s where pnrno=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def deletep(pnrno):
    db=getConnection()
    sql = 'delete from passengers where pnrno=%s'
    cr=db.cursor()
    cr.execute(sql,pnrno)
    db.commit()
    db.close()

def all():
    db=getConnection()
    sql = 'select * from passengers'
    cr=db.cursor()
    cr.execute(sql)
    rows = cr.fetchall()
    db.commit()
    db.close()
    return rows

def get_single_passenger(pnrno):
    db=getConnection()
    sql= 'select * from passengers where pnrno=%s'
    cr=db.cursor()
    cr.execute(sql,pnrno)
    row = cr.fetchone()
    db.commit()
    db.close()
    return row

def acc():
    db=getConnection()
    sql = 'select * from account'
    cr=db.cursor()
    cr.execute(sql)
    rows = cr.fetchall()
    db.commit()
    db.close()
    return rows


def get_single_account(id):
    db=getConnection()
    sql= 'select * from account where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    row = cr.fetchone()
    db.commit()
    db.close()
    return row


def updateacc(p):
    db=getConnection()
    sql = 'update account set fullname=%s,username=%s,password=%s,email=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,p)
    db.commit()
    db.close()

def delete(id):
    db=getConnection()
    sql = 'delete from account where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()






