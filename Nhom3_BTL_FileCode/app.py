import secrets
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
import connectdb
from functools import wraps
import hashlib
# from flask import request

def login_required(f):
    @wraps(f)
    def check(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for("login", next=request.url))
        return f(*args , **kwargs)
    return check
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Tạo một SECRET_KEY có độ dài 16 bytes

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    err_msg = ""
    # form = LoginForm()
    # if form.validate_on_submit():
    #     print("nhan login")
    #     # Đoạn mã xử lý đăng nhập ở đây (điều này sẽ được thực hiện trong phiên bản thực tế).
    #     flash(f'Logged in as {form.username.data}', 'success')
    #     return redirect(url_for('home'))
    if request.method == "POST":
        taikhoan = request.form.get("taikhoan")
        matkhau = request.form.get("matkhau")
        print(taikhoan , matkhau)
        matkhau = hashlib.md5(matkhau.strip().encode("utf-8")).hexdigest()
        userDao = connectdb.checkLogin(taikhoan , matkhau)
        if userDao:
            session ["user"] = userDao.to_dict()
            return redirect(url_for('iot'))    
            # render_template('login.html')
        else:
            err_msg = "Đăng nhập không thành công"

    return render_template('login.html',err_msg = err_msg)

@app.route("/logout")
def logout():
    session["user"] = None
    return redirect(url_for("home"))

@app.route('/iot', methods=['GET', 'POST'])
# @login_required
def iot():
    return render_template('iot.html')

@app.route('/savedata', methods=['GET', 'POST'])
def savedata():
    if request.method == "POST":
        nhietdo = request.form.get("temperature")
        doam = request.form.get("humidity")
        doamdat = request.form.get("soilMoisture")
        # connectdb.insertData(nhietdo , doam , doamdat)
    # return jsonify({"message": "Dữ liệu đã được lưu thành công"})
        try:
            # Gọi hàm insertData từ module connectdb
            connectdb.insertData(nhietdo, doam, doamdat)
            return "Dữ liệu đã được chèn thành công"
        except Exception as e:
            print("Lỗi khi chèn dữ liệu:", str(e))
            return "Đã xảy ra lỗi khi chèn dữ liệu"

@app.route('/dudoan', methods=['GET', 'POST'])  
def dudoan():
    if request.method == "GET":
        loairaududoan = str(connectdb.dudoan())
        print(loairaududoan)
        return loairaududoan

if __name__ == '__main__':
    # print(connectdb.checkLogin("admin" , "123"))
    app.run(host='0.0.0.0', port=5000)
