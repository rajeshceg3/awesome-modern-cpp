---
name: verify-resource-list
description: Verify awesome-modern-cpp's actual resource-list source, Jekyll entry linkage and bounded reader-link journeys before editing its catalog or site files.
---
# Verify modern C++ resource list
## Surface
Reader-facing Markdown resource catalog and Jekyll source. Not a C++ executable or library. README and site index share content via index.md symlink. Original author/credit and upstream contribution links are intentional; this helper does not rewrite attribution to the fork owner.
## Launch
Python3 standard library only. No app server required for Markdown/link-source verification. Run from repo root. Full Jekyll site rendering requires Ruby/Jekyll, not installed or tested by this helper; do not call source-contract checks a rendered-site build.
## Doctor
`python3 .cursor/skills/verify-resource-list/helpers/drive.py doctor --out .verification-evidence/doctor`
Checks README frontmatter, actual index symlink target and layout content/title slots, with no network effects.
## Drive
`python3 .cursor/skills/verify-resource-list/helpers/drive.py drive --out .verification-evidence/run`
Checks the actual222 Markdown resource link shapes and required source sections, then opens the actual C++ Core Guidelines and Compiler Explorer links with HTTP GET, retaining resolved URL, status and HTML title. This is a bounded reader-link journey, not all-resource health.
## Evidence
JSON survives cleanup in requested directory. Parse errors, wrong site entry or a selected resource failure exit nonzero. No package installation, code execution from listed sites, downloads of books, commercial site interaction, contact email or messages.
## Cleanup
Only short-lived Python process and HTTP reads. No shared data/server/scratch credentials created. Never delete retained JSON during cleanup.
## Helpers
Executable helpers/drive.py supports doctor/drive and --out. Keep features/README.md current. Build/publication and layout pixel acceptance remain separate from link checks.
