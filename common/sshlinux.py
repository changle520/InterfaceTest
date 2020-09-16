#__author__:ipharmacare
# 2020/9/10
import paramiko
from config import linux_port,username_linux,password_linux,ip

def get_file(src,dct='../../data/innerIn/'):
    '''
    远程连接linux服务器，下载文件到本地
    args:
        src:服务器上的文件路径
        dct:本地路径
    '''

    t=paramiko.Transport(ip,linux_port)
    t.connect(username=username_linux,password=password_linux)  #登录远程服务器
    sftp=paramiko.SFTPClient.from_transport(t)      #sftp传输协议
    timeid_dir=sftp.listdir(src)   #获取路径下时间生成的id目录
    src=src+timeid_dir[-1]+'/'     #将获取的id目录拼接到src的后面
    file_name=sftp.listdir(src)    #获取内部入参的落地文件名称
    IN_file=(file_name[0] if file_name[0].startswith('IN') else file_name[1])           #获取file_name中入参的那个文件:IN开头的
    src=src+IN_file         #将文件名称拼接到src后面
    dct=dct+IN_file           #将文件名称拼接到本地目录的后面
    # print(src,dct)
    sftp.get(src,dct)              #将落地文件下载到本地
    t.close()
    return dct

if __name__ == '__main__':
    get_file('/data/interface/interface_unified/in_out_bak/2020-09-10/H0003/REAL_OPT/test_opt_002/INNER_AUDIT_CENTER')