# Step 1 — UX Exploration: Directory Listings
## Feature: Directory Listings (includes Google Business Profile + Facebook Page)
**Date:** April 18, 2026
**Account Used:** #1718 (SeaShore House Optical) — demo only, NEVER use in public content
**Sources:** Direct observation of PatientEngage UI

---

## Feature Scope (Confirmed by Stakeholder)

Directory Listings is NOT a single feature. It is three practice-level tools under one marketing page:

1. **Directory Listings** (`/u/{id}/marketing/seo/location/{locationId}`) — NAP distribution to 15+ online directories
2. **Google Business Profile** (`/u/{id}/marketing/google-my-business`) — GBP sync (name, phone, address, hours, description, category)
3. **Facebook Page** (`/u/{id}/marketing/facebook-page`) — Facebook page sync (name, phone, address, hours, cover photo, bio, about)

All three share **one source of truth**: the Location record. Edit it once, and it pushes to directories + Google + Facebook.

There is **no admin-level dashboard or report** for this service. It is entirely practice-level. (Confirmed by stakeholder: "There is no super dashboard or tool that goes with this service.")

---

## MODE 1: Before State (The Manual Reality Without This Feature)

### What Practices Do Today (Without Directory Listings)
Most independent optometry practices set up their online listings once — during the initial practice opening or website build — and never touch them again. The listings rot.

### How NAP Data Drifts
- Practice moves locations, changes phone number, updates hours
- Staff updates Google manually (if they remember), forgets Yelp, never heard of Manta
- Different hours on Google vs Facebook vs the practice website
- Old phone number still live on yellowpages.com, superpages.com, mapquest.com
- Fax number from 2015 showing up as primary contact on some directories

### Why This Matters (Local SEO)
- Google's local search algorithm uses **NAP consistency** as a ranking signal
- Inconsistent data across directories = lower confidence score = lower Map Pack placement
- A patient searching "eye doctor near me" sees the competitor with consistent listings ranked higher
- Wrong phone number = lost patient. Wrong hours = patient shows up to a closed office.

### The Triggering Moments
1. A patient calls the old number and can't reach the practice
2. The doctor Googles themselves and sees wrong information
3. A marketing audit reveals the practice is listed on 15 directories with 3 different phone numbers
4. A new competitor appears above them in Google Maps despite worse reviews

### The Manual Fix (What It Would Take)
- Identify all directories where the practice is listed (15-30+ sites)
- Create/claim accounts on each directory individually
- Update NAP data on each one, one at a time
- Some directories don't allow updates (read-only / aggregator-sourced)
- Repeat every time anything changes (new phone, new hours, new doctor)
- Estimated time: 10-20 hours initially, 2-5 hours per change event
- Most practices never do this. The data just stays wrong.

---

## MODE 2: Data Landscape Survey

### URL Structure
- Practice Directory Listings: `/u/{practiceId}/marketing/seo/location/{locationId}`
- Location Edit Form: `/u/{practiceId}/websites/{websiteId}/locations/{locationId}`
- Google Business Profile: `/u/{practiceId}/marketing/google-my-business/location/{locationId}`
- Facebook Page: `/u/{practiceId}/marketing/facebook-page/location/{locationId}`

### A. Directory Listings Page

**Header:**
- Title: "Directory Listings"
- Location dropdown (for multi-location practices): "Rayville - 1215 Hwy 135."

**Location Card (read-only display):**
- Name, Phone, Address, Website
- Last PatientEngage Location Edit timestamp + editor name
- Green checkmark when data is current
- **(Edit)** link → navigates to Location edit form
- **UPDATE LISTINGS** button (gold/prominent) — triggers push of current location data to all directories

**Status Donut Chart:**
- Large visual showing percentage of listings that are Live
- Legend: Live (teal) | Pending Approval (orange) | Processing (red) | Not Live (gray)
- For SeaShore House: 100% Live

**Directory Table:**
| Column | Description |
|---|---|
| Domain | Clickable link to the actual listing on the external directory |
| Status | Live, Live (Not updatable), Pending Approval, Processing, Not Live |
| Domain Authority | Numeric score (SEO authority metric) |

**Observed Directories (15 total for this location):**

