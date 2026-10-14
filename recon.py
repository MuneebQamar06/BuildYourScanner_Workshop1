import socket

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0

def run_recon(target, results):
    for port in range(1, 101):
        if scan_port(target, port):
            results["ports"].append(port)
    return results

if __name__ == "__main__":
    test_results = {"target": "127.0.0.1", "ports": [], "services": {}}
    print(run_recon("127.0.0.1", test_results))