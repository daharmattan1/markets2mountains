# Markets2Mountains Hugo Site - Troubleshooting Guide

## Recurring Issue: Site Rendering Breaks After Changes

### Symptoms
- Site doesn't render properly in browser
- Layout appears broken or missing
- Changes don't appear even though Hugo rebuilt

### Root Causes Identified

1. **Multiple Hugo Servers Running** (RARE - mostly false alarms from context transfer)
   - Previous sessions may leave Hugo servers in background
   - Conflicting ports cause rendering issues

2. **Custom Layout Overrides Breaking Rendering**
   - `layouts/_default/single.html` - KNOWN TO BREAK RENDERING
   - cardView settings in `params.toml` - KNOWN TO BREAK RENDERING
   - Custom layouts can conflict with Congo theme

3. **Browser Cache Issues**
   - Old CSS/JS cached by browser
   - Hard refresh needed after changes

### Quick Fix Checklist

When rendering breaks, try these in order:

1. **Hard Refresh Browser** (Ctrl+F5 or Cmd+Shift+R)
   - Clears browser cache
   - Often fixes "ghost" rendering issues

2. **Check Git Status**
   ```bash
   cd 05_shop/markets2mountains
   git status
   git diff
   ```
   - Look for uncommitted changes to config files
   - Especially `config/_default/params.toml`

3. **Revert to Last Known Good State**
   ```bash
   cd 05_shop/markets2mountains
   git reset --hard HEAD
   # OR revert specific config file:
   git checkout config/_default/params.toml
   ```

4. **Kill All Hugo Processes** (Usually not needed, but check if suspicious)
   ```bash
   # Find Hugo processes
   tasklist | grep -i hugo

   # Kill specific process
   taskkill /PID <process_id> /F
   ```

5. **Restart Hugo Server**
   - Stop all Claude Code background bash shells
   - Start fresh: `hugo server --buildDrafts --disableFastRender`

### Known Dangerous Changes

**DO NOT COMMIT** these without testing extensively:

1. **Custom Single Post Layout**
   - File: `layouts/_default/single.html`
   - Status: DISABLED (renamed to single.html.bak)
   - Reason: Breaks rendering, conflicts with Congo theme

2. **CardView Settings in params.toml**
   - Lines like: `cardView = true` or `cardViewScreenWidth = false`
   - Reason: Breaks homepage/list rendering

3. **Table of Contents Settings**
   - Be careful changing `showTableOfContents` in different sections
   - Test homepage, lists, and individual posts after changes

### Safe Configuration Areas

These files are generally safe to edit:

1. **languages.en.toml** (Author bio, site title)
   - Text content changes are safe
   - No layout-breaking risks

2. **hugo.toml** (Permalinks, baseURL)
   - Tested configurations work well

3. **assets/css/custom.css** (Custom fonts, styling)
   - Additive only, doesn't override theme

4. **layouts/partials/extend-head.html** (Google Fonts, meta tags)
   - Extension point designed for customization

### Pre-Commit Checklist

Before committing any config change:

- [ ] Test in browser - homepage renders?
- [ ] Test in browser - individual post renders?
- [ ] Test in browser - posts list page renders?
- [ ] Hard refresh (Ctrl+F5) to clear cache
- [ ] Check console for JavaScript errors
- [ ] Verify no Hugo build warnings

### Emergency Rollback

If site is completely broken after a commit:

```bash
cd 05_shop/markets2mountains

# See recent commits
git log --oneline -5

# Revert to specific good commit
git reset --hard <commit-hash>

# OR undo last commit but keep changes
git reset --soft HEAD~1

# OR undo last commit and discard changes
git reset --hard HEAD~1
```

### Current Known-Good State

**Last verified working commit:** `0881c7d Switch to clean slug-only URLs`

**Working configuration:**
- Permalinks: `/:slug/` (clean URLs)
- Layout: Congo profile layout
- Custom fonts: DM Sans (headers), Instrument Sans (body)
- Table of contents: DISABLED on individual posts
- Custom single.html: DISABLED (renamed to .bak)
- Summary truncation: Handled by frontmatter (summaryLength setting not working)

### Pattern Recognition

If rendering breaks after changing:
1. **layouts/** directory → Likely layout override issue
2. **params.toml** → Likely cardView or layout setting issue
3. **hugo.toml** → Permalink or output format issue
4. **languages.en.toml** → Unlikely to break rendering (text content only)
5. **custom.css** → Check CSS syntax, but usually safe

### Debugging Steps

When investigating a rendering issue:

1. **Check Hugo build output**
   ```bash
   # Look for errors or warnings
   hugo server --buildDrafts --disableFastRender
   ```

2. **Inspect browser console**
   - Open DevTools (F12)
   - Look for JavaScript errors
   - Check Network tab for 404s

3. **Compare with working commit**
   ```bash
   # See what changed
   git diff 0881c7d..HEAD
   ```

4. **Test incrementally**
   - Revert everything
   - Apply changes one file at a time
   - Test after each change

---

**Last Updated:** 2025-11-16
**Maintainer:** Claude Code + Victor
