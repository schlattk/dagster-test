from dagster import op
import paramiko

@op
def dbt_run_ssh():
    client = paramiko.SSHClient()
    hostname =""
    username ="ec2-user"
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    run_command= "bash /home/ec2-user/run_job.sh &"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, key_filename=key_path)
    transport = client.get_transport()
    channel = transport.open_session()
    channel.exec_command(run_command)
    client.close()
