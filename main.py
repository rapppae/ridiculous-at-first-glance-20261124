"""Write the ridiculous startup pitch entry to /output/entry.txt.

One sentence, 177 characters (limit 200) -- no trailing newline.
The pitch names the odd thing sold, who pays, and why it holds together.
"""

from pathlib import Path

ENTRY = "We rent out idle Roombas as night-shift security guards for small warehouses: they already patrol the floor, they never sleep, and the subscription costs less than one break-in."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
