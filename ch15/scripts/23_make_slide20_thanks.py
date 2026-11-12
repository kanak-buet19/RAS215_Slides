"""Slide 20: thank you and questions (last page, numbered).

Writes ../slides/separate/20_slide20_thanks.html. Same washed campus photo as the title page
(02_make_slide0_title.py); guideline A12 closing page: "Thank you!" (88 px navy bold),
"Questions?" (48 px red bold italic), then name, school, university and email.

Run:  python3 23_make_slide20_thanks.py
"""
import importlib

lib = importlib.import_module("01_slide_lib")
title_page = importlib.import_module("02_make_slide0_title")    # WASH

NAVY, RED = lib.NAVY, lib.RED


def build():
    photo = lib.data_uri(lib.ASSETS / "polytechnic_photo.jpeg", "image/jpeg")
    css = f"""
  .bg {{ position: absolute; left: 0; top: 0; width: 1280px; height: 720px; object-fit: cover; }}
  .wash {{ position: absolute; left: 0; top: 0; width: 1280px; height: 720px;
           background: rgba(255, 255, 255, {title_page.WASH}); }}
  .title {{ display: none; }}
  .thanks {{ position: absolute; left: 48px; top: 200px; margin: 0; font-size: 88px; font-weight: bold; color: {NAVY}; }}
  .q {{ position: absolute; left: 52px; top: 320px; margin: 0; font-size: 48px; font-weight: bold; font-style: italic; color: {RED}; }}
  .who {{ position: absolute; left: 52px; top: 450px; font-size: 22px; line-height: 1.45; color: #000; }}
  .who b {{ font-size: 30px; }}
  .who a {{ color: #0563c1; text-decoration: underline; }}
"""
    body = f"""  <img class="bg" src="{photo}" alt="">
  <div class="wash"></div>
  <p class="thanks">Thank you!</p>
  <p class="q">Questions?</p>
  <div class="who"><b>Rakibul Islam Kanak</b><br>
    Teaching Assistant, RAS 215<br>
    School of Manufacturing Systems and Networks, Arizona State University<br>
    Email: <a href="mailto:rkanak@asu.edu">rkanak@asu.edu</a></div>"""
    lib.write_page("20_slide20_thanks.html", "Slide 20 - Thank you", "", body, 20, css)


if __name__ == "__main__":
    build()
