from datetime import datetime, timedelta
import math

# ---------------------------------------------------------
# Moon Phase Calculation
# ---------------------------------------------------------

def get_moon_phase(date=None):
    if date is None:
        date = datetime.now()

    diff = date - datetime(2001, 1, 1)
    days = diff.days + (diff.seconds / 86400)
    lunations = days / 29.53058867
    position = lunations % 1

    if position < 0.03 or position > 0.97:
        return "New Moon"
    elif position < 0.22:
        return "Waxing Crescent"
    elif position < 0.28:
        return "First Quarter"
    elif position < 0.47:
        return "Waxing Gibbous"
    elif position < 0.53:
        return "Full Moon"
    elif position < 0.72:
        return "Waning Gibbous"
    elif position < 0.78:
        return "Last Quarter"
    else:
        return "Waning Crescent"

# ---------------------------------------------------------
# Bite Window Calculation (simple model)
# ---------------------------------------------------------

def get_bite_windows(date=None):
    if date is None:
        date = datetime.now()

    major_start = date.replace(hour=10, minute=45)
    major_end   = date.replace(hour=12, minute=15)

    minor_start = date.replace(hour=17, minute=20)
    minor_end   = date.replace(hour=18, minute=5)

    return {
        "major": f"{major_start.strftime('%I:%M %p')} – {major_end.strftime('%I:%M %p')}",
        "minor": f"{minor_start.strftime('%I:%M %p')} – {minor_end.strftime('%I:%M %p')}",
        "major_count": 1,
        "minor_count": 1,
    }

# ---------------------------------------------------------
# Sunrise / Sunset (simple model)
# ---------------------------------------------------------

def get_sun_times(date=None):
    if date is None:
        date = datetime.now()

    sunrise = date.replace(hour=6, minute=45)
    sunset  = date.replace(hour=19, minute=25)

    return {
        "sunrise": sunrise.strftime("%I:%M %p"),
        "sunset": sunset.strftime("%I:%M %p"),
    }

# ---------------------------------------------------------
# Tide Stage (simple model)
# ---------------------------------------------------------

def get_tide_stage(date=None):
    if date is None:
        date = datetime.now()

    hour = date.hour

    if 4 <= hour < 10:
        return "Incoming Tide"
    elif 10 <= hour < 14:
        return "High Tide"
    elif 14 <= hour < 18:
        return "Outgoing Tide"
    elif 18 <= hour < 22:
        return "Low Tide"
    else:
        return "Slack Tide"

# ---------------------------------------------------------
# Bite Rating
# ---------------------------------------------------------

def get_bite_rating(phase):
    if phase in ["Full Moon", "New Moon"]:
        return "EXCELLENT"
    elif "Gibbous" in phase:
        return "GOOD"
    elif "Quarter" in phase:
        return "FAIR"
    else:
        return "POOR"

# ---------------------------------------------------------
# Solunar Score (0–100)
# ---------------------------------------------------------

def get_solunar_score(phase, tide_stage):
    score = 50

    if phase in ["Full Moon", "New Moon"]:
        score += 25
    elif "Gibbous" in phase:
        score += 15
    elif "Quarter" in phase:
        score += 5

    if tide_stage in ["Incoming Tide", "Outgoing Tide"]:
        score += 20
    elif tide_stage == "High Tide":
        score += 10

    return min(score, 100)

# ---------------------------------------------------------
# Main Solunar Engine
# ---------------------------------------------------------

def get_solunar_data():
    date = datetime.now()

    phase = get_moon_phase(date)
    windows = get_bite_windows(date)
    sun = get_sun_times(date)
    tide = get_tide_stage(date)
    rating = get_bite_rating(phase)
    score = get_solunar_score(phase, tide)

    return {
        "moon_phase": phase,
        "major_window": windows["major"],
        "minor_window": windows["minor"],
        "major_count": windows["major_count"],
        "minor_count": windows["minor_count"],
        "sunrise": sun["sunrise"],
        "sunset": sun["sunset"],
        "tide_stage": tide,
        "bite_rating": rating,
        "solunar_score": score,
    }
