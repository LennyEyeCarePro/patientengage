# Step 4 — Observe the Resulting View
## Feature: Campaigns-To-Go
**Date:** April 10, 2026
**Resulting View Location:** Campaign preview carousel inside PatientEngage admin (setup flow + results section)
**Practice Used for Observation:** North Park Vision (#1813) — campaign setup preview; Delran Eye Assoc. (#4898) — results/pieces view

---

## Where the Patient-Facing Output Lives

Unlike features that live on a website widget or embed, Campaigns-To-Go output is **distributed across multiple channels simultaneously**. There is no single URL a patient visits — instead, the campaign reaches patients where they already are:

1. **Email inbox** — the primary channel (drives 95%+ of appointment attribution)
2. **Facebook feed** — social posts published to the practice's page
3. **Google Business Profile** — GMB posts visible in Google Maps/Search
4. **Instagram feed** — social posts published to the practice's IG
5. **Campaign landing page** — hosted on the practice's PatientEngage subdomain, linked from email/social
6. **In-office poster** — printed for waiting room display
7. **Facebook cover photo** — updated for the duration of the campaign

The preview carousel in the campaign setup flow (and the results section of past campaigns) is the only place to see all 7 pieces together.

---

## Campaign Pieces — Full Inventory [OBSERVED]

### 1. Landing Page
- **What patients see:** A branded page with the practice's logo, phone number with live hours ("Closing at 5:30 pm"), review count badge ("297 Reviews — Super Popular"), and a "Book Eye Exam" CTA button. Below the header: campaign-specific content with headline, body text, and the campaign imagery.
- **Branding:** Fully practice-branded — logo, phone, booking link, review count all pulled from the practice's PatientEngage profile.
- **CTA path:** Patient clicks email link → lands here → clicks "Book Eye Exam" or calls the practice number.
- **Design quality:** Professional, clean layout. The review badge and live hours create urgency. The booking CTA is prominent.

### 2. Email
- **What patients see:** Practice logo at top, followed by phone number CTA and "Book Eye Exam" CTA buttons, then the campaign banner image, then body text. Unsubscribe link at the very top.
- **Key elements:** Two clear CTAs (call + book), campaign imagery, professional formatting.
- **Utilities available to staff:** "Send Preview" (enter email address to send a test), "Copy HTML" (export raw email HTML).
- **Design quality:** Clean, mobile-friendly email layout. CTAs are above the fold.

### 3. Campaign Poster
- **What patients see:** Large print-ready poster with campaign headline and imagery. Designed for in-office display (waiting room, exam lanes).
- **Format:** Full-bleed image with large typography. No practice-specific branding on the poster itself — it's the campaign creative only.

### 4. Facebook Cover
- **What patients see:** Wide-format cover photo for the practice's Facebook page. Updated automatically when the campaign starts, reset when it ends ("Reset Cover" is a separate scheduled item visible in the results section).
- **Design quality:** Professional, eye-catching. Same creative as the campaign.

### 5. Facebook Posts (×4 variations)
- **What patients see:** 4 unique social media posts, each with a different image and headline variation on the campaign theme. Posted weekly throughout the campaign month (e.g., Mar 02, 09, 16, 23).
- **Copy structure:** Each post has a unique image + body text that ends with "[Practice Name]" and "[Landing Page Link]" — merge fields that get populated per-practice.
- **Scheduling:** Posts are auto-scheduled at 1 pm EST on their respective dates.

### 6. GMB Posts (×4 variations)
- **What patients see:** Same 4 post variations as Facebook, formatted for Google Business Profile. Visible on the practice's Google Maps listing and Google Search results.
- **Design quality:** Identical creative to Facebook — consistent cross-channel messaging.

### 7. Instagram Post (×1)
- **What patients see:** Single square-format image post with caption. Same campaign creative adapted for Instagram's square ratio.
- **Caption:** Body text with "Practice Name" merge field. No landing page link (Instagram doesn't support clickable links in post captions).

---

## Campaign Results Section — Delran Eye Assoc. March 2026 [OBSERVED]

The campaign detail page (`/u/4898/marketing/campaigns/72181`) shows all scheduled/posted pieces in a timeline grid:

### Layout
- **Top section:** Campaign image, title ("Allergies Winter Is It Eye Allergies"), date range (Mar 02 – Mar 31), status ("Ended"), and metrics (Impressions, Views, Appointments).
- **Content grid:** All pieces displayed as thumbnails with channel icons (Facebook, Google, Instagram, envelope for email) and schedule dates. Each piece has a context menu with "View" and "Edit" options.
- **EHR Patient Filter:** Configuration section at the bottom showing targeting options (Age, Last Appointment date, ZIP, City, etc.).

### Piece Status Indicators
- Channel icons (Facebook ●, Google G, Instagram camera, envelope) show which channel each piece targets
- "Not Posted" warning triangle appears when a scheduled post failed to publish (observed on one Google post)
- "Posted" green checkmark confirms successful publication
- "Reset Cover" entry appears at the end — scheduled to restore the original Facebook cover after the campaign ends

### Key Observation
The results section shows the **full timeline of multi-channel activity** for a single campaign. For the Allergies Winter campaign, there were approximately 14 individual pieces scheduled across the month: 1 landing page, 1 email, 1 Facebook cover, 4 Facebook posts, 4 Google posts, 1 Instagram post, and 1 cover reset — all from a single "schedule campaign" action by the practice.

---

## Patient Experience Walkthrough

### Email → Landing Page → Appointment (Primary Funnel)
1. **Patient receives email** in their inbox. Subject line and preview text are campaign-specific. Practice logo and name visible.
2. **Patient opens email** → sees campaign banner, practice phone number, and "Book Eye Exam" button above the fold.
3. **Patient clicks any link in email** → taken to the campaign landing page on the practice's PatientEngage subdomain.
4. **On landing page**, patient sees the practice header (logo, phone with live hours, review count, booking button) plus campaign content.
5. **Patient clicks "Book Eye Exam"** → redirected to practice's online booking system (or calls the displayed phone number).

### Social → Landing Page → Appointment (Secondary Funnel)
1. Patient sees a Facebook/Google post in their feed while scrolling.
2. Post includes campaign image and copy with a link to the landing page.
3. Click-through leads to the same landing page as email.

### Friction Points
- **None observed in the funnel itself.** The email-to-landing-page-to-booking flow is clean.
- **Instagram limitation:** No clickable link in post caption — patients would need to visit the practice's profile link. This is an Instagram platform limitation, not a PatientEngage issue.
- **One "Not Posted" Google post** observed in Delran's March campaign — indicates occasional publishing failures to Google, but this is a minor operational detail, not a patient-facing issue.

---

## Observations for Marketing Page

### The "7 Pieces, 1 Click" Story
The most compelling insight from Step 4 is the **scope of what gets created automatically**. When a practice schedules one campaign, they get 7 distinct marketing pieces across 5+ channels, all professionally designed, all branded with their practice info, all scheduled and posted automatically. This is the core "Campaigns-To-Go" value proposition.

**Recommended marketing framing:** "One click. Seven marketing pieces. Five channels. Every month."

### The Landing Page Is the Differentiator
From Step 3 data, Delran's 10% landing page view rate was the standout metric. Now seeing the actual landing page, it's clear why: the page includes the practice's real-time review count ("297 Reviews — Super Popular"), live hours ("Closing at 5:30 pm"), and a direct booking button. It's not just a campaign page — it's a mini practice homepage optimized for conversion.

### Professional Quality at Scale
The creative quality is noticeably professional — not "small business clip art." The imagery, typography, and layout would pass as agency work. This matters because the alternative for most independent practices is either no marketing or low-quality DIY efforts.

### Multi-Channel Consistency
Every piece uses the same creative theme adapted for each channel's format. A patient who sees the Facebook post, then gets the email, then visits the landing page sees a consistent message. This is textbook multi-channel marketing — normally requiring a marketing team or agency to coordinate.

---

## Step 4b — Screenshot Brief (Campaigns-Specific)

### Patient-Facing Shots Needed

```
5. [Campaign Email Preview]
   Setup: Navigate to any active campaign → click VIEW → navigate to "Email" piece
   Highlight: Practice logo, CTA buttons (phone + Book Eye Exam), campaign banner
   Why it matters: Shows the professional, branded email patients actually receive

6. [Campaign Landing Page]
   Setup: Navigate to any active campaign → click VIEW → "Landing Page" piece
   Highlight: Review count badge, live hours, Book Eye Exam CTA, campaign content
   Why it matters: Demonstrates the complete conversion-optimized page auto-generated per campaign

7. [All 7 Pieces Overview]
   Setup: Navigate to a past campaign results page (e.g., /u/4898/marketing/campaigns/72181) → scroll to content grid
   Highlight: The full grid of all pieces with channel icons (FB, Google, IG, email, landing page, poster, cover)
   Why it matters: Visual proof of "7 pieces from 1 click" — the core value proposition

8. [Social Post Variations]
   Setup: Navigate to campaign VIEW → "Facebook Posts" piece
   Highlight: 4 unique post variations with different images and copy
   Why it matters: Shows the variety and quality of auto-generated social content
```

---

## Provenance Notes
- All campaign piece observations: [OBSERVED] — viewed directly in the PatientEngage campaign preview carousel and results section
- Piece count and types: [OBSERVED] — cycled through the full carousel (Landing Page → Email → Campaign Poster → FB Cover → Facebook Posts → GMB Posts → Instagram Post)
- Channel icons and status indicators: [OBSERVED] — from Delran campaign results grid
- Patient experience walkthrough: [OBSERVED + INFERRED] — based on visible CTAs and link structure; did not actually click through to a live booking page
- Marketing observations: [INTERPRETATION] — editorial analysis based on observed features

---

## Auto-Save Confirmation
This output should be POSTed to:
```
POST http://localhost:8080/api/feature/Campaigns/stepdata/step4
```
