import time
import requests

BASE_URL = "http://localhost:8000"


def wait_for_service(timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(f"{BASE_URL}/health")
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False


if __name__ == "__main__":
    print("Waiting for service to start...")
    if not wait_for_service():
        raise SystemExit("Service did not start in time.")

    print("Sending smoke test request...")
    response = requests.post(f"{BASE_URL}/predict", json={"feature": "smoketest"})

    if response.status_code != 200:
        raise SystemExit(f"Smoke test FAILED with status: {response.status_code}")

    print("Smoke test PASSED:", response.json())
