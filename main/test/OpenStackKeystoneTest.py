'''
OpenStack Python开发测试：
创建项目（project）
wy-2016-12-13
'''

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
auth = v3.Password(auth_url="http://192.168.245.132:5000/v3", username="admin",
                    password="admin", project_name="admin",
                     user_domain_id="default", project_domain_id="default")
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)
keystone.projects.list()

project = keystone.projects.create(name="test1", description="My new Project!", domain="default", enabled=True)
project.delete()