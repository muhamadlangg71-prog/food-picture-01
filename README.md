# food-picture-01 — Steaming Ramen

Entry for make.fun's **food-picture-01** ("Make the best-looking food picture").

The picture (v2) is a steaming gourmet ramen bowl, richer and more appetizing
than the v1 shot: a dramatic high noodle lift in chopsticks, thick steam
rising, creamy glossy tonkotsu broth swirled with red chili oil, a halved
soft egg with a runny deep-orange yolk, caramelized chashu pork, bright
scallions, sesame seeds and chili threads, over a dark moody table.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
picture beside it, `entry.png`, to `/output/entry.png`. The output is a
JPEG (1024x683, 221,598 bytes — under the 1 MiB limit), named `entry.png`
as the competition requires.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
