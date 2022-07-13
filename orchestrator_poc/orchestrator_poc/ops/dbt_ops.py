from dagster import op
import paramiko

@op
def dbt_run_ssh():
    client = paramiko.SSHClient()
    hostname ="$DBT_SSH_HOST"
    username ="$DBT_SSH_USER"
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    run_command= "cd dbt_repo && dbt run"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, key_filename=key_path)
    client.exec_command('touch before.txt')
    client.exec_command(run_command)
    client.exec_command('touch after.txt')
    client.close()
