from datetime import datetime

# ---------------------------------------------------------
# Simple Surf Engine for Dog Beach
# ---------------------------------------------------------

def get_surf_conditions(date=None):
    if date is None:
        date = datetime.now()

    # Placeholder logic for now – later we can wire real data
    breakers_ft = 2.5          # breaker height in feet
    sets_per_min = 3           # wave sets per minute
    surf_temp_f = 57           # water temperature in °F

    # Simple surf energy estimate
    # Energy ~ height^2 * sets
    surf_energy = round(breakers_ft ** 2 * sets_per_min * 6, 1)  # arbitrary scaling

    # Fishability score (0–100)
    score = 50

    if 2 <= breakers_ft <= 4:
        score += 20
    elif 1 <= breakers_ft < 2:
        score += 10

    if 2 <= sets_per_min <= 4:
        score += 15
    elif 1 <= sets_per_min < 2:
        score += 5

    if 55 <= surf_temp_f <= 62:
        score += 10

    score = min(score, 100)

    # GO / CAUTION / NO-GO
    if score >= 70:
        go_status = "GO"
    elif score >= 50:
        go_status = "CAUTION"
    else:
        go_status = "NO-GO"

    return {
        "breakers": f"{breakers_ft:.1f} ft",
        "sets": f"{sets_per_min} / min",
        "surf_temp": f"{surf_temp_f}°F",
        "surf_energy": f"{surf_energy} kJ",
        "fishability_score": score,
        "go_status": go_status,
    }
