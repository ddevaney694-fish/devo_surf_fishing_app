from datetime import datetime, timedelta
import math

# ---------------------------------------------------------
# Moon Phase Calculation
# ---------------------------------------------------------

def get_moon_phase(date=None):
    if date is None:
        date = datetime.now()

    # Simple moon phase algorithm
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

    # Major window = moon overhead or underfoot
    major_start = date.replace(hour=10, minute=45)
    major_end   = date.replace(hour=12, minute=15)

    # Minor window = moon rise or set
    minor_start = date.replace(hour=17, minute=20)
    minor_end   = date.replace(hour=18, minute=5)

    return {
        "major": f"{major_start.strftime('%I:%M %p')} – {major_end.strftime('%I:%M %p')}",
        "minor": f"{minor_start.strftime('%I:%M %p')} – {minor_end.strftime('%I:%M %p')}",
    }

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
# Main Solunar Engine
# ---------------------------------------------------------

def get_solunar_data():
    date = datetime.now()

    phase = get_moon_phase(date)
    windows = get_bite_windows(date)
    rating = get_bite_rating(phase)

    return {
        "moon_phase": phase,
        "major_window": windows["major"],
        "minor_window": windows["minor"],
        "bite_rating": rating,
    }
