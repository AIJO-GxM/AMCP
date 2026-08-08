def detect_drift(current, baseline):
    changes = []

    if current["firewall"] != baseline["firewall"]:
        changes.append(
            f"Firewall changed: {baseline['firewall']} → {current['firewall']}"
        )

    if current["bucket"] != baseline["bucket"]:
        changes.append(
            f"Bucket changed: {baseline['bucket']} → {current['bucket']}"
        )

    if len(changes) == 0:
        return {
            "cloud": current["cloud"],
            "drift": False,
            "changes": ["No configuration changes"]
        }

    return {
        "cloud": current["cloud"],
        "drift": True,
        "changes": changes
    }