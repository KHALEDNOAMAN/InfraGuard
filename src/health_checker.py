import psutil
import socket

class HealthChecker:
    def check_cpu(self, threshold=80):
        cpu = psutil.cpu_percent(interval=1)
        return cpu < threshold, cpu

    def check_memory(self, threshold=85):
        mem = psutil.virtual_memory().percent
        return mem < threshold, mem

    def check_disk(self, threshold=90):
        disk = psutil.disk_usage('/').percent
        return disk < threshold, disk

    def check_network_connectivity(self, hosts):
        results = {}
        for host in hosts:
            try:
                socket.create_connection((host, 80), timeout=2)
                results[host] = True
            except OSError:
                results[host] = False
        return results

    def check_process(self, name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == name:
                return True
        return False

    def check_port(self, host, port):
        try:
            socket.create_connection((host, port), timeout=2)
            return True
        except OSError:
            return False

    def generate_health_report(self):
        cpu_ok, cpu = self.check_cpu()
        mem_ok, mem = self.check_memory()
        disk_ok, disk = self.check_disk()
        score = 100
        if not cpu_ok: score -= 20
        if not mem_ok: score -= 20
        if not disk_ok: score -= 20
        return {"score": score, "cpu": cpu, "memory": mem, "disk": disk}
