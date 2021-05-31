import subprocess
import datetime
import os
from sqlalchemy import create_engine

def run_command(command):
    return subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).stdout.read()




print("Script started at {}".format(datetime.datetime.now()))
cpu = run_command("top -b -n 1 -d1 | grep \"Cpu(s)\" | awk '{printf \"%.1f\",$2}'")
memory = run_command("free -m | awk 'NR==2{printf \"%s\",$3}'")
disk = run_command("df -h | awk \'$NF==\"/\"{printf \"%s\",$3}\'")
time=datetime.datetime.now().replace(microsecond=0)

db_string = "postgresql://postgres:postgres@database:5432/postgres"

db = create_engine(db_string)
values=(time,cpu.decode(),disk.decode(),memory.decode())
# Create 
db.execute("CREATE TABLE IF NOT EXISTS Stat (time DateTime, cpu String, disk String, memory String)")
db.execute('''INSERT INTO Stat (time,cpu,disk,memory) VALUES (%s,%s,%s,%s)''',values)

