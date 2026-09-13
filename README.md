# InfraGuard

Infrastructure Health Monitor.

## Features
- Server health checks
- Remote server monitoring via SSH
- VM/Container monitoring
- Alert system
- FastAPI dashboard

## Installation

```bash
pip install -r requirements.txt
python setup.py install
```


## Overview
Monitors infrastructure security compliance, detects misconfigurations

## Architecture
Scanner agents -> Analysis engine -> Dashboard

## Tech Stack
Python, FastAPI, React, Docker

## How It Works
Agents scan infrastructure -> Rules engine checks compliance -> Dashboard shows findings

## Usage
docker-compose up, open dashboard, configure targets, run scan

## Project Structure
- ackend/ (app/, scanners/, rules/)
- rontend/ (src/)
- docker/

## Future
CIS benchmarks, PCI-DSS checks, automated remediation, Slack alerts

## Screenshots
[ASCII compliance dashboard]