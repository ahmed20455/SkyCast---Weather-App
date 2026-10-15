# SkyCast Weather App — Accessibility Audit

- **Live URL:** https://skycast-weather-app-beov.onrender.com/
- **Standard / target:** WCAG 2.2 Level AA
- **Audit stage:** Automated retesting, selected keyboard checks, responsive testing at 320 CSS pixels, browser zoom testing at 200% and 400%, history deletion testing, and selected NVDA screen-reader checks completed
- **Tools used:** axe DevTools 4.13.0, Google Lighthouse (Chrome DevTools), NVDA screen reader with Google Chrome, and manual keyboard testing
- **Audit date:** 15 October 2026

## 1. Executive summary

SkyCast Weather App was evaluated using axe DevTools, Google Lighthouse, keyboard-only testing, responsive layout checks, browser zoom, and functional testing of the history deletion flow.

The initial Lighthouse accessibility score was 76/100, increased to 88/100 during follow-up testing, and reached 100/100 in the latest run. The latest axe DevTools scan reported zero detected issues.

Manual checks confirmed that the tested keyboard interactions work, the history layout remains usable at 320 CSS pixels, the tested layout remains usable at 200% and 400% browser zoom, and the POST-based deletion flow works as tested.

These results apply to the pages, states, and interactions actually checked. Selected screen-reader checks were completed using NVDA with Google Chrome. The audit does not certify full WCAG 2.2 Level AA conformance.

## 2. Scope and method

This audit covers the deployed SkyCast Weather App at the URL above. It combines automated scans with selected manual checks.

- **Automated testing:** axe DevTools 4.13.0 and Google Lighthouse.
- **Keyboard testing:** Tab, Shift+Tab, Space activation, weather search submission, and keyboard-trap checks.
- **Responsive testing:** 320 CSS-pixel viewport and the other widths actually tested.
- **Zoom testing:** browser zoom at 200% and 400%.
- **Functional testing:** POST-based history deletion and rejection of GET deletion requests.

Automated tools only detect a subset of accessibility issues. Results apply to the tested page, browser, viewport, content, and interaction state; they do not prove that every page or state conforms to WCAG.

## 3. Initial axe DevTools baseline

**Tool:** axe DevTools 4.13.0  
**Date:** 15 October 2026  
**Initial result:** five reported instances across two axe rule types.

| ID | Initial finding | WCAG criterion | Status |
|---|---|---|---|
| A-01 | Insufficient contrast on Get Weather button | 1.4.3 — Contrast (Minimum) | Fixed; not detected in latest axe scan (details below) |
| A-02 | Insufficient contrast on Use My Location button | 1.4.3 — Contrast (Minimum) | Fixed; not detected in latest axe scan (details below) |
| A-03 | Insufficient contrast on About link | 1.4.3 — Contrast (Minimum) | Fixed; not detected in latest axe scan (details below) |
| A-04 | Insufficient contrast on Export History as CSV link | 1.4.3 — Contrast (Minimum) | Fixed; not detected in latest axe scan (details below) |
| A-05 | Missing HTML language attribute | 3.1.1 — Language of Page | Fixed; not detected in latest axe scan (details below) |

### Initial findings and evidence

The following details preserve the original baseline so that changes can be tracked rather than erasing the original findings.

#### A-01 — Get Weather button contrast

- **Location:** City/date search form; `button[type="submit"]`
- **Criterion:** WCAG 2.2 SC 1.4.3, Contrast (Minimum), Level AA
- **Initial observation:** white text (`#FFFFFF`) on blue (`#007BFF`), reported ratio approximately 3.97:1. Normal-sized text requires at least 4.5:1.
- **Potential impact:** some users with low vision may have difficulty reading the label.
- **Initial evidence:** `audit-evidence/A-01-get-weather-contrast.png`
- **Latest status:** The button background was changed to `#0066CC` with white text. The verified contrast ratio is 5.56:1 in the normal state and 7.04:1 on hover (`#0056B3`). Both exceed the WCAG AA minimum of 4.5:1 for normal text.

#### A-02 — Use My Location button contrast

- **Location:** `.location-btn`
- **Criterion:** WCAG 2.2 SC 1.4.3, Contrast (Minimum), Level AA
- **Initial observation:** white text (`#FFFFFF`) on green (`#28A745`), reported ratio approximately 3.13:1.
- **Potential impact:** some users with low vision may have difficulty reading the label.
- **Initial evidence:** `audit-evidence/A-02-use-my-location-contrast.png`
- **Latest status:** The location button background was changed to `#187A32` with white text. The verified contrast ratio is 5.42:1 in the normal state and 4.52:1 on hover (`#218838`). Both exceed the WCAG AA minimum of 4.5:1 for normal text.

#### A-03 — About link contrast

- **Location:** `.about-link`
- **Criterion:** WCAG 2.2 SC 1.4.3, Contrast (Minimum), Level AA
- **Initial observation:** blue text (`#007BFF`) on light grey (`#F4F4F4`), reported ratio approximately 3.61:1.
- **Potential impact:** some users with low vision may have difficulty reading the link.
- **Initial evidence:** `audit-evidence/A-03-about-link-contrast.png`
- **Latest status:** The verified contrast ratio is 6.4:1 against the page background (`#F4F4F4`). This exceeds the WCAG AA minimum of 4.5:1 for normal text.

#### A-04 — Export History as CSV link contrast

- **Location:** `.export-link`
- **Criterion:** WCAG 2.2 SC 1.4.3, Contrast (Minimum), Level AA
- **Initial observation:** green text (`#28A745`) on light grey (`#F4F4F4`), reported ratio approximately 2.84:1.
- **Potential impact:** some users with low vision may have difficulty reading the link.
- **Initial evidence:** `audit-evidence/A-04-export-link-contrast.png`
- **Latest status:** The verified contrast ratio is 4.93:1 against the page background (`#F4F4F4`). This exceeds the WCAG AA minimum of 4.5:1 for normal text.

