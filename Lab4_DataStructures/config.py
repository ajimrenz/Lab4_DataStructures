
LAST_NAME = "AGAWA"
FAVORITE_ARTIST = "Juan Karlos"
SEED_NUM = 2   

LETTERS = [c for c in FAVORITE_ARTIST.upper() if c.isalpha()]
POSITIONS = [ord(c) - 64 for c in LETTERS]   # A=1 ... Z=26


def show_inputs():
    print("=== STUDENT INPUTS ===")
    print(f"LAST_NAME={LAST_NAME}  FAVORITE_ARTIST={FAVORITE_ARTIST}  SEED_NUM={SEED_NUM}")
    print(f"Character positions: {POSITIONS}\n")