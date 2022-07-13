from dagster import op
import paramiko

@op
def dbt_run_ssh():
    client = paramiko.SSHClient()
    hostname ="ec2-34-244-209-39.eu-west-1.compute.amazonaws.com"
    username ="ec2-user"
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    run_command= "nohup bash /home/ec2-user/run_job.sh &"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, key_filename=key_path)
    channel = client.get_transport().open_session()
    pty = channel.get_pty()
    shell = client.invoke_shell()
    shell.send(run_command)
