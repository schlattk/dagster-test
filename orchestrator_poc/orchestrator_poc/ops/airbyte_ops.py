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
def airbyte_ssh():
    client = paramiko.SSHClient()
    hostname =""
    username =""
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    url = "localhost:8000/api/v1/connections/sync"
    connection = '{"connectionId": "c1a5fdf3-903f-4d86-8601-5b6462afe40e"}'
    sync_query = "curl -X POST -H 'Content-Type: application/json' -d '@/home/ec2-user/salesforce.json' http://localhost:8000/api/v1/connections/sync > response.txt"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, key_filename=key_path)
    client.exec_command('touch before.txt')
    client.exec_command(sync_query)
    client.exec_command('touch after.txt')
    client.close()

@op
def ssh():
    client = paramiko.SSHClient()
    hostname = "ec2-52-215-25-222.eu-west-1.compute.amazonaws.com"
    username = "ec2-user"
    key_path = "/home/ec2-user/.ssh/airbyte_key"
    url = "localhost:8000/api/v1/connections/sync"
    connection = '{"connectionId": "c1a5fdf3-903f-4d86-8601-5b6462afe40e"}'
    sync_query = "curl -X POST -H 'Content-Type: application/json' -d '@/home/ec2-user/salesforce.json' http://localhost:8000/api/v1/connections/sync > response.txt"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, key_filename=key_path)
    client.exec_command('touch before.txt')
