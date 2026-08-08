import random


def check_security(cloud):

    alerts = []

    # Generate random demo security values
    firewall = random.choice(["Public", "Private"])
    bucket = random.choice(["Public", "Private"])

    if firewall == "Public":
        alerts.append("⚠ Public Firewall")

    if bucket == "Public":
        alerts.append("⚠ Public Storage Bucket")

    issue_count = len(alerts)

    if issue_count == 0:
        alerts.append("✅ No Security Issues")

    score = 100 - (issue_count * 20)

    return {
        "cloud": cloud["cloud"],
        "score": score,
        "alerts": alerts
    }