| Directory | Status | Domain Authority |
|---|---|---|
| ablocal.com | Live (Not updatable) | — |
| acompio.us | Live | — |
| brownbook.net | Live | — |
| chamberofcommerce.com | Live (Not updatable) | 60 |
| citysquares.com | Live | 48 |
| dexknows.com | Live (Not updatable) | 58 |
| ezlocal.com | Live | 55 |
| giftly.com | Live (Not updatable) | 47 |
| manta.com | Live | 81 |
| mapquest.com | Live (Not updatable) | 88 |
| merchantcircle.com | Live | 79 |
| showmelocal.com | Live (Not updatable) | 54 |
| superpages.com | Live (Not updatable) | 74 |
| tupalo.co | Live (Not updatable) | 41 |
| yellowpages.com | Live (Not updatable) | — |

**Key Observations:**
- Two status types: "Live" (updatable by PatientEngage) and "Live (Not updatable)" (listing exists but PatientEngage can't push changes — aggregator-sourced or claimed elsewhere)
- Domain Authority scores range from 41 to 88 — these are real SEO backlink sources
- 15 directories managed per location
- Each directory link goes directly to the practice's live listing on that site

### B. Location Edit Form

**URL:** `/u/{practiceId}/websites/{websiteId}/locations/{locationId}`

**Fields (the single source of truth):**
- Location Name
- Location Phone Number
- Fax Number (optional)
- Email Contact (optional)
- Street Address 1
- Street Address 2
- Country (dropdown)
- State
- Neighborhood
- City
- ZIP Code
- Location description (long text)
- Short description

**Tracking Numbers Section:**
- Campaigns Landing Pages: Campaign / Location phone
- Google Business Profile: Google / Location phone
- Google Ads: Campaign / Location phone
- ADD TRACKER button
- MANAGE button

**Key Insight:** This single form is the data source for Directory Listings + Google Business Profile + Facebook Page. Edit once, push everywhere. The Tracking Numbers section also shows how call tracking integrates — different tracking numbers can be assigned per channel.

### C. Google Business Profile Page

**URL:** `/u/{practiceId}/marketing/google-my-business/location/{locationId}`

**Toggle:** "Update Google Business Profile" (on/off)
- When enabled: auto-syncs to Google when Location or Business Hours pages are saved
- Note: "Changes may take up to 24 hours to sync with Google"

**Editable Fields (pushed to Google):**
- Location: Name, Phone, Address (from Location record)
- Hours: Full weekly schedule with split hours support (e.g., Wed 8:00am-1:30pm, 2:30pm-4:30pm)
- Description
- Primary Category: dropdown (e.g., "Eye Care Center")
- Website URL

**Read-Only Section (synced FROM Google):**
- "Other Information (To Update Go To Google)"
- Last Synced: 20 Aug 2025, 9:03 AM
- Accessibility attributes (wheelchair accessible seating, restroom, parking lot)

**Key Insight:** Two-way awareness — PatientEngage pushes data TO Google, and also pulls read-only attributes FROM Google to display. The "Last Synced" timestamp shows when the pull happened.

### D. Facebook Page

**URL:** `/u/{practiceId}/marketing/facebook-page/location/{locationId}`

**Toggle:** "Update Facebook" (on/off)
- When enabled: auto-syncs to Facebook when this page is saved or when Location/Business Hours change
- Last Successful Update timestamp shown (e.g., "16 Apr 2026, 01:31")

**Editable Fields (pushed to Facebook):**
- Location: Name, Phone, Address (from Location record)
- Hours: Full weekly schedule
- Cover Photo: Current cover photo + Default cover photo (both editable)
- Website URL
- Email
- Intro Bio (short text)
- About You (longer text)
- Price Range (dropdown: N/A, $, $$, $$$, $$$$)

**Read-Only Section:**
- "Other Information (To Update Go To Facebook)"

**Key Insight:** Facebook page includes Cover Photo management — PatientEngage can push seasonal/promotional cover photos (observed: Glaucoma awareness banner). This is a unique feature not available in most directory management tools.

---

## MODE 3: Workflow Narrative

### Setup Workflow (One-Time)
1. Practice signs up for PatientEngage
2. EyeCarePro team enters practice's Location data (name, address, phone, hours, description)
3. Directory Listings are submitted to 15+ directories
4. Listings go through statuses: Not Live → Processing → Pending Approval → Live
5. Google Business Profile toggle is enabled, connecting to practice's GBP
6. Facebook Page toggle is enabled, connecting to practice's Facebook page
7. Practice reaches "100% Live" status

### Ongoing Maintenance Workflow
1. Practice changes phone number / moves / updates hours
2. Staff (or EyeCarePro team) edits the Location record once
3. Clicks "UPDATE LISTINGS" on the Directory Listings page
4. Google Business Profile auto-syncs (if toggle is on)
5. Facebook Page auto-syncs (if toggle is on)
6. All 15+ directories + Google + Facebook updated from one edit

### What the Practice DOESN'T Have to Do
- Log into Google Business Profile manager
- Log into Facebook Page settings
- Visit 15 individual directory websites
- Remember which directories they're listed on
- Track which ones are updatable vs not
- Check for inconsistencies
- Re-submit data after every change

---

## MODE 4: Emotional Mapping

### Staff Experience
| Moment | Without Feature | With Feature |
|---|---|---|
| Phone number changes | Dread — "Now I have to update 20 different websites" | Confidence — one edit, one click |
| New hours for holiday | Forget half the sites, patients show up to closed doors | Update once, all channels reflect new hours |
| Doctor Googles practice | Anxiety — "Why does it say we close at 3pm? That was 2 years ago" | Pride — everything matches, looks professional |
| Patient reports wrong info | Embarrassment — "Sorry, that listing is outdated" | Rarely happens — data stays consistent |
| Competitor ranks higher | Helplessness — "I don't know why Google prefers them" | Understanding — NAP consistency is a factor they control |
| New marketing audit | Overwhelm — 30+ directories to check manually | Calm — dashboard shows 100% Live with one glance |

### The Core Emotional Shift
**FROM:** "Our online information is probably wrong somewhere, but we don't have time to fix it"
**TO:** "We manage our entire digital footprint from one screen"

---

## MODE 5: Marketing Translation

### Feature → Benefit Translations

| Technical Feature | Marketing Benefit |
|---|---|
| 15+ directory submissions | Your practice shows up everywhere patients search |
| One source of truth (Location record) | Change your info once, it updates everywhere |
| "Live" status tracking with donut chart | See at a glance that your listings are active and accurate |
| Domain Authority scores | Your practice gets SEO credit from high-authority sites |
| Google Business Profile sync | Your Google listing always matches your actual hours and info |
| Facebook Page sync | Your Facebook page stays current without logging into Facebook |
| Cover photo management | Seasonal promotional banners push to Facebook automatically |
| "UPDATE LISTINGS" button | One click to push changes to 15+ directories |
| "Live (Not updatable)" transparency | You know exactly which directories you control and which you don't |
| Tracking numbers per channel | Know which listing generated which phone call |

### Killer Stat Candidates (Need Step 2 Data)
- Total locations with directory listings active
- Average number of directories per location
- Percentage of listings at "Live" status across network
- Google Business Profile connection rate
- Facebook Page connection rate

### Potential Page Angles
1. **"One Edit. Everywhere."** — The single source of truth story
2. **"Your Practice is Listed in Places You've Never Heard Of"** — The invisible directory network
3. **"Wrong Number, Lost Patient"** — The cost of inconsistent data
4. **"Google Trusts Consistency"** — The NAP/SEO ranking signal story
5. **"15 Directories. Zero Logins."** — The automation/time-saving angle

### Persona Connections
- **Dr. "Someday"**: Has never updated listings since 2019. Phone number might be wrong on 10 sites. Directory Listings fixes the backlog.
- **Sarah "Swiss Army Knife"**: She'd have to spend a full day updating directories manually. One click replaces that.
- **The Growth Chaser**: Skeptical about SEO, but NAP consistency is a concrete, measurable ranking signal. Domain Authority scores prove the backlink value.

---

## QUESTIONS FOR STEP 6 (Flagged During Exploration)

1. How many practices/locations have directory listings active? (Need for network stats)
2. What's the typical "Live" percentage across the network? Is 100% common?
3. How many directories does each location get submitted to? (Is 15 the standard, or does it vary?)
4. Do practices ever use the "UPDATE LISTINGS" button themselves, or does EyeCarePro handle it?
5. What's the connection rate for Google Business Profile and Facebook Page across the network?
6. Are there any case study-worthy results from directory listings (e.g., ranking improvements)?
7. Who are the competitors in the directory listing / local SEO space? (Yext, Moz Local, BrightLocal, Synup, etc.)
8. Is there a "before/after" story for a practice that connected all three?
9. How does the cover photo management work at scale — does EyeCarePro push seasonal covers to all practices?
10. What's the pricing story? Is this included in the base program or an add-on?

---

## PROVENANCE
- All UI observations: [OBSERVED] from PatientEngage app, account #1718
- Mode 1 (Before State): [INTERPRETATION] based on industry knowledge
- Emotional Mapping: [INTERPRETATION] based on observed workflow
- Marketing Translations: [INTERPRETATION] editorial synthesis
- No network-level numbers yet — those come in Step 2

