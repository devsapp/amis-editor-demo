import subprocess
import time
import os
import shutil


eve_app = 'start-amis-editor'
print("----------------------: ", eve_app)

os.chdir('../')
os.makedirs("_tmp", exist_ok=True)
os.rename('amis-editor-demo', "_tmp/src")
os.rename("_tmp", 'amis-editor-demo')
shutil.move("./amis-editor-demo/src/publish.yaml", "./amis-editor-demo/publish.yaml")

publish_script = 'https://serverless-registry.oss-cn-hangzhou.aliyuncs.com/publish-file/python3/hub-publish.py'
command = 'cd ./amis-editor-demo && wget %s && python hub-publish.py' % (publish_script)
child = subprocess.Popen(
    command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, )
stdout, stderr = child.communicate()
if child.returncode == 0:
    print("stdout:", stdout.decode("utf-8"))
else:
    print("stdout:", stdout.decode("utf-8"))
    print("stderr:", stderr.decode("utf-8"))
    raise ChildProcessError(stderr)