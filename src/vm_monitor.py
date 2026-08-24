import subprocess

class VMMonitor:
    def list_docker_containers(self):
        result = subprocess.run(["docker", "ps", "--format", "{{.ID}}:{{.Names}}"], capture_output=True, text=True)
        return result.stdout.strip().split("\n")

    def get_container_stats(self, container_id):
        result = subprocess.run(["docker", "stats", "--no-stream", "--format", "{{.CPUPerc}}:{{.MemUsage}}", container_id], capture_output=True, text=True)
        return result.stdout.strip()

    def check_container_health(self):
        return subprocess.run(["docker", "ps", "-f", "health=unhealthy"], capture_output=True, text=True).stdout

    def list_vms(self):
        # Placeholder for VBoxManage or virsh
        result = subprocess.run(["virsh", "list", "--all"], capture_output=True, text=True)
        return result.stdout.strip()

    def get_vm_resources(self):
        pass
