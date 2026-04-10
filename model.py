def calculate_risk(rainfall):
    if rainfall < 20:
        return "Low"
    elif rainfall < 50:
        return "Medium"
    else:
        return "High"