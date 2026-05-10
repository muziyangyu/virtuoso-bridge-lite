#!/usr/bin/env python3
"""Find SMIC Spectre model file on remote host."""
from virtuoso_bridge.transport.tunnel import SSHClient

ssh = SSHClient.from_env(keep_remote_files=True)
try:
    ssh.warm()
    runner = ssh.ssh_runner
    runner._verbose = False
    # Search for SMIC Spectre models
    result = runner.run_command(
        'find /mnt/data -name "*.scs" -path "*[Ss][Mm][Ii][Cc]*" 2>/dev/null | head -10',
        timeout=30,
    )
    print("SMIC .scs files:")
    for line in result.stdout.splitlines():
        print(f"  {line.strip()}")
finally:
    ssh.close()
