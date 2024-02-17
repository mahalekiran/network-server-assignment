import requests
import time
from tabulate import tabulate

def check_subdomain_status(subdomains):
    results = []
    for subdomain in subdomains:
        url = f"http://{subdomain}"
        try:
            response = requests.get(url, timeout=5)
            status = str(response.status_code) + " - Up"
        except requests.ConnectionError:
            status = "Down"
        results.append((subdomain, status))
    return results

def display_results(results):
    headers = ["Subdomain", "Status"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

def main():
    try:
        subdomains = ["b.iana-servers.net.", "www.wikipedia.org", "subdomain1.example.com", "www.example.com"]
        while True:
            results = check_subdomain_status(subdomains)
            display_results(results)
            time.sleep(60)  # automatically check the status every minute
    except Exception as error:
        print("Some error occurred: "+ str(error))
    except KeyboardInterrupt as key:
        print("Keyboard Interrupt: "+str(key))


if __name__ == "__main__":
    main()
