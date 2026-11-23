#!/usr/bin/env python3
"""Compose the news-image-20261122 entry: a newspaper front page, 1024x1024.
All text is rendered by PIL (crisp, no garbled AI text); the four photos are
AI-generated illustrations of the day's verified stories.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1024, 1024
M = 24                      # margin
GUT = 16                    # gutter between columns
ASSETS = "/home/hatch/workspace/makefun/news-image-20261122/assets/"
OUT = "/home/hatch/workspace/makefun/news-image-20261122/repo/entry.png"

PAPER = (248, 245, 238)
INK = (20, 20, 20)
NAVY = (22, 35, 63)
RED = (163, 29, 29)
GREY = (90, 90, 90)
RULE = (180, 175, 165)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def photo(path, w, h):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
y = 0

# ---- Masthead ----
d.rectangle([0, 0, W, 68], fill=NAVY)
f_mast = font(SERIF_B, 42)
t = "THE WORLD IN ONE DAY"
d.text(((W - d.textlength(t, font=f_mast)) / 2, 10), t, font=f_mast, fill=(255, 255, 255))
d.rectangle([0, 68, W, 72], fill=RED)

# ---- Date line (must be unmissable: criterion 1) ----
y = 82
f_date = font(SERIF_B, 40)
t = "SUNDAY, 22 NOVEMBER 2026"
d.text(((W - d.textlength(t, font=f_date)) / 2, y), t, font=f_date, fill=RED)
y += 50
f_sub = font(SANS, 17)
t = "THE DAY'S WORLD NEWS  —  AS REPORTED ON 22 NOVEMBER 2026"
d.text(((W - d.textlength(t, font=f_sub)) / 2, y), t, font=f_sub, fill=GREY)
y += 30
d.line([M, y, W - M, y], fill=RULE, width=2)
y += 12

# ---- Lead photo (COP31) ----
lead_w, lead_h = W - 2 * M, 160
img.paste(photo(ASSETS + "media-generation-cop31-hall-0-203f2175-006d-437b-a033-3b4a12efa1d4.webp",
                lead_w, lead_h), (M, y))
y += lead_h + 10

# ---- Lead story ----
f_kick = font(SANS_B, 18)
d.text((M, y), "ANTALYA, TURKEY  ·  CLIMATE", font=f_kick, fill=RED)
y += 26
f_head = font(SERIF_B, 54)
d.text((M, y), "CLIMATE TALKS COLLAPSE", font=f_head, fill=INK)
y += 62
f_deck = font(SANS, 21)
deck = ("COP31 ends with no agreement after the EU rejects a final draft with no "
        "mention of fossil fuels.")
y = draw_lines(d, wrap(d, deck, f_deck, W - 2 * M), f_deck, M, y, INK, 26)
y += 10
d.line([M, y, W - M, y], fill=RULE, width=2)
y += 12

# ---- Three secondary stories ----
col_w = (W - 2 * M - 2 * GUT) // 3
col_h_img = 120
cols = [
    ("media-generation-bahrain-port-0-dcdd87a3-4b73-4156-8bf1-28b3916bbcb5.webp",
     "BAHRAIN  ·  MIDDLE EAST",
     "Iran strike hits Bahrain site; two hurt",
     "Bahrain says an Iranian strike on an industrial site in Sitra injured "
     "two, one critically. Gulf states condemned the attack."),
    ("media-generation-kyiv-rubble-0-c248c4da-31e1-4c53-8fa7-f029dd558c3a.webp",
     "KYIV REGION  ·  UKRAINE",
     "Drone hits Kyiv block; 14 missing",
     "A Russian drone strike partly collapsed a five-storey block on Sunday "
     "morning. At least 14 are missing as rescuers search the rubble."),
    ("media-generation-westbank-fire-0-ab1cfd20-1782-4ecf-a567-95ca69cf1516.webp",
     "WEST BANK  ·  MIDDLE EAST",
     "Settlers torch cars across the West Bank",
     "Settlers attacked Palestinian villages overnight, burning cars and "
     "homes. Opposition leader Eisenkot called it \u201cJewish terrorism\u201d."),
]
top = y
col_bottom = top
f_ckick = font(SANS_B, 16)
f_chead = font(SERIF_B, 25)
f_cbody = font(SANS, 17)
for i, (fn, kick, head, body) in enumerate(cols):
    x = M + i * (col_w + GUT)
    img.paste(photo(ASSETS + fn, col_w, col_h_img), (x, top))
    yy = top + col_h_img + 8
    d.text((x, yy), kick, font=f_ckick, fill=RED)
    yy += 22
    yy = draw_lines(d, wrap(d, head, f_chead, col_w), f_chead, x, yy, INK, 29)
    yy += 4
    yy = draw_lines(d, wrap(d, body, f_cbody, col_w), f_cbody, x, yy, INK, 21)
    col_bottom = max(col_bottom, yy)
y = col_bottom + 8
d.line([M, y, W - M, y], fill=RULE, width=2)
y += 10

# ---- Also on 22 November ----
f_also_h = font(SANS_B, 18)
d.text((M, y), "ALSO ON 22 NOVEMBER", font=f_also_h, fill=RED)
y += 26
f_also = font(SANS, 19)
items = [
    ("INDONESIA", "Fire at a candy factory in Cikande, Banten, kills 3; dozens missing."),
    ("NIGERIA", "Boat carrying funeral mourners capsizes; 24 dead."),
    ("SPACE", "Europe\u2019s BepiColombo probe enters orbit around Mercury after an eight-year journey."),
    ("SOUTH KOREA", "Education minister resigns over an AI cheating scandal."),
    ("SPORT", "Leeds stun Chelsea 4\u20131 at Stamford Bridge, a first win there since 1999."),
]
for tag, txt in items:
    d.rectangle([M, y + 6, M + 8, y + 14], fill=RED)
    line = f"{tag}  —  {txt}"
    d.text((M + 16, y), line, font=f_also, fill=INK)
    y += 23
y += 6
d.line([M, y, W - M, y], fill=RULE, width=2)
y += 8

# ---- Footer ----
f_foot = font(SANS, 14)
t = ("All events of Sunday 22 November 2026, as reported by AP, Reuters, CNN, AFP and "
     "Al Jazeera. Photos are illustrations.")
d.text((M, y), t, font=f_foot, fill=GREY)
y += 20

print("final y =", y, "canvas H =", H)
assert y <= H, "layout overflow!"

img.save(OUT, "PNG", optimize=True)
import os
print("saved", OUT, os.path.getsize(OUT), "bytes")
