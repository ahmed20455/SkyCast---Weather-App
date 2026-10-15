# SkyCast Weather App — Accessibility Audit

**Live URL:** https://skycast-weather-app-beov.onrender.com/  
**Standard:** WCAG 2.2 Level AA  
**Audit stage:** Initial automated baseline  
**Tool:** axe DevTools 4.13.0  
**Date:** 15 October 2026

## 1. Scope and method

An initial automated accessibility scan was performed on the deployed SkyCast Weather App using axe DevTools. The scan reported five issue instances: four colour contrast failures and one missing HTML language attribute.

These findings are recorded as the initial baseline. No fixes have been applied or verified at this stage.

## 2. Initial findings summary

| ID | Finding | WCAG criterion | Initial status |
|---|---|---|---|
| A-01 | Insufficient contrast on Get Weather button | 1.4.3 — Contrast (Minimum) | Open |
| A-02 | Insufficient contrast on Use My Location button | 1.4.3 — Contrast (Minimum) | Open |
| A-03 | Insufficient contrast on About link | 1.4.3 — Contrast (Minimum) | Open |
| A-04 | Insufficient contrast on Export History as CSV link | 1.4.3 — Contrast (Minimum) | Open |
| A-05 | Missing HTML language attribute | 3.1.1 — Language of Page | Open |

**Initial result:** 5 reported instances across 2 axe rule types. These are automated findings and still require validation and retesting.

---

## A-01 — Insufficient contrast on Get Weather button

- **Location:** City/date search form; `button[type="submit"]`
- **WCAG:** 1.4.3 — Contrast (Minimum), Level AA
- **Detection:** axe DevTools automated scan
- **Observed:** White text (`#FFFFFF`) on a blue background (`#007BFF`) has a reported contrast ratio of 3.97:1. The expected minimum for normal-sized text is 4.5:1.
- **Impact:** Users with low vision may have difficulty reading the button label.
- **Recommended fix:** Adjust the foreground or background colour to achieve a contrast ratio of at least 4.5:1, then retest.
- **Status:** Open — baseline finding; fix not yet attempted.
- **Evidence:** `audit-evidence/A-01-get-weather-contrast.png`

## A-02 — Insufficient contrast on Use My Location button

- **Location:** `.location-btn`
- **WCAG:** 1.4.3 — Contrast (Minimum), Level AA
- **Detection:** axe DevTools automated scan
- **Observed:** White text (`#FFFFFF`) on a green background (`#28A745`) has a reported contrast ratio of 3.13:1. The expected minimum is 4.5:1.
- **Impact:** Users with low vision may have difficulty reading the button label.
- **Recommended fix:** Adjust the foreground or background colour to achieve a contrast ratio of at least 4.5:1, then retest.
- **Status:** Open — baseline finding; fix not yet attempted.
- **Evidence:** `audit-evidence/A-02-use-my-location-contrast.png`

## A-03 — Insufficient contrast on About link

- **Location:** `.about-link`
- **WCAG:** 1.4.3 — Contrast (Minimum), Level AA
- **Detection:** axe DevTools automated scan
- **Observed:** Blue text (`#007BFF`) on a light-grey background (`#F4F4F4`) has a reported contrast ratio of 3.61:1. The expected minimum is 4.5:1.
- **Impact:** Users with low vision may have difficulty reading the link text.
- **Recommended fix:** Adjust the link's foreground colour or background to achieve a contrast ratio of at least 4.5:1. Preserve a visible link distinction and retest.
- **Status:** Open — baseline finding; fix not yet attempted.
- **Evidence:** `audit-evidence/A-03-about-link-contrast.png`

## A-04 — Insufficient contrast on Export History as CSV link

- **Location:** `.export-link`
- **WCAG:** 1.4.3 — Contrast (Minimum), Level AA
- **Detection:** axe DevTools automated scan
- **Observed:** Green text (`#28A745`) on a light-grey background (`#F4F4F4`) has a reported contrast ratio of 2.84:1. The expected minimum is 4.5:1.
- **Impact:** Users with low vision may have difficulty reading the link text.
- **Recommended fix:** Adjust the link's foreground colour or background to achieve a contrast ratio of at least 4.5:1. Preserve a visible link distinction and retest.
- **Status:** Open — baseline finding; fix not yet attempted.
- **Evidence:** `audit-evidence/A-04-export-link-contrast.png`

## A-05 — Missing HTML language attribute

- **Location:** Root HTML element (`html`)
- **WCAG:** 3.1.1 — Language of Page, Level A
- **Detection:** axe DevTools automated scan
- **Observed:** axe reports that the root `<html>` element does not have a `lang` attribute.
- **Impact:** Screen readers may not reliably determine the document's default language, potentially affecting pronunciation and comprehension.
- **Recommended fix:** Declare the page's primary language on the root element, for example, `<html lang="en">`, if English is the primary language.
- **Status:** Open — baseline finding; fix not yet attempted.
- **Evidence:** `audit-evidence/A-05-html-lang-attribute.png`

---

## 3. Limitations

- This is an initial automated scan, not a complete WCAG conformance assessment.
- Automated checks do not establish whether all keyboard, screen reader, responsive, focus-management, or dynamic announcement behaviours are accessible.
- Findings have not yet been manually validated or retested after fixes.
- The final audit conclusions will depend on subsequent keyboard, screen reader, visual, and responsive testing.

## 4. Next steps

1. Complete keyboard-only testing and record reproducible observations.
2. Inspect the relevant HTML and CSS for the reported issues.
3. Implement fixes after documenting the baseline.
4. Rerun axe DevTools and repeat the relevant manual tests.
5. Update each finding's status only after verifying the fix.
6. Document remaining issues and audit limitations honestly.
