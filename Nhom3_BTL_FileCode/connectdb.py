import mysql.connector
from model.user import User
from sklearn.tree import DecisionTreeClassifier
import hashlib
db = mysql.connector.connect(user='root', password='123456', host='localhost', database='iot')
mycursor = db.cursor()
#tao csdl database
def create_schema_and_insert_data():
    # Tạo kết nối đến MySQL
    db = mysql.connector.connect(user='root', password='123456', host='localhost', database='iot')
    # Tạo con trỏ
    mycursor = db.cursor()

    # Truy vấn CREATE SCHEMA (nếu chưa tồn tại)
    code_create_schema = 'CREATE SCHEMA IF NOT EXISTS `iot`;'
    mycursor.execute(code_create_schema)
    db.commit()
def selectAll():
    code_select_all = "SELECT * FROM `user`;"
    mycursor.execute(code_select_all)
    # Lấy tất cả các dòng kết quả
    result = mycursor.fetchall()
    arr = []
    for row in result:
        # print(f'Tài khoản: {row[1]}, Mật khẩu: {row[2]}')
        user_x = User(row[0] , row[1] , row[2])
        arr.append(user_x)
    return arr
def checkLogin(tk , mk):
    # Tạo kết nối đến MySQL
    # db = mysql.connector.connect(user='root', password='123456', host='localhost', database='iot')

    # Tạo con trỏ
    # mycursor = db.cursor()

    # Truy vấn SELECT ALL từ bảng user
    code_select_all = "SELECT * FROM `user` WHERE taikhoan = %s AND matkhau = %s;"
    params = (tk, mk)  # Đặt giá trị tham số vào tuple
    mycursor.execute(code_select_all ,params)

    # Lấy tất cả các dòng kết quả
    result = mycursor.fetchall()
    # In ra tất cả các dòng kết quả
    for row in result:
        userDao = User(row[0] ,row[1] ,row[2])

    if not result:
        print("đăng nhập thất bại")
        return None
    else:
        print("đăng nhập thành công")
        return userDao

def getAllData():
    code_select_all = "SELECT * FROM `data`;"
    mycursor.execute(code_select_all)
    # Lấy tất cả các dòng kết quả
    result = mycursor.fetchall()

    return result

def insertData(nhietdo , doam , doamdat):
    code_insert_data = "INSERT INTO `iot`.`data`(`temperature`,`humidity`,`soilMoisture`)VALUES(%s , %s , %s);"
    params = (nhietdo, doam ,doamdat)  # Đặt giá trị tham số vào tuple
    mycursor.execute(code_insert_data ,params)
    db.commit()

def TBC100DataNew():
    code_select_all = """SELECT AVG(temperature) AS avg_temperature, AVG(humidity) AS avg_humidity
                         FROM (
                           SELECT temperature, humidity
                           FROM `data`
                           ORDER BY `id` DESC
                           LIMIT 1000
                         ) AS subquery;"""
    mycursor.execute(code_select_all)
    result = mycursor.fetchall()

    return result
    
# Machine learning
def dudoan():

    X = [[25, 65], [30, 70], [20, 60], [28, 68]]  # Nhiệt độ và độ ẩm không khí
    y = ['Rau A', 'Rau B', 'Rau C', 'Rau D']  # Loại rau tương ứng

    # Huấn luyện mô hình
    model = DecisionTreeClassifier()
    model.fit(X, y)

    # Dữ liệu mới để dự đoán
    new_data = TBC100DataNew()  # Nhiệt độ và độ ẩm không khí mới
    # new_data = [(22.189000000000025, 77.02)]

    # Dự đoán loại rau
    prediction = model.predict(new_data)

    # Kết quả
    print(f"Loại rau nên trồng: {prediction}")

    # Tên các loại rau
    loai_rau = {
        'Rau A': 'Cải Xoăn',
        'Rau B': 'Rau Mùi',
        'Rau C': 'Rau Ngót',
        'Rau D': 'Rau Răm',
    }

    # In tên loại rau dự đoán
    print(f"Tên loại rau: {loai_rau[prediction[0]]}")
    return loai_rau[prediction[0]]
    
def main():
    # Gọi hàm để tạo schema và chèn dữ liệu
    # create_schema_and_insert_data()

    # Gọi hàm để thực hiện truy vấn SELECT ALL
    # select_all_from_user()
    # print(checkLogin("admin" , "123"))
    # insertUser()
    # a = checkLogin("admin" , "123456")
    # print(TBC100DataNew())
    # print(dudoan())
    print(checkLogin("admin" ,"e10adc3949ba59abbe56e057f20f883e"))

if __name__ == "__main__":
    main()
