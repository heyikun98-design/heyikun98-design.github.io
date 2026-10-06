#!/usr/bin/env python3
"""Regenerate assets/og-image.png — the 1200x630 link-preview card.

Optional: only needed if you want to change the wording on the social share card.
Run it with any Python 3 that has Pillow installed:

    python3 tools/make-og-image.py

It uses the Arial fonts shipped with macOS; edit FONT_BOLD / FONT_REG for other systems.
The colours match assets/style.css so the card looks like the site.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, os.pardir, "assets", "og-image.png"))

W, H = 1200, 630
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

BLUE = (0, 123, 255)
BLUE_DARK = (0, 86, 179)
INK = (51, 51, 51)
SOFT = (85, 85, 85)
MUTED = (120, 130, 145)
BAND = (240, 240, 240)
LINE = (222, 226, 232)

NAME = "Yikun He"
ROLE = "Mechanical Engineering  ·  Robotics  ·  Deep Learning"
LINES = [
    "Robotics R&D intern — humanoid leg & torso mechanical design,",
    "reinforcement learning for robot policies, URDF simulation.",
    "Point-cloud deep learning for collision injury prediction.",
]
CHIPS = ["heyikun98@gmail.com", "github.com/heyikun98-design"]

img = Image.new("RGB", (W, H), BAND)
d = ImageDraw.Draw(img)

# top accent bar, same blue as the site buttons
d.rectangle([0, 0, W, 8], fill=BLUE)

# white content card on the grey band
d.rounded_rectangle([56, 62, W - 56, H - 62], radius=10, fill=(255, 255, 255))

f_name = ImageFont.truetype(FONT_BOLD, 84)
f_role = ImageFont.truetype(FONT_REG, 30)
f_body = ImageFont.truetype(FONT_REG, 25)
f_chip = ImageFont.truetype(FONT_REG, 23)

x = 112
d.text((x, 120), NAME, font=f_name, fill=INK)
d.text((x + 3, 218), ROLE, font=f_role, fill=SOFT)

# blue rule under the name
d.rectangle([x, 274, x + 130, 279], fill=BLUE)

y = 314
for ln in LINES:
    d.text((x, y), ln, font=f_body, fill=SOFT)
    y += 38

# contact chips
cx = x
for c in CHIPS:
    w = d.textlength(c, font=f_chip)
    d.rounded_rectangle([cx, 470, cx + w + 40, 518], radius=24, fill=(255, 255, 255),
                        outline=LINE, width=1)
    d.text((cx + 20, 494), c, font=f_chip, fill=INK, anchor="lm")
    cx += w + 56

# small footer note inside the card
d.text((x, 540), "Available for robotics / AI internship opportunities",
       font=ImageFont.truetype(FONT_REG, 21), fill=MUTED)

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, img.size)
