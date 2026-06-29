# Release notes format

## vX.Y.Z (YYYY-MM-DD)

### 🎉 Added
- New features

### 🔄 Changed
- Changes in existing functionality

### ⛔ Deprecated
- Soon-to-be removed features

### 🗑️ Removed
- Removed features

### 🐛 Fixed
- Bug fixes

### 🔒 Security
- Security-related fixes

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (X): Incompatible API changes (e.g., renaming a required skill field)
- **MINOR** (Y): Backward-compatible feature additions (e.g., new guide, new data entries)
- **PATCH** (Z): Backward-compatible bug fixes (e.g., fixing a broken link, correcting a contrast ratio)

## Release process

1. Update version in `SKILL.md` frontmatter
2. Update version badge in `README.md`
3. Add entry to `CHANGELOG.md`
4. Tag: `git tag -a vX.Y.Z -m "vX.Y.Z — short description"`
5. Push tag: `git push origin vX.Y.Z`
6. Create GitHub Release with notes from CHANGELOG
