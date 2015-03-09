import pymysql
conn = pymysql.connect(host='localhost', user='milad', passwd='*23AE809DDACAF96AF0FD78ED04B6A265E05AA257', db='mysql')
cur = conn.cursor()

cur.execute("SELECT * FROM ")

print(cur.description)

print()

for row in cur:
   print(row)

cur.close()
conn.close()
