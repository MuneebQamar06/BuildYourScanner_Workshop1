def generate_report(results):
    print("=" * 30)
    print("SCAN REPORT")
    print("=" * 30)
    print("Target:", results["target"])
    print("Open ports found:", len(results["ports"]))
    print()

    if len(results["ports"]) == 0:
        print("No open ports found.")
    else:
        for port in results["ports"]:
            service = results["services"][port]
            print("Port", port, "-", service)
            input("Press Enter to continue...")