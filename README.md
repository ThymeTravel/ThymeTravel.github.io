# thymetravel.github.io

Personal site for Basil Aranda. Plain HTML/CSS, no build step.

## Deploy

1. Create a **public** repo named exactly `ThymeTravel.github.io` (the repo name is what makes it the root site at `https://thymetravel.github.io/`).
2. From this folder:
   ```bash
   git init -b main
   git add .
   git commit -m "Rebuild site"
   git remote add origin git@github.com:ThymeTravel/ThymeTravel.github.io.git
   git push -u origin main
   ```
3. Repo → **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)`.
4. Wait ~1 minute, then open the URL. Hard-refresh (Cmd+Shift+R) if you see stale content.

## Layout

```
index.html          the page
404.html            custom not-found page
css/style.css       all styles
images/             hero.jpg, about.jpg, band.jpg, og.jpg
images/projects/    maverick.jpg, panel-method.jpg, mars-rover.jpg
images/photography/ 01.jpg … 12.jpg
resume/             Basil-Aranda-Resume.pdf   <- you add this
tools/prep_images.py  resize + strip GPS/EXIF
robots.txt, sitemap.xml, .nojekyll
```

## Replace the placeholders

Every image in `images/` is a labeled placeholder. Overwrite each with the real file, **same name, lowercase, `.jpg`**. GitHub Pages is case-sensitive: `IMG_1968.JPG` ≠ `img_1968.jpg`.

| Old file (deleted site) | New file | Target size |
|---|---|---|
| `fury.jpg` | `images/hero.jpg` | 1920×1080 |
| `basilshuttle.png` | `images/about.jpg` | ~900×1100 |
| `u2Plane1.png` | `images/band.jpg` | 1920×800 |
| `MissionRender1.JPG` | `images/projects/maverick.jpg` and `images/og.jpg` (crop 1200×630) | 1200×800 / 1200×630 |
| `n250minus1.png` | `images/projects/panel-method.jpg` | 1200×800 |
| `agnesi.png` | `images/projects/mars-rover.jpg` | 1200×800 |
| `IMG_1968 … IMG_2331` (12 photos) | `images/photography/01.jpg … 12.jpg` | ≤1600px long edge |

Photos: run them through the prep script. It resizes to ≤1600px, fixes rotation, compresses to ~200–400 KB each, and **removes GPS location data** that phone photos embed.

```bash
pip install pillow
python3 tools/prep_images.py ~/Pictures/portfolio images/photography
```

Keep every image under ~500 KB. The old site served 12 full-resolution phone photos, which is why it was slow.

## Resume

Put the PDF at `resume/Basil-Aranda-Resume.pdf`. Until then the Resume card 404s. (The old link used a backslash path, which never works on GitHub Pages.)

## Email

Uncomment the email card in the Contact section and add an address. Use one you're fine with scrapers seeing.

## Before you push

- Re-check the GPA and dates against your transcript/resume.
- Check that the three game links still load: `/gamemaybe/`, `/snake/`, `/breakout/`. Those are separate repos; if you deleted them along with the old site, restore them or remove the links in `index.html`.
- Open the site on your phone.
- Paste the URL into LinkedIn's Post Inspector or a Slack message to confirm the preview image (`images/og.jpg`) shows.
