import paramiko

class SSHMonitor:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, host, user, key_path):
        self.client.connect(host, username=user, key_filename=key_path)

    def execute_command(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode('utf-8').strip()

    def get_remote_stats(self):
        cpu = self.execute_command("top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'")
        mem = self.execute_command("free -m | awk 'NR==2{printf \"%.2f\", $3*100/$2 }'")
        disk = self.execute_command("df -h | awk '$NF==\"/\"{printf \"%s\", $5}'")
        return {"cpu": cpu, "mem": mem, "disk": disk}

    def get_running_services(self):
        return self.execute_command("systemctl list-units --type=service --state=running")

    def get_system_logs(self, lines=50):
        return self.execute_command(f"tail -n {lines} /var/log/syslog")

    def batch_check(self, hosts_list):
        results = {}
        for h in hosts_list:
            try:
                self.connect(h['host'], h['user'], h['key'])
                results[h['host']] = self.get_remote_stats()
            except Exception as e:
                results[h['host']] = {"error": str(e)}
        return results
