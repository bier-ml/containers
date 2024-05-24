import os
c = get_config()

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_connect_ip = '127.0.0.1'

c.JupyterHub.db_url = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@postgres:5432/{os.environ['POSTGRES_DB']}"