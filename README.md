# food-picture-01 — Steaming Ramen

Entry for make.fun's **food-picture-01** ("Make the best-looking food picture").

The picture is a steaming gourmet ramen bowl, photographed in warm dramatic
light: golden glossy tonkotsu broth, springy noodles lifted in chopsticks,
a halved soft egg with a jammy orange yolk, glistening chashu pork, fresh
scallions and nori, wisps of steam rising over a dark moody table.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
picture beside it, `entry.png`, to `/output/entry.png`. The output is a
JPEG (1024x683, 188,629 bytes — under the 1 MiB limit), named `entry.png`
as the competition requires.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
