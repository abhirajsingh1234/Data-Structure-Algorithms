import re
import shutil
from pathlib import Path

# Folder that contains your downloaded/unzipped font folders (searched recursively)
SOURCE_DIR = Path(r"C:\Users\pooja\Downloads\Abril_Fatface,Amatic_SC,Anton,Bebas_Neue,Caveat,etc")

# Android project font folder (created if missing)
DEST_DIR = Path(r"C:\Users\pooja\AndroidStudioProjects\LockScreenTracker\app\src\main\res\font")

# Set True to only print what would happen, without moving anything
DRY_RUN = False

# normalized family name -> file name the Kotlin code expects
TARGETS = {
    "pacifico":        "pacifico.ttf",
    "lobster":         "lobster.ttf",
    "dancingscript":   "dancing_script.ttf",
    "caveat":          "caveat.ttf",
    "satisfy":         "satisfy.ttf",
    "greatvibes":      "great_vibes.ttf",
    "playfairdisplay": "playfair_display.ttf",
    "merriweather":    "merriweather.ttf",
    "lora":            "lora.ttf",
    "montserrat":      "montserrat.ttf",
    "poppins":         "poppins.ttf",
    "raleway":         "raleway.ttf",
    "oswald":          "oswald.ttf",
    "bebasneue":       "bebas_neue.ttf",
    "anton":           "anton.ttf",
    "abrilfatface":    "abril_fatface.ttf",
    "permanentmarker": "permanent_marker.ttf",
    "indieflower":     "indie_flower.ttf",
    "amaticsc":        "amatic_sc.ttf",
    "cinzel":          "cinzel.ttf",
    "orbitron":        "orbitron.ttf",
    "pressstart2p":    "press_start_2p.ttf",
    # "roboto":        "roboto.ttf",   # uncomment if you add Roboto
}


def classify(path: Path):
    """Return (family_key, is_static_regular) for Regular/variable files, else None."""
    stem = path.stem
    has_axes = "[" in stem                      # variable font, e.g. Montserrat[wght]
    stem = re.sub(r"\[.*?\]", "", stem)         # drop [wght] etc.
    parts = stem.split("-")
    family = re.sub(r"[^a-z0-9]", "", parts[0].lower())
    style = parts[1].lower() if len(parts) > 1 else ""
    if style not in ("", "regular"):
        return None                             # Bold, Italic, etc. -> skip
    return family, (not has_axes and style == "regular")


def main():
    # best candidate per family: static Regular wins over variable
    best = {}
    for ttf in SOURCE_DIR.rglob("*.ttf"):
        if DEST_DIR in ttf.parents:
            continue
        info = classify(ttf)
        if not info:
            continue
        family, is_static = info
        if family not in TARGETS:
            continue
        if family not in best or (is_static and not best[family][1]):
            best[family] = (ttf, is_static)

    if not DRY_RUN:
        DEST_DIR.mkdir(parents=True, exist_ok=True)

    for family, target_name in TARGETS.items():
        if family not in best:
            print(f"MISSING   {target_name}")
            continue
        src = best[family][0]
        dest = DEST_DIR / target_name
        if dest.exists():
            print(f"EXISTS    {target_name} (skipped)")
            continue
        print(f"{'WOULD MOVE' if DRY_RUN else 'MOVED'}  {src.name}  ->  {target_name}")
        if not DRY_RUN:
            shutil.move(str(src), str(dest))


if __name__ == "__main__":
    main()