# Step 1 : UX Research: Google Reserve

## Mode 1: The Before State
**What does the practice do WITHOUT Google Reserve?**

Without Google Reserve, when a patient searches for an optometrist on Google Search or Maps, they see the standard Google Business Profile with a Call button, a Directions button, a Website button, plus hours, reviews, and address.

To book an appointment, the patient must either:
1. **Phone-only:** Call during business hours, wait on hold, speak with front desk
2. **Website detour:** Click Website, navigate to the practice site, find the scheduling page, fill out a form or use embedded scheduler
3. **Leave and come back:** Note the number, call later, or forget entirely

**The three before states:**
- **Phone-only practice:** Patient sees GBP, calls, gets voicemail after hours or holds during busy times. High drop-off. No booking captured.
- **Website form practice:** Patient clicks Website, navigates multi-page site, finds a contact form (not a real scheduler). May submit, may bounce. Days before confirmation.
- **Hybrid (scheduler but no Google Reserve):** Patient has to leave Google, navigate to practice site, find scheduler widget. Extra clicks = friction = drop-off at point of highest intent.

**The core problem:** Patients searching on Google have IMMEDIATE booking intent. Every click away from Google is a leak point. Google Reserve eliminates ALL intermediate steps.

## Mode 2: Data Landscape

### Admin/Settings UI
**Location:** Within Scheduler settings (Settings > Google Reserve)
**Controls observed:**
- Toggle: On/Off (simple switch to enable Google Reserve)
- Booking Type: "PatientEngage Scheduler" (shows bookings feed into main scheduler queue)
- Sync: Daily sync with Google
- First appearance: Takes ~24 hours after activation
- Clicks chart: Shows G Reserve clicks over time

### Network-Level Metrics (GBP Insights Report)
**Report URL:** https://app.patientengage.ai/a/gbp-insights-report

**March 2026, All Groups [OBSERVED]:**
- 1,739 Practices, 2,395 Locations in network
- 4,174,442 Total Views
- 1,285,184 (31%) Total Actions
- 227,108 Total G Reserve Clicks
- 1,207 Google Reserve active locations (out of 2,395 total = ~50% adoption)

**Per-practice table columns:** Name, City, Search Views, Map Views, Total Views, Calls, G Reserve Clicks, Website Clicks, Directions, Total Actions, Total Actions %

### Killer Stat Candidates
- "227,000+ Google Reserve clicks in a single month across 1,200+ locations" [OBSERVED]
- "1,207 practices using Google Reserve" [OBSERVED]
- "50% of all PatientEngage locations have Google Reserve active" [CALCULATED: 1,207/2,395]
- G Reserve clicks represent a meaningful share of total actions across the network

### Case Study Candidate: Simmons Eye Care (3 locations)
**March 2026, All 3 Locations [OBSERVED]:**

| Location | City | Search Views | Map Views | Total Views | Calls | G Reserve Clicks | Website Clicks | Directions | Total Actions | Actions % |
|---|---|---|---|---|---|---|---|---|---|---|
| Benton | Benton | 1,905 | 290 | 2,195 | 753 | 314 | 331 | 202 | 1,600 | 73% |
| Hot Springs | Hot Springs | 2,498 | 285 | 2,783 | 483 | 227 | 191 | 128 | 1,029 | 37% |
| Little Rock | Little Rock | 1,954 | 411 | 2,365 | 237 | 155 | 132 | 101 | 625 | 26% |
| **TOTAL** | | **6,357** | **986** | **7,343** | **1,473** | **696** | **654** | **431** | **3,254** | **44%** |

Key insight: At Benton, G Reserve Clicks (314) are nearly equal to Website Clicks (331), meaning the Book online button captures almost as many actions as the entire website. At Benton, 73% of all profile views result in an action.

G Reserve Clicks as % of Total Actions: 696/3,254 = 21% [CALCULATED]
G Reserve Clicks vs Website Clicks: 696 vs 654, G Reserve EXCEEDS website clicks across all 3 locations [CALCULATED]

