from dagster import op
import paramiko

@op
def dbt_run_ssh():
    client = paramiko.SSHClient()
    hostname =""
    username ="ec2-user"
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    run_command= " cd dbt_repo/dbt-dagster/dbt_test_mode; nohup dbt run"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, key_filename=key_path)
    channel = client.get_transport().open_session()
    pty = channel.get_pty()
    shell = client.invoke_shell()
    shell.send(run_command)
