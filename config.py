import pymysql

DATABASE = "medical"
IMAGE_TABLE_NAME = "medical_storage"
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database=DATABASE,
    cursorclass=pymysql.cursors.DictCursor,
)
