# Yikun He — personal résumé website

A fast, dependency-free static site built from `resume.docx`, styled after the layout of
[francescocrivelli.com](https://www.francescocrivelli.com): Arial, `#333` text on white,
`#007BFF` blue buttons, a centered 800px column made of light-grey blocks, a fixed header
with right-aligned nav links, and a 3-up project grid on its own page.

No build step, no framework, no external requests (no Google Fonts, no CDN, no trackers).

```
resume-site/
├── index.html                      # home: hero, about, experience, education, skills, contact
├── projects.html                   # projects grid + publication
├── assets/
│   ├── style.css                   # the whole design system + responsive + print styles
│   ├── main.js                     # mobile hamburger menu + footer year (vanilla, ~40 lines)
│   ├── favicon.svg                 # blue "YH" monogram
│   ├── og-image.png                # 1200×630 link-preview card
│   └── Yikun-He-Resume.pdf         # the CV, offered as a download from both pages
├── tools/
│   └── make-og-image.py            # optional: regenerates the share card
└── README.md
```

## Page structure

| Page | Anchor | Content |
| --- | --- | --- |
| `index.html` | — | Hero: name, tagline, "View My Work" / "View CV" buttons, short bio |
| | `#about` | About Me + key-facts line |
| | `#experience` | Mimicverse (current) and SIAT internships |
| | `#education` | Central South University / Dundee, UC Berkeley summer sessions |
| | `#skills` | Algorithms, programming, robotics tools, mathematics |
| | `#contact` | Email, GitHub, WeChat + Download CV |
| `projects.html` | — | "My Projects": PT-HICnet, external structural airbag, structural dynamics |
| | `#publication` | IEEE Transactions on Evolutionary Computation paper |

## Design notes

- **Layout** — sections are an 800px centered column (`section { max-width: 800px }`), so the
  grey hero and contact blocks are 800px wide with white margins, exactly like the reference.
  The projects page widens to 1200px for the 3-column grid.
- **Colours** — `--blue: #007BFF` (hover `#0056b3`), `--ink: #333`, cards `#f9f9f9`,
  hero band `#f0f0f0`, footer `#f1f1f1`. All in `:root` at the top of `assets/style.css`.
- **Breakpoints** — `1024px` drops the project grid to 2 columns; `768px` switches the header
  to the hamburger overlay, stacks the hero buttons, and makes the contact links a 2-column grid.
- **No dark mode** — the reference design is light-only, so the theme toggle was removed.
- **Accessibility** — skip link, `aria-expanded` on the menu button, `Escape` closes the menu,
  `aria-current` on the active nav item, visible focus outlines, and full keyboard support.
- **Print** — `Cmd/Ctrl + P` gives a clean paper version (3 pages home, 2 pages projects);
  the header, buttons, social row and thumbnails are hidden.

### One gotcha worth knowing

The header uses `backdrop-filter`, which makes it the **containing block for fixed-position
descendants**. The mobile menu overlay lives inside the header, so `inset: 0` alone sized it
to the 60px header instead of the screen. `height: 100vh` fixes it — if you move the menu
markup outside `<header>`, that line becomes unnecessary.

## Live site

**https://heyikun98-design.github.io/** — published with GitHub Pages from the public repo
[heyikun98-design/heyikun98-design.github.io](https://github.com/heyikun98-design/heyikun98-design.github.io)
(branch `main`, root folder, HTTPS enforced). Put this URL on the CV.

Because the repo is named `<username>.github.io`, GitHub serves it as the account's user site —
no path prefix, so the URL is as short as it gets.

### Updating the live site

The repo is already initialised here and wired to `origin`, so publishing a change is:

```sh
cd resume-site
git add -A
git commit -m "Update content"
git push
```

Pages rebuilds automatically in ~30–60 s. The GitHub CLI is registered as the git credential
helper (`gh auth setup-git`), so no password prompt appears.

### Notes specific to this deployment

- **Absolute URLs in `<head>`.** `og:image`, `og:url` and `rel=canonical` must stay absolute
  (`https://heyikun98-design.github.io/...`). Social crawlers do not resolve relative paths, so
  a relative `og:image` silently produces link previews with no image.
- **Moving to a custom domain** means updating those three tags in both HTML files, plus adding
  a `CNAME` file containing just the domain.
- **WeChat caches link previews per URL.** After changing the share card, re-share with a query
  string (`?v=2`) or a different URL to bust the cache.

## Preview locally

Open `index.html` directly in a browser, or serve the folder:

```sh
cd resume-site
python3 -m http.server 8000
# → http://localhost:8000
```

## Alternative hosts

**Vercel / Netlify** — drag the `resume-site` folder onto the dashboard and you get a URL such as
`yikun-he.vercel.app`. Note that `vercel.app` is frequently unreachable from mainland China, so
GitHub Pages is the safer default for applications to Chinese employers.

**Cloudflare Pages** — better China routing than both; requires a Cloudflare account and either
a Git connection or `wrangler pages deploy .`.

**Custom domain** — buy one (e.g. `yikunhe.com`), add a `CNAME` file containing just the domain
name, and point an `A`/`CNAME` record at the host.

## Editing content

All copy lives in the two HTML files — one block per CV section. Colours, spacing and
typography are CSS custom properties in `:root` at the top of `assets/style.css`; changing
`--blue` and `--band` re-skins the entire site.

When the CV changes, replace `assets/Yikun-He-Resume.pdf` with the new export, keeping the
same filename so the download links keep working.

## Outbound links

Every organisation, journal and tool named on the site links to its official page, so a
recruiter can click straight through:

| Where | Links to |
| --- | --- |
| About Me | [Central South University](https://en.csu.edu.cn/) · [University of Dundee](https://www.dundee.ac.uk/) |
| Experience | [SIAT](https://www.siat.ac.cn/) · [Vicon](https://www.vicon.com/) · [Delsys](https://delsys.com/) |
| Education | [CSU](https://en.csu.edu.cn/) · [Dundee International Institute](https://dii.csu.edu.cn/) · [UC Berkeley](https://www.berkeley.edu/) · [Summer Sessions](https://summer.berkeley.edu/) |
| Projects | [PyTorch](https://pytorch.org/) · [ANSYS](https://www.ansys.com/) · [SJTU](https://en.sjtu.edu.cn/) · [UCLA](https://www.ucla.edu/) |
| Publication | [IEEE Transactions on Evolutionary Computation](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=4235) |
| Skills | [PyTorch](https://pytorch.org/) · [ANSYS](https://www.ansys.com/) · [MuJoCo](https://mujoco.org/) · [mjlab](https://github.com/mujocolab/mjlab) · [ROS 2](https://ros.org/) |
| Contact | Email · GitHub · WeChat |

All of them were checked and return HTTP 200. Two notes:

- **Mimicverse has no link** — no official site could be verified, so the heading is left
  plain rather than pointing somewhere wrong. Send the company URL and it takes one line:
  `<h3><a href="…">Mimicverse</a> | Robotics R&amp;D Intern</h3>`.
- Links inside body copy carry a faint underline (not colour alone), so they are still
  discoverable for colour-blind readers and in grayscale print.

## Suggested next steps

- **Add "View Project" links.** The `.project-link` style is already in the stylesheet — as
  soon as a project has a GitHub repository or a write-up, add
  `<a class="project-link" href="...">View Project</a>` inside its `.project-item`.
- **Swap the abstract thumbnails for real images.** Each card currently uses an inline SVG
  diagram. Replace `<div class="project-thumb">…</div>` with
  `<img class="project-thumb" src="assets/pt-hicnet.jpg" alt="…">` for a photo of the robot,
  a simulation screenshot or a result plot — real visuals read much better for robotics roles.
- **Add a photo to the hero** (the reference has a 200px circular one). Add
  `<img class="profile-image" src="assets/me.jpg" alt="Yikun He">` inside `.hero-content`.
- **Re-generate the share card** after changing your tagline:
  `python3 tools/make-og-image.py`.
