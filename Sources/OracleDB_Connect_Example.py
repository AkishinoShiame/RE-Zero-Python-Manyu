import cx_Oracle
conn = cx_Oracle.connect('admin/pa$$w0rd@127.0.0.1:1521/test')


cursor = conn.cursor()
cursor.execute("select * from new_table where key in ( 41001, 41003, 41004, 41005) and temp_status = 1")

result = cursor.fetchall()
print(result)