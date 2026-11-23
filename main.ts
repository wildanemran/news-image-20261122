// news-image-20261122 — "The World in One Day".
// The entry is a front page (entry.png) summing up the world's news of
// Sunday 22 November 2026: COP31 collapses, the Bahrain strike, the Kyiv
// drone strike, the West Bank attacks, and the rest of the day.
// This program only puts that image where the grader reads it, as
// /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when set).
// It copies bytes and nothing else, so two runs write identical output.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outDir, { recursive: true });
const image = readFileSync(join(here, "entry.png"));
writeFileSync(join(outDir, "entry.png"), image);
