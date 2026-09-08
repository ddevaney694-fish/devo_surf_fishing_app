import requests
from datetime import datetime, timedelta
import pytz

# NOAA Tides & Currents station for Morro Bay
STATION_ID = "9412110"  # Morro Bay, CA

def fetch_tide_predictions():
    """
    Fetch today's verified tide predictions for Morro Bay (station 9412110).
    Returns a list of dicts with time (PST) and height (feet).
    """
    pst = pytz.timezone("America/Los_Angeles")
    today = datetime.now(pst).strftime("%Y%m%d")

    # NOAA API for verified tide predictions (height)
    url = (
        "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
        f"?product=predictions&application=devo_surf_fishing"
        f"&begin_date={today}&end_date={today}"
        f"&datum=MLLW&station={STATION_ID}"
        f"&time_zone=lst_ldt&units=english&interval=6&format=json"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return []

    preds = data.get("predictions", [])
    results = []

    for p in preds:
        t_str = p.get("t")
        h_str = p.get("v")

        if not t_str or not h_str:
            continue

        try:
            # Time is already in local standard/daylight time (lst_ldt)
            t = datetime.strptime(t_str, "%Y-%m-%d %H:%M")
            height = float(h_str)
        except Exception:
            continue

        results.append({"time": t, "height_ft": height})

    return results


def classify_tide_stage(height_now, height_prev, height_next):
    """
    Simple tide stage classifier based on height trend.
    """
    if height_prev is None or height_next is None:
        return "Unknown"

    rising = height_next > height_now
    falling = height_next < height_now

    if rising and height_now < height_next:
        return "Incoming"
    if falling and height_now > height_next:
        return "Outgoing"

    # Near turning points
    if abs(height_next - height_now) < 0.1:
        return "Slack"

    return "Unknown"


def get_tide_summary():
    """
    Returns:
      - list of points for charting (time, height_ft)
      - current tide height
      - current tide stage
    """
    pst = pytz.timezone("America/Los_Angeles")
    now = datetime.now(pst)

    points = fetch_tide_predictions()
    if not points:
        return {
            "points": [],
            "current_height": None,
            "current_stage": "Unknown",
        }

    # Find the closest prediction to 'now'
    closest = min(points, key=lambda p: abs(p["time"] - now))
    idx = points.index(closest)

    height_now = closest["height_ft"]
    height_prev = points[idx - 1]["height_ft"] if idx > 0 else None
    height_next = points[idx + 1]["height_ft"] if idx < len(points) - 1 else None

    stage = classify_tide_stage(height_now, height_prev, height_next)

    return {
        "points": points,
        "current_height": height_now,
        "current_stage": stage,
    }
