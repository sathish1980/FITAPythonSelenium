import cdata.mysql as mod
class mysql():

    def mysqlconnection(self):

        conn = mod.connect("User=user@domain.com; Password=password;")

        # Create cursor and iterate over results
        cur = conn.cursor()
        cur.execute("SELECT * FROM MySQLTable")

        rs = cur.fetchall()

        for row in rs:
            print(row)