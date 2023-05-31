# find pin from database
def check_pin(pin):
    import mysql.connector as ms
    mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
    cur=mydb.cursor()
    cur.execute('select pin from cos_data')
    xpin=cur.fetchall()
    for i in xpin:
        if i[0]==pin:
            return i[0]
    else:
        return 'Wrong pin'

# return costumer detail
def detail(pin):
    import mysql.connector as sc
    mydb=sc.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
    mycur=mydb.cursor()
    mycur.execute(f'select * from cos_data where pin={pin}')
    info=mycur.fetchone()
    hideac=f"xxxxxx{info[0][-5:]}"
    x=f"Hi {info[1]}, Your A/c is {hideac} and your Avl_bal Rs.{info[3]}."
    return x

# return costumer balance
def balance(pin):
    import mysql.connector as sc
    mydb=sc.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
    mycur=mydb.cursor()
    mycur.execute(f'select balance from cos_data where pin={pin}')
    info=mycur.fetchone()
    x=info[0]
    return x

# update balance
def update_bal(amount,pin):
    import mysql.connector as sc
    mydb=sc.connect(host='localhost',user='root',password='Neeraj@123',database='atm_data')
    mycur=mydb.cursor()
    sql=f"update cos_data set balance={amount} where pin={pin}"
    mycur.execute(sql)
    mydb.commit()
    return 'Yes'