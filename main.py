import os

TEXT = (
    "High above the clouds, snow is falling on a mountain no one climbed "
    "this year. It falls the way it fell a thousand years ago, quiet and "
    "unhurried, in no need of being seen. You can hear it, if you stop. "
    "The world is very large, and very patient, and it is holding you too."
)


def main():
    # The gate allows 1 to 280 Unicode code points, not only white space.
    if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
        raise ValueError(f"entry text is {len(TEXT)} characters, outside 1-280")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