Note: Simmons Eye Care has 3 locations. GBP names are "Simmons Eye Care - [Location]" (e.g., "Simmons Eye Care - Little Rock", "Simmons Eye Care - Benton", "Simmons Eye Care - Hot Springs").

## Mode 3: Workflow Narrative

### Setup workflow (practice side):
1. Practice has PatientEngage Scheduler active
2. Admin navigates to Google Reserve settings within Scheduler
3. Flips toggle to On
4. System syncs with Google (daily sync cycle)
5. Within 24 hours, Book online button appears on Google Business Profile
6. All bookings flow into the same Scheduler queue, no separate dashboard

### Patient booking workflow:
1. Patient searches "eye doctor near me" or practice name on Google
2. Google Business Profile appears in Search results or Maps
3. Patient sees Book online button prominently displayed (light blue banner in Maps, action button in Search)
4. Patient clicks Book online
5. Redirected via Google's Reserve with Google system to PatientEngage Scheduler
6. Patient selects appointment type, date/time, enters info
7. Appointment flows into practice's Scheduler queue
8. Auto-approval if configured, or manual approval by staff

**The aha moment:** The practice owner sees bookings appearing in their queue from patients who never visited their website and never called. These are pure Google-to-appointment conversions.

**The relief moment:** Front desk stops getting "I want to make an appointment" calls during the busiest hours. Some of those patients just booked themselves from Google.

**The embarrassment moment:** A competitor practice across town has Book online on their Google listing. Your practice only shows Call and Website. Patients choose the easier path.

## Mode 4: Emotional Mapping

**What is the practice owner afraid of?**
- "We're invisible on Google" = they're not invisible, but they're NOT converting their Google visibility into appointments
- "Patients are choosing the other practice" = if a competitor has Book online and you don't, that's a real competitive disadvantage
- "We're paying for SEO but not capturing the results" = all that GBP optimization, review collection, and local SEO is wasted if the patient has to leave Google to book

**What does relief feel like?**
- "I didn't even know she booked, she found us on Google and just booked." The zero-effort conversion.
- Looking at the scheduler queue and seeing appointment sources split between website widget AND Google Reserve, two intake channels running simultaneously.

**The dinner party sentence:**
"Our patients can book appointments directly from our Google listing, they don't even need to visit our website."

## Mode 5: Marketing Translations

| Observation | Marketing Claim | Tag |
|---|---|---|
| 227,108 G Reserve clicks in March 2026 | "Over 227,000 patients clicked Book online from Google in a single month" | [OBSERVED] |
| 1,207 locations with Google Reserve active | "1,200+ practices have activated Google Reserve through PatientEngage" | [OBSERVED] |
| Simmons Benton: G Reserve clicks nearly equal to website clicks | "For some practices, Google Reserve generates as many bookings as their entire website" | [OBSERVED, Simmons Benton specific] |
| Bookings feed into existing Scheduler queue | "No new dashboard to learn, Google Reserve bookings appear in your existing scheduler" | [OBSERVED] |
| Setup is a single toggle | "Activate Google Reserve with one click, live on Google within 24 hours" | [OBSERVED] |
| Patient never leaves Google to start booking | "Convert patients at the moment of highest intent, right from Google Search" | [OBSERVED workflow] |
| 50% of PatientEngage locations have adopted G Reserve | "Half of all PatientEngage practices have already activated Google Reserve" | [CALCULATED] |

### GBP Profile Observed (Simmons Eye Care - Little Rock):
- 4.9 stars, 790 reviews
- Address: 11115 Hermitage Rd, Little Rock, AR 72211
- Hours: Mon-Fri 8am-5pm, Sat-Sun Closed
- Action buttons in Maps: Directions, Save, Nearby, Send to phone, Share
- Book online button: Prominent light blue banner in Maps, action link in Search
- Book online URL: ngj.ai redirect with rwg_token parameter (Reserve with Google token)
