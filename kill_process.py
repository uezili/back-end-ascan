import subprocess

pid = None
port = None


def get_pid():
    global password, pid, port
    port = str(input("Enter the port number to stop the process: "))
    process = subprocess.run(["sudo", "-S", "lsof", "-i", f"tcp:{port}"], input=password.encode(),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

    if process.stdout:
        pid = str(process.stdout).split()
        pid = pid[9]
        print(f"The PID code that process running on port {port} is {pid}")
        return True
    else:
        return False


def kill_process():
    global password, pid
    # pid = int(input("Enter the PID of the process to kill: "))
    # Execute o comando 'sudo lsof -t tcp:port'
    process = subprocess.Popen(["sudo", "-S", "kill", "-9", str(pid)],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    process.communicate(password.encode())
    print("Process with PID", pid, "killed successfully.")


if __name__ == '__main__':
    password = input("Enter the superuser password: ")

    pid_cod = get_pid()
    if pid_cod:
        kill_process()
    else:
        print(f"Don't have process on port {port}")
