import click
from .health_checker import HealthChecker

@click.group()
def cli():
    pass

@cli.command()
def check():
    checker = HealthChecker()
    print(checker.generate_health_report())

@cli.command()
def monitor():
    print("Monitoring...")

@cli.command()
def ssh_status():
    print("SSH status...")

@cli.command()
def alerts():
    print("Alerts...")

@cli.command()
def vms():
    print("VMs...")

if __name__ == '__main__':
    cli()
