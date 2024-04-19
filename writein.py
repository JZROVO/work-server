import pymysql

def writein(name,baseType,variant,levelRequired):

    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "poe"

    )
    cursor = con.cursor()
    cursor.execute("insert into jewels(name,basetype,passive,level) values(%s, %s, %s, %s)",(name,baseType,variant,levelRequired))
    con.commit()
    con.close()
    return 0



def writein1(jewelname,passive,weight):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "poe"


    )

    cursor = con.cursor()
    cursor.execute("insert into usefullpassive(jewelname,passive,weight) values(%s, %s, %s)",(jewelname,passive,weight))
    con.commit()
    con.close()
    return 0

def writein2(enname,cnname):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "poe"


    )

    cursor = con.cursor()
    cursor.execute("insert into cntoen(enname,chname) values(%s,%s)",(enname,cnname))
    con.commit()
    con.close()
    return 0


def writein3(cardname,value,stack):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "poe"
    )
    cursor = con.cursor()
    cursor.execute("insert into divinationcard(cardname,value,stack) values(%s ,%s , %s)",(cardname,value,stack))
    con.commit()
    con.close()
    return 0



def writein4(nickname,id,password):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "user"
    )
    cursor = con.cursor()
    cursor.execute("insert into alluser(nickname,id,password) values(%s,%s,%s)",(nickname,id,password))
    con.commit()
    con.close()
    return 0



def findsome(id):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "user"
    )
    cursor = con.cursor()
    #cursor.execute("select * from alluser where id = %s ",(id))
    if cursor.execute("select * from alluser where id = %s ",(id)) !=0:
        return False
    else:
        return True
    
def logincheck(id,password):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "user"
    )
    cursor = con.cursor()
    
    if cursor.execute("select * from alluser where id = %s and password = %s" ,(str(id),str(password))) != 0:
        
        return True
    else:
        
        return False


def search (id):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "user"
    )
    cursor = con.cursor()

    cursor.execute("select nickname from alluser where id = %s " ,(str(id)))
    con.commit()
    nickname = cursor.fetchone()
    #print(nickname[0])
    return nickname[0]

def findcard(id):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "poe"
    )
    cursor = con.cursor()
    newid = int(id)
    cursor.execute("select * from divinationcard where id = %s ",(newid))
    con.commit()
    cardname =  cursor.fetchone()
    
    return cardname[1],cardname[3]
    


def abc(cardname,value,stack):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "poe"
    )
    cursor = con.cursor()
    cursor.execute("insert into divinationcard(cardname,value,stack) values(%s,%s,%s)",(cardname,value,stack))
    con.commit()
    con.close()
    return 0



def saveinrecord(id,cardname):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "user"
    )
    cursor = con.cursor()
    cursor.execute("insert into successrecord(id,cardname) values(%s ,%s)",(id,cardname))
    con.commit()
    con.close()
    
    return 0



def checkrecord(id):
    con = pymysql.connect(
        user = "root",
        password = "skyandpig1017",
        host = "localhost",
        database = "user"
    )
    cursor = con.cursor()
    cursor.execute("select id from successrecord where id = %s",(id))
    row_count =cursor.rowcount
   
    
    con.commit()
    con.close()
    if row_count >0:
        return row_count
    else:
        return 0