from recon import run_recon
from analysis import analyse_results
from report import generate_report

def main():
    target = input("Enter target IP or hostname: ")

    results = {
        "target": target,
        "ports": [],
        "services": {}
    }

    results = run_recon(target, results)
    results = analyse_results(results)
    generate_report(results)

if __name__ == "__main__":
    main()