def get_emergency_guidance(risk_level):
    """
    Converts model prediction into actionable guidance.
    """

    if risk_level == 0:
        return {
            "risk": "Normal",
            "message": "Vitals are stable. No immediate emergency detected.",
            "dos": [
                "Continue regular activities",
                "Stay hydrated",
                "Monitor vitals periodically"
            ],
            "donts": [
                "Ignore sudden symptoms",
                "Overexert physically"
            ],
            "alert": "NONE"
        }

    elif risk_level == 1:
        return {
            "risk": "Warning",
            "message": "Early signs of instability detected. Take precautions.",
            "dos": [
                "Sit or lie down safely",
                "Avoid physical exertion",
                "Keep phone accessible",
                "Monitor breathing and consciousness"
            ],
            "donts": [
                "Drive or operate machinery",
                "Stay alone for long periods"
            ],
            "alert": "LOW"
        }

    elif risk_level == 2:
        return {
            "risk": "High Emergency",
            "message": "Critical condition detected. Immediate action required.",
            "dos": [
                "Lie down immediately",
                "Call emergency services",
                "Inform nearby people",
                "Share live location with emergency contact"
            ],
            "donts": [
                "Delay seeking help",
                "Consume food or drink",
                "Attempt to walk alone"
            ],
            "alert": "HIGH"
        }

    else:
        return {
            "risk": "Unknown",
            "message": "Invalid risk level received.",
            "dos": [],
            "donts": [],
            "alert": "UNKNOWN"
        }
    
if __name__ == "__main__":
    for risk in [0, 1, 2]:
        print("\n--- RISK LEVEL:", risk, "---")
        guidance = get_emergency_guidance(risk)
        for key, value in guidance.items():
            print(f"{key}: {value}")


