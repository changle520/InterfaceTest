#__author__:ipharmacare
# 2020/9/23

import pymysql
from config import mysql_host,mysql_port,mysql_username,mysql_password,database

class ConnectMySQL():
    '''连接数据库获取配置文件的id'''

    def openmysql(self):
        '''连接数据库'''

        self.conn=pymysql.Connect(host=mysql_host,port=mysql_port,user=mysql_username,passwd=mysql_password,database=database,charset='utf8')
        return self.conn

    def get_cursor(self,conn):
        '''获取游标'''

        self.cur=conn.cursor()
        return self.cur

    def get_data(self):
        conn=self.openmysql()
        cur=self.get_cursor(conn)
        cur.execute("SELECT config_key,id FROM `tb_sys_config` where config_key in ('commons_old_version_interface_enable','sf_unicom_enable','filter_valid_data','gy_result_by_prescription_enable','gy_temporary_orders_effective_once_enable','gy_long_orders_valid_time_scope');")
        return dict(cur.fetchall())

config_data=ConnectMySQL().get_data()
print(config_data)

# if __name__ == '__main__':
#     conn=ConnectMySQL()
#     print(dict(conn.get_data()))
