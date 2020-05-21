# coding:utf-8
import re
import pymssql
dbinfo = {
    "server": "114.115.153.29",
    "user": "sa",
    "password": "qwe@58jzr"
}
class DbConnect():
    def __init__(self,db_cof,database):
        self.db_cof = db_cof
        # 数据库连接
        try:
            self.db = pymssql.connect(database=database,
                                      **db_cof)
        except Exception as a:
            print("数据库连接异常：%s" % a)
        self.cursor = self.db.cursor()

    def select(self,sql):
        # SQL查询语句
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except Exception as a:
            print("执行SQL查询语句出现异常：%s" % a)
        return results

    def execute(self,sql):
        # SQL 删除、添加、修改语句
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as a:
            self.db.rollback()
            print("执行SQL增改删出现异常：%s" % a)

    def close(self):
        self.db.close()

def select_sql(select_sql):
    '''查询数据库'''
    db = DbConnect(dbinfo, database="JZRZP_V1_KF")
    result = db.select(select_sql) #查询
    db.close()
    return result

def execute_sql(exe_sql):
    '''执行sql'''
    db = DbConnect(dbinfo, database="JZRZP_V1_KF")
    db.execute(exe_sql)
    db.close()

def table_exists(m, table_name):
    '''判断表是否存在'''
    sql_table = "show tables;"
    m.execute(sql_table)
    tables = [m.cursor.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return 1  # 存在返回1
    else:
        return 0  # 不存在返回0

if __name__ == "__main__":
    db = DbConnect(dbinfo, database="JZRZP_V1_KF")
    # # 判断是否存在表
    # table_name = 'linguser'
    # if (table_exists(db, table_name) != 1):
    #     sql_create = "create table linguser(id INT primary key NOT NULL AUTO_INCREMENT,username VARCHAR(32),password VARCHAR(32));"
    #     db.execute(sql_create)
    # else:
    #     pass
    #
    # insert_sql = '''insert into linguser(`username`,`password`) values('lsird','s34sd');'''
    # db.execute(insert_sql) # 插入数据
    delete_sql = '''DELETE FROM [User] WHERE Phone = 18328015689'''
    execute_sql(delete_sql)
    # sel_sql = '''select * from [User];'''
    # result = db.select(sel_sql)
    # print(result)
    # db.close()

# import pymysql
# '''
# pip install PyMySQL==0.9.3
# '''
#
# dbinfo = {
#     "host": "49.235.92.12",
#     "user": "root",
#     "password": "123456",
#     "port": 3309}
#
#
# class DbConnect():
#     def __init__(self, db_cof, database=""):
#         self.db_cof = db_cof
#         # 打开数据库连接
#         self.db = pymysql.connect(database=database,
#                                   cursorclass=pymysql.cursors.DictCursor,
#                                   **db_cof)
#
#         # 使用cursor()方法获取操作游标
#         self.cursor = self.db.cursor()
#
#     def select(self, sql):
#         # SQL 查询语句
#         # sql = "SELECT * FROM EMPLOYEE \
#         #        WHERE INCOME > %s" % (1000)
#         self.cursor.execute(sql)
#         results = self.cursor.fetchall()
#         return results
#
#     def execute(self, sql):
#         # SQL 删除、提交、修改语句
#         # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
#         try:
#            # 执行SQL语句
#            self.cursor.execute(sql)
#            # 提交修改
#            self.db.commit()
#         except:
#            # 发生错误时回滚
#            self.db.rollback()
#
#     def close(self):
#         # 关闭连接
#         self.db.close()
#
# def select_sql(select_sql):
#     '''查询数据库'''
#     db = DbConnect(dbinfo, database="apps")
#     result = db.select(select_sql)  # 查询
#     db.close()
#     return result
#
# def execute_sql(insert_sql):
#     '''执行sql'''
#     db = DbConnect(dbinfo, database="apps")
#     db.execute(insert_sql)  # 查询
#     db.close()
#
#
# if __name__ == '__main__':
#     # db = DbConnect(db_cof=dbinfo, database="apps")
#     # sql = 'SELECT * from auth_user WHERE username="test";'
#     # result = db.select(select_sql)
#     # print(result[0]["username"])
#     sql = 'SELECT * from auth_user WHERE username="test";'
#     a = select_sql(sql)
#     print(a)
