#__author__:ipharmacare
# 2020/9/8

ip='10.1.1.116'
system_port=9999
interface_port=2002
linux_port=22


login_api='syscenter/api/v1/currentUser'
username='admin'
password='ipharmacare'

username_linux = 'root'
password_linux = 'ipharmacare'

cfg_api='sysConfig/update'
cfg_key=['commons_old_version_interface_enable','sf_unicom_enable','filter_valid_data','gy_result_by_prescription_enable','gy_temporary_orders_effective_once_enable','gy_long_orders_valid_time_scope']
cfg_value=['true','false','true,true','false,false']
cfg_id=[27,29,47,61,1173]

interface_api='face'
service_code=['GY_SF_V4','SF_V4_AUDIT_CENTER','SF_V4_VALID_FLAG']

interface_path="data/interface/interface_unified/in_out_bak"

#存放落地文件中要校验的字段
check_tag=["drug_return_flag","despensing_num","order_status","recipe_status","order_status","drug_name"]