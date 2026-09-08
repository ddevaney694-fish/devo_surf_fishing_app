import requests
from datetime import datetime, timedelta
import pytz

PRIMARY_BUOY = "46028"   # Point San Luis
BACKUP_BUOY  = "46011"   # San Simeon

# Breaker multiplier chosen by Doug
BREAKER_MULTIPLIER = 0.55


# ---------------------------------------------------------
# Fetch NOAA buoy JSON safely
# ---------------------------------------------------------

def fetch_buoy_json(buoy_id):
    url = f"https://www.ndbc.noaa.gov/data/realtime2/{buoy_id}.json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


# ---------------------------------------------------------
# Validate buoy data
# ---------------------------------------------------------

def validate_buoy_data(data):
    if not data or "data" not in data or len(data["data"]) == 0:
        return None

    latest = data["data"][0]

    # NOAA uses "MM" for missing values
    wave_height = latest.get("WVHT")
    wave_period = latest.get("DPD")
    temp_c      = latest.get("WTMP")
    timestamp   = latest.get("time")

    if wave_height in ["MM", None] or wave_period in ["MM", None] or temp_c in ["MM", None]:
        return None

    try:
        wave_height = float(wave_height)
        wave_period = float(wave_period)
        temp_c      = float(temp_c)
    except:
        return None

    # Zero values are invalid
    if wave_height <= 0 or wave_period <= 0:
        return None

    # Timestamp check (must be < 3 hours old)
    try:
        utc = pytz.utc
        buoy_time = utc.localize(datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ"))
        pst = pytz.timezone("America/Los_Angeles")
        buoy_time_pst = buoy_time.astimezone(pst)

        if datetime.now(pst) - buoy_time_pst > timedelta(hours=3):
            return None
    except:
        return None

    return {
        "wave_height_ft": wave_height * 3.28084,  # meters → feet
        "wave_period_sec": wave_period,
        "temp_f": round((temp_c * 9/5) + 32),
        "timestamp_pst": buoy_time_pst.strftime("%A %I:%M %p"),
    }


# ---------------------------------------------------------
# Try primary → backup → synthetic fallback
# ---------------------------------------------------------

def get_noaa_buoy_data():
    # Try primary buoy
    primary_raw = fetch_buoy_json(PRIMARY_BUOY)
    primary = validate_buoy_data(primary_raw)

    if primary:
        return primary

    # Try backup buoy
    backup_raw = fetch_buoy_json(BACKUP_BUOY)
    backup = validate_buoy_data(backup_raw)

    if backup:
        return backup

    # Synthetic fallback
    return {
        "wave_height_ft": 4.0,
        "wave_period_sec": 10,
        "temp_f": 57,
        "timestamp_pst": "Synthetic Fallback",
    }


# ---------------------------------------------------------
# Main Surf Engine
# ---------------------------------------------------------

def get_surf_conditions():
    buoy = get_noaa_buoy_data()

    # Convert buoy → Dog Beach breakers
    breakers_ft = round(buoy["wave_height_ft"] * BREAKER_MULTIPLIER, 1)

    # Convert wave period → sets per minute
    sets_per_min = max(1, round(60 / buoy["wave_period_sec"]))

    # Surf energy
    surf_energy = round(breakers_ft**2 * sets_per_min * 6, 1)

    # Fishability score
    score = 50

    if 2 <= breakers_ft <= 4:
        score += 20
    elif 1 <= breakers_ft < 2:
        score += 10

    if 2 <= sets_per_min <= 4:
        score += 15
    elif 1 <= sets_per_min < 2:
        score += 5

    if 55 <= buoy["temp_f"] <= 62:
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
        "surf_temp": f"{buoy['temp_f']}°F",
        "surf_energy": f"{surf_energy} kJ",
        "fishability_score": score,
        "go_status": go_status,
        "buoy_time": buoy["timestamp_pst"],
        "buoy_source": PRIMARY_BUOY if buoy["timestamp_pst"] != "Synthetic Fallback" else "Fallback",
    }
