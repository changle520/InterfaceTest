#__author__:ipharmacare
# 2020/9/8

ip='10.1.1.116'
system_port=9999
interface_port=2002
linux_port=22

#业务系统的登录接口及登录账号
login_api='syscenter/api/v1/currentUser'
username='admin'
password='ipharmacare'

#服务器的账号
username_linux = 'root'
password_linux = 'ipharmacare'

#统一接口数据库的相关配置
mysql_host='10.1.1.118'
mysql_port=3306
mysql_username='yyuser'
mysql_password='iPh@23ysq!'
database='ipharmacare_pull'

#用户中心配置项的数据
cfg_api='sysConfig/update'
cfg_key=['commons_old_version_interface_enable','sf_unicom_enable','filter_valid_data','gy_result_by_prescription_enable','gy_temporary_orders_effective_once_enable','gy_long_orders_valid_time_scope']
cfg_value=['true','false','true,true','false,false']

#统一接口相关
interface_api='face'
service_code=['GY_SF_V4','SF_V4_AUDIT_CENTER','SF_V4_VALID_FLAG']

interface_path="data/data/interface_bak/interface_unified/in_out_bak"

#存放落地文件中要校验的字段
check_tag=["drug_return_flag","despensing_num","order_status","recipe_status","order_status","drug_name","error_info"]

#测试用例文件相关
testfile='../data/统一接口自动化测试用例.xls'
target_file='../data/innerIn/'
sheetname=['4.0_old','4.0_new']

#审方系统接口相关配置
startAudit_api="auditcenter/api/v1/startAuditWork"
endAudit_api="auditcenter/api/v1/endAuditWork"
sfAuditList_api='auditcenter/api/v1/ipt/selNotAuditIptList'
