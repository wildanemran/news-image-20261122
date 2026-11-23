# The World in One Day — Sunday, 22 November 2026

A newspaper front page summing up the world's news of Sunday 22 November 2026
in a single image (`entry.png`, 1024×1024).

## The day

- **Climate — COP31 collapses in Antalya.** After two weeks of talks, the
  summit ends with no agreement: the EU rejects a final draft with no mention
  of fossil fuels.
- **Bahrain — Iran strike.** Bahrain says an Iranian strike on an industrial
  site in Sitra injured two people, one critically. Gulf states condemned
  the attack.
- **Ukraine — Kyiv region.** A Russian drone strike partly collapses a
  five-storey residential block on Sunday morning; at least 14 people are
  missing.
- **West Bank — settler attacks.** Israeli settlers attack Palestinian
  villages overnight, burning cars and homes; opposition leader Gadi Eisenkot
  calls the attacks "Jewish terrorism".
- **Also on 22 November:** a factory fire in Cikande, Indonesia (3 dead,
  dozens missing); a boat capsizes in Nigeria (24 dead); Europe's BepiColombo
  probe enters orbit around Mercury; South Korea's education minister resigns
  over an AI cheating scandal; Leeds beat Chelsea 4–1 at Stamford Bridge.

All events as reported on 22 November 2026 by AP, Reuters, CNN, AFP and
Al Jazeera. The photos are AI-generated illustrations, not photographs of the
events.

## How it is built

`compose.py` (Python 3, Pillow) lays out the front page: masthead, date,
lead story, three secondary stories with photos, and an "also on 22 November"
strip. All text is rendered by Pillow, so nothing is garbled. The four photos
in `assets/` were generated for this entry. `main.ts` (Node 22, standard
library only) copies `entry.png` to the output directory.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 compose.py                                      # rebuild entry.png
```

## License

MIT — see `LICENSE`.
