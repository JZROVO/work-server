from flask import Flask
from flask import request #載入 Request 物件
import json
from flask import redirect
from flask import render_template
from flask import session
import writein as wr
import random
from flask import send_from_directory
from flask_cors import CORS
from datetime import timedelta
#建立application物件,可以設定靜態檔案的路徑處理
app=Flask(  
    __name__,
    static_folder="static",     #靜態檔案的資料夾名稱

    static_url_path="/static"    #靜態檔案對應的網址路徑
    )
 #所有在static資料夾底下的檔案，都對應到網址路徑/static/檔案名稱


CORS(app,supports_credentials=True)
app.secret_key ="jimmy15978"  #設定Session密鑰 可以是任何字串 但只能自己知道

app.permanent_session_lifetime = timedelta(days=1)





@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue_app(path):
    if path == '':
        return render_template('dist/index.html')  # Render Vue.js dynamic content
    elif path.startswith('js/') or path.startswith('css/') or path.startswith('img/') or path.startswith('fonts/'):
        return send_from_directory('static', path)
    else:
        return render_template('dist/index.html')  # Render Vue.js dynamic content
    #return redirect("nttps://www.google.com/") #導向其他網址("/zh/")
    #print("請求方法",request.method)
    #print("通訊協定",request.scheme)
    #print("主機名稱",request.host)
    #print("路徑",request.path)
    #print("完整的網址",request.url)
    #print("瀏覽起和作業系統",request.headers.get("user-agent"))
    #print("語言偏好",request.headers.get("accept-language"))
    #print("引薦網址", request.headers.get("referrer"))
    '''
    lang= request.headers.get("accept-language")
    if lang.startswith("en"):
        return json.dumps({
            "status":"OK",
            "text":"Hello Flask" 
        })                                #回傳網站首頁的內容
                            
    else:
        return json.dumps({
            "status":"OK",
            "text":"您好，歡迎光臨" 
        }, ensure_ascii=False)        #指示不要用ASCII處理中文            
    '''




@app.route("/signup", methods=["POST"])
def signup():
    nickname = request.form["nickname"]
    id = request.form["ID"]
    password = request.form["password"]
    if wr.findsome(id) == True:
        wr.writein4(nickname,id,password)
        return redirect("/")
    else:
        return redirect("/error?msg=id已經被註冊")

cardarray = []
for i in range(0,425):
    cardarray.append(i) 

@app.route("/api/draw")
def draw():
    
    cardnumber = random.choice(cardarray)
    cardarray.remove(cardnumber)
    name,stack = wr.findcard(cardnumber)

    x = {
        "name":name,
        "stack": stack,
    }
    return json.dumps(x)



@app.route("/loadcardnumber")
def loadcardnumber():
    owncard = request.args.get("cardname")
    session["owncard"] = owncard
    cardnumber =  request.args.get("number2")
    return 


@app.route("/reset")
def reset():
    return render_template("test.html")


@app.route("/api/gg", methods=['POST'])
def gg():
    nickname = request.form.get("nickname")
    id = request.form.get("ID")
    password = request.form.get("password")
    print(nickname, id ,password)

    if wr.findsome(id) == True:
        wr.writein4(str(nickname),str(id),str(password))
        return "a"
    else:
        return "已經被註冊了"


@app.route("/api/login", methods=['POST'])
def login():
    nickname = request.form.get("nickname")
    id = request.form.get("ID")
    password = request.form.get("password")
    
    if wr.logincheck(id,password) != True :
        return ("")
    session["ID"] = str(id)  #session["欄位名稱"]= 資料      
    
    nickname =str(wr.search(id))
    record = str(wr.checkrecord(id))
    session["successcount"] = record
    print(nickname,record)
    return nickname+' '+record
    
            
    
    
@app.route("/api/logout")
def logout():
    session.pop("ID",None)
    return redirect("http://localhost:5173/")
    


@app.route("/api/checkloginornot")
def checkloginornot():
    if "ID" in session and session["ID"] != None:
        nickname = str(wr.search(session["ID"]))
        winrate = session["successcount"] 
        return nickname +" "+ winrate
    else:
        return "0"


@app.route("/api/saverecord")
def saverecord():
    id = session["ID"]
    cardname = request.args.get("cardname")
    wr.saveinrecord(str(id),str(cardname))
    
    return "0"



app.run(port=3000)  #啟動網站伺服器 可透過port 參數指定埠號
