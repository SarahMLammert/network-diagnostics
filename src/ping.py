"""
Ping execution utilities.

Builds and runs system ping commands for MacOS/Linux and returns
raw command output without parsing.
"""
import platform
import subprocess

def build_ping_cmd(host: str, count: int, timeout: int) -> list[str]:
    """
    Builds a platform specific ping command.

    On MacOS, timeout is converted to milliseconds.
    On Linux, timeout is in seconds.
    """
    system = platform.system()
    if system == "Darwin": # MacOS
        timeout_ms = timeout * 1000
        return ["ping", "-c", str(count), "-W", str(timeout_ms), host]

    elif system == "Linux":
        return ["ping", "-c", str(count), "-W", str(timeout), host]

    else:
        raise NotImplementedError(f"Unsupported OS: {system}")


def run_ping(cmd: list[str], timeout: int) -> tuple[str, str, int]:
    """
    Executes a ping command and returns raw stdout, stderr, and exit code
    """
    try:
        result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout,
        check=False
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as e:
        return e.stdout or "", "Ping command timed out", 1
