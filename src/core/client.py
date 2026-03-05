import os
import subprocess


def query(prompt: str) -> str:
    env = os.environ.copy()
    env.pop("CLAUDECODE", None)

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        env=env
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude CLI error:\nSTDERR: {result.stderr}\nSTDOUT: {result.stdout}")
    return result.stdout.strip()
