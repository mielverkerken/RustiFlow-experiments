import subprocess
import os
import time
import signal


def main():
    # Command to run your bash script
    cmd = ["./argus_script_realtime.sh"]

    # Start the script in a new process group
    # so we can send signals to the entire group.
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        preexec_fn=os.setsid,
    )
    print(f"Started script. PID={proc.pid}")

    # Wait for 10 seconds
    time.sleep(10)

    print("Stopping script...")
    # Send SIGTERM to the entire process group
    pgid = os.getpgid(proc.pid)
    os.killpg(pgid, signal.SIGTERM)

    # Optionally wait for the process to exit; if it doesn’t exit,
    # send SIGKILL as a last resort.
    try:
        proc.wait(timeout=5)
        print("Script terminated gracefully.")
    except subprocess.TimeoutExpired:
        print("Script did not terminate; sending SIGKILL...")
        os.killpg(pgid, signal.SIGKILL)
        proc.wait()
        print("Script terminated with SIGKILL.")


if __name__ == "__main__":
    main()
