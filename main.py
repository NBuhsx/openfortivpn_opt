import json
import pyotp
import subprocess


def main():
    with open(file="config.json", mode="r") as file:
        config = json.load(file)

    code = pyotp.parse_uri(config["opt"])
    print(f"OTP: {code}")
    subprocess.run(
        [
            "sudo",
            "openfortivpn",
            f"{config['host']}:{config['port']}",
            f"--username={config['user']}",
            f"--password={config['password'] + code.now()}",
            f"--trusted-cert={config['trusted-cert']}"
        ])
    exit()


if __name__ == "__main__":
    main()
