# Claude Code Workflow for Markets2Mountains

## For Claude Code: Pre-Commit Mandatory Checklist

**STOP** before committing any changes to config files. Follow this checklist:

### 1. Identify Risk Level

**HIGH RISK** (Requires extensive testing):
- `layouts/_default/single.html` (KNOWN DANGEROUS - currently disabled)
- Changes to `params.toml` layout settings (cardView, etc.)
- Changes to `params.toml` list/homepage sections
- New layout files in `layouts/` directory

**MEDIUM RISK** (Test before committing):
- `hugo.toml` (permalinks, outputs, baseURL)
- `params.toml` article settings (showTOC, etc.)
- `assets/css/custom.css` (CSS syntax errors can break site)

**LOW RISK** (Safe with basic verification):
- `languages.en.toml` author bio/headline (text content only)
- `layouts/partials/extend-head.html` (if adding fonts/meta tags)
- Content files (posts, pages)

### 2. Before Any Commit: Verification Steps

**Step 1: Verify Hugo Server is Running**
```bash
# Check if Hugo is running
tasklist | grep -i hugo

# If not running, start it:
cd 05_shop/markets2mountains
hugo server --buildDrafts --disableFastRender
```

**Step 2: Announce Testing**
Tell the user: "Testing changes in browser before committing..."

**Step 3: Ask User to Verify**
For any config change, ask:
> "Please verify in your browser (http://localhost:[PORT]/):
> - [ ] Homepage renders correctly?
> - [ ] Individual post renders correctly?
> - [ ] Posts list page renders correctly?
>
> Let me know when you've confirmed, then I'll commit."

**DO NOT commit until user confirms** for MEDIUM or HIGH risk changes.

### 3. Safe Commit Process

**Step 1: Stage Changes**
```bash
git add <specific-files>
# DO NOT use git add . or git add -A
```

**Step 2: Review Diff**
```bash
git diff --staged
```

**Step 3: Create Descriptive Commit**
```bash
git commit -m "$(cat <<'EOF'
Clear description of what changed and why

Details about specific changes made.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

**Step 4: Verify Commit**
```bash
git log --oneline -3
git status
```

### 4. If Rendering Breaks

**Immediate Fix:**
```bash
# Hard reset to last known good state
git reset --hard HEAD~1

# OR if you need to keep some changes:
git reset --soft HEAD~1
git checkout config/_default/params.toml  # Revert specific file
```

**Then:**
1. Tell user: "Rendering broke - reverted to last known good state"
2. Investigate what change broke it (see TROUBLESHOOTING.md)
3. Try smaller, incremental changes
4. Test each change individually

### 5. Known Dangerous Patterns to Avoid

❌ **NEVER COMMIT** without testing:
- Custom layout files in `layouts/_default/`
- cardView = true/false settings
- Changes to multiple config files at once
- Layout/template changes copied from online examples

❌ **NEVER ASSUME** text content changes are safe:
- Even author bio changes should be tested
- Special characters (/, &, <, >) can break TOML parsing

❌ **NEVER BATCH COMMITS**:
- One logical change per commit
- Makes rollback easier
- Easier to identify what broke

### 6. Configuration Change Workflow

For any config file edit:

```
1. Read current file
2. Understand what's changing
3. Make the change
4. Verify Hugo rebuilds successfully (check server output)
5. Ask user to test in browser
6. Wait for user confirmation
7. Commit with descriptive message
8. Update todo list (mark task complete)
```

### 7. Emergency Recovery Commands

Keep these handy:

```bash
# See what's changed
git status
git diff

# Revert specific file
git checkout <file-path>

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Go back to specific commit
git log --oneline -10
git reset --hard <commit-hash>

# Current known-good commit
git reset --hard 0881c7d  # "Switch to clean slug-only URLs"
```

### 8. Testing Checklist (Copy-Paste for User)

Use this template when asking user to test:

```
🧪 Testing required before commit:

Changes made:
- [List specific changes]

Please verify:
- [ ] Homepage (http://localhost:PORT/) renders correctly
- [ ] Click any blog post - does it render correctly?
- [ ] Click "Posts" or browse list - does it render correctly?
- [ ] Hard refresh (Ctrl+F5) to clear cache
- [ ] No console errors (F12 → Console tab)

Reply "✅ confirmed" when ready to commit, or "❌ broken" if issues.
```

### 9. Post-Commit Verification

After committing:

1. **Update todo list** - Mark task as completed
2. **Run git status** - Ensure clean working tree
3. **Check Hugo server** - Still running without errors?
4. **Document in chat** - What was changed and why

### 10. Session Handoff Notes

When ending a session, document:

**Current State:**
- Last commit hash and message
- Hugo server status (running/stopped)
- Any uncommitted changes
- Known issues or warnings

**Next Session Needs:**
- Check Hugo server before continuing
- Verify last known good state
- Review TROUBLESHOOTING.md if rendering was broken

---

## Quick Reference

**Is Hugo running?**
```bash
tasklist | grep -i hugo
```

**Start Hugo:**
```bash
cd 05_shop/markets2mountains
hugo server --buildDrafts --disableFastRender
```

**Broke something?**
```bash
git reset --hard HEAD~1
```

**Test before commit?**
✅ ALWAYS for config changes
✅ ALWAYS for layout changes
✅ ALWAYS for CSS changes
❌ Optional for content (markdown posts)

---

**Last Updated:** 2025-11-16
**Purpose:** Prevent recurring rendering breaks during development