#### A-05 — Missing HTML language attribute

- **Location:** root HTML element (`html`)
- **Criterion:** WCAG 2.2 SC 3.1.1, Language of Page, Level A
- **Initial observation:** axe reported that the root `<html>` element had no `lang` attribute.
- **Potential impact:** assistive technology may not reliably identify the page's default language.
- **Initial evidence:** `audit-evidence/A-05-html-lang-attribute.png`
- **Latest status:** The latest axe DevTools scan reported zero detected issues. The page template was updated to include `<html lang="en">`.

### Latest axe retest

- **Date:** 15 October 2026
- **Result:** **0 issues detected**
- **Interpretation:** The latest axe scan reported zero detected issues in the page state and configuration tested. This result does not establish full WCAG conformance.
- **Important limitation:** A zero-issue scan does not mean every WCAG requirement has passed. Other pages and states, including validation errors, location-permission outcomes, and populated history, were not comprehensively tested.

## 4. Lighthouse results

| Run | Accessibility score | Notes |
|---|---:|---|
| Initial baseline | 76/100 | Contrast, missing `lang`, missing main landmark, and repeated-link warning were reported |
| Follow-up | 88/100 | Score improved; contrast and language findings were still listed at that stage |
| Latest | 100/100 | No longer listed the earlier contrast, `lang`, main-landmark, or repeated-link warnings |

The latest Lighthouse run also listed **10 items for manual review**, **11 passed audits**, and **52 not applicable**. The 10 manual-review prompts are not automatically passed by a score of 100.

### Interpretation

The increase from 76 to 100 is encouraging and the latest axe scan reported zero issues. These results support saying that the tested automated checks are currently clear. They do **not** support claiming complete WCAG 2.2 AA conformance without further manual evaluation.

## 5. Manual keyboard testing

**Environment:** Google Chrome on the deployed SkyCast Weather App  
**Date:** 15 October 2026

| ID | Test | Observed result | Status |
|---|---|---|---|
| K-01 | Press Tab repeatedly from a page reload | Focus moved through tested interactive elements in a logical order; visible focus was observed | Pass for tested path |
| K-02 | Press Shift+Tab | Focus moved backwards as expected | Pass |
| K-03 | Focus a native button and press Space | The tested button activated | Pass for tested button |
| K-04 | Submit a Hyderabad weather search using the keyboard | Focus remained understandable and navigation could continue | Pass for tested interaction |
| K-05 | Continue tabbing through the tested page | No keyboard trap encountered | Pass for tested path |

These checks cover only the tested keyboard interactions. Focus visibility and behavior across all page states have not been comprehensively verified.

## 6. History deletion and related Lighthouse findings

### L-01 — Repeated Delete controls

- **Original report:** Lighthouse flagged repeated Delete links beside history entries.
- **Accessibility concern:** a control should make clear which entry it acts on when that context is needed to distinguish repeated controls.
- **Change made:** the delete control was updated to use a POST form/button and a descriptive accessible name for the associated history entry.
- **Latest status:** The descriptive accessible names were checked using NVDA, and the Delete buttons were announced understandably during the tested interactions. Other history states and controls were not comprehensively evaluated.

### L-02 — Main landmark

- **Original report:** Lighthouse reported that the document did not have a main landmark.
- **Change made:** the primary page content was changed to use a `<main class="container">` landmark.
- **Latest status:** Lighthouse no longer lists the earlier warning. The primary content uses a `<main>` landmark in the updated template. Other relevant pages were not comprehensively checked for landmark structure.

### L-03 — Deletion through GET

- **Original concern:** the delete route accepted GET requests and performed a destructive action.
- **Change made:** deletion was changed to use POST, with a form and submit button.
- **Verification reported:** a GET request to the delete endpoint returns **HTTP 405 Method Not Allowed**; the POST deletion flow has also been tested.
- **Current status:** I tested the POST flow, and a GET request returns HTTP 405.

## 7. Additional screen-reader observations

- NVDA announced city names and weather temperatures clearly in the tested weather results.
- The city search field and Delete buttons had understandable accessible names during testing.
- Keyboard navigation through headings, landmarks, form fields, and buttons worked as expected on the tested page.
- These checks provide evidence of basic screen-reader usability for the tested interactions; they do not establish complete WCAG 2.2 Level AA conformance.

## 8. Responsive and zoom retest

**Responsive viewport:** 320 CSS pixels  
**Browser zoom:** 200% and 400%  
**Result:** Pass for the checks performed.

I confirmed that the layout and history controls remained usable at a 320 CSS-pixel viewport and at 200% and 400% browser zoom. Keyboard navigation was also tested after the layout changes.

These results apply to the pages, content states, and interactions actually checked.

## 9. Final audit status

The planned audit pass is complete for the automated scans, selected keyboard interactions, responsive checks at 320 CSS pixels, browser zoom testing at 200% and 400%, and the tested history deletion flow.

The latest axe DevTools scan reported zero detected issues, and the latest Lighthouse run returned an accessibility score of 100/100. These results apply to the tested pages, states, and interactions and do not establish full WCAG 2.2 Level AA conformance.

Selected screen-reader checks were completed using NVDA with Google Chrome. NVDA announced the tested city names, temperatures, search field, Delete buttons, headings, landmarks, form fields, and buttons as expected. These checks do not establish complete screen-reader compatibility or full WCAG 2.2 Level AA conformance. Real-device testing was not performed.