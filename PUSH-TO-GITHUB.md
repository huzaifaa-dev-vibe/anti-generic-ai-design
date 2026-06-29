# Push to GitHub

The repo at `/home/z/my-project/ai-design-skill/` is git-initialized with 2 commits on the `main` branch. To push it to GitHub:

## Option A — Create the repo on GitHub first (recommended)

1. Go to https://github.com/new
2. **Repository name**: `anti-generic-ai-design` (or your choice)
3. **Description**: `A design skill for AI coding agents that forces research, debate, and justification before code. Kills the "AI look".`
4. **Public** (recommended — this should be a community resource)
5. **Do NOT initialize** with README, .gitignore, or LICENSE (the repo already has them)
6. Click **Create repository**
7. Copy the URL GitHub gives you (looks like `https://github.com/yourusername/anti-generic-ai-design.git`)

Then run from the project directory:

```bash
cd /home/z/my-project/ai-design-skill
git remote add origin https://github.com/YOUR_USERNAME/anti-generic-ai-design.git
git branch -M main
git push -u origin main
```

## Option B — Use GitHub CLI (if installed + authenticated)

```bash
cd /home/z/my-project/ai-design-skill
gh repo create anti-generic-ai-design --public --source=. --remote=origin --push
```

## Option C — SSH (if you use SSH keys with GitHub)

```bash
cd /home/z/my-project/ai-design-skill
git remote add origin git@github.com:YOUR_USERNAME/anti-generic-ai-design.git
git branch -M main
git push -u origin main
```

## After the first push

1. **Add topics** on GitHub (repo page → gear icon next to About): `ai`, `design-system`, `claude-code`, `cursor`, `llm`, `vibe-coding`, `frontend`, `design-tokens`
2. **Enable Issues** (Settings → Features → Issues)
3. **Enable Discussions** (Settings → Features → Discussions) — for Q&A and contribution ideas
4. **Add a social preview image** (Settings → Social preview) — a screenshot of the demo HTML
5. **Pin the repo** to your GitHub profile

## Optional — GitHub Pages demo

The `examples/demo-saas-landing.html` file is a standalone demo. To publish it on GitHub Pages:

1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main`, folder: `/examples`
4. Save — your demo will be live at `https://YOUR_USERNAME.github.io/anti-generic-ai-design/demo-saas-landing.html`

## Verifying the push

After pushing, verify the repo has:

- [ ] `SKILL.md` visible in the root (the main orchestrator)
- [ ] `README.md` rendered on the repo home page
- [ ] 21 guide files in `guides/`
- [ ] 5 JSON data files in `data/` (each with 100 entries)
- [ ] React+TS templates in `templates/`
- [ ] HTML demo in `examples/`
- [ ] LICENSE file shows MIT
- [ ] `.gitignore` present

## Tagging a release

Once pushed, tag v1.0.0:

```bash
cd /home/z/my-project/ai-design-skill
git tag -a v1.0.0 -m "v1.0.0 — Initial public release"
git push origin v1.0.0
```

Then on GitHub: Releases → Draft a new release → choose the `v1.0.0` tag → publish.

## Promoting it

- Share on Twitter/X: "Built a design skill that forces AI agents to research, debate, and justify every design decision before writing code. 21 guides + 500 curated references (sites/themes/palettes/fonts/animations) + drop-in React templates. Open source. Kills the 'AI look'."
- Post to: Hacker News (Show HN), r/webdev, r/nextjs, r/claudeai, r/cursor
- Add to: awesome-claude-code, awesome-cursor lists
