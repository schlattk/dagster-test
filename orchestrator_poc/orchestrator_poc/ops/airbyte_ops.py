from dagster import op
from dagster_airbyte import airbyte_sync_op
import paramiko

sync_google = airbyte_sync_op.configured(
    {"connection_id": "some-connection-id"},
    name="google"
)

sync_salesforce = airbyte_sync_op.configured(
    {"connection_id": "c1a5fdf3-903f-4d86-8601-5b6462afe40e"},
    name="salesforce_stronger_nudge"
)

@op
def ssh():
    ssh = paramiko.SSHClient()
    hostname = "ec2-52-215-25-222.eu-west-1.compute.amazonaws.com"
    username = "ec2-user"
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    url = "localhost:8000/api/v1/connections/sync"
    connection = "{\"connectionId\": \"c1a5fdf3-903f-4d86-8601-5b6462afe40e\"}"
    curl_command = f"""curl -X POST {url} \
                            -H 'Content-Type: application/json' \
                            -d {connection} \
                            > error.txt
                    """
    sync_query = "curl -X POST localhost:8000/api/v1/connections/sync -H 'Content-Type: application/json' -d '{\"connectionId\": \"c1a5fdf3-903f-4d86-8601-5b6462afe40e\"}'"
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, key_filename=key_path)
    except:
        print('connection failed')
    try:
        ssh.exec_command('touch before.txt')
        ssh.exec_command(curl_command)
        ssh.exec_command('touch after.txt')
    except:
        ssh.exec_command('touch error.txt')
    ssh.close()
