import psutil
import time
import argparse


def monitor_resources(pid):
    try:
        parent_process = psutil.Process(pid)
        print(f"Monitoring process ID: {parent_process.pid}")

        while parent_process.is_running():
            children = parent_process.children(recursive=True)
            process_map = {parent_process.pid: parent_process}
            for child in children:
                process_map[child.pid] = child

            total_cpu_percent = 0.0
            total_memory_usage = 0.0
            total_cpu_num = []
            total_num_threads = 0
            total_open_files = 0
            total_ctx_switches = 0

            for p in process_map.values():
                try:
                    proc_info = p.as_dict(
                        attrs=[
                            "cpu_percent",
                            "memory_info",
                            "cpu_num",
                            "num_threads",
                            "open_files",
                            "num_ctx_switches",
                        ]
                    )

                    total_cpu_percent += proc_info["cpu_percent"]
                    total_memory_usage += proc_info["memory_info"].rss / (1024 * 1024)
                    total_cpu_num.append(proc_info["cpu_num"])
                    total_num_threads += proc_info["num_threads"]
                    total_open_files += (
                        len(proc_info["open_files"]) if proc_info["open_files"] else 0
                    )
                    total_ctx_switches += (
                        proc_info["num_ctx_switches"].voluntary
                        + proc_info["num_ctx_switches"].involuntary
                    )

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            print(f"CPU Usage (%): {total_cpu_percent}")
            print(f"Memory Usage (MB): {total_memory_usage}")
            print(f"CPU Num: {total_cpu_num}")
            print(f"Num Threads: {total_num_threads}")
            print(f"Open Files: {total_open_files}")
            print(f"Context Switches: {total_ctx_switches}")
            print(f"Child Processes: {len(children)}")
            print("-" * 40)

            time.sleep(1)

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print("Process not found or access denied.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Monitor resource usage of a process by PID."
    )
    parser.add_argument("pid", type=int, help="The PID of the process to monitor.")
    args = parser.parse_args()

    monitor_resources(args.pid)
