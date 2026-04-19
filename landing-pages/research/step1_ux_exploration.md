# Step 1 -- UX Exploration: Landing Pages
## Feature: Campaign Landing Pages
**Date:** April 19, 2026
**Account Used:** #1718 (SeaShore House Optical) -- demo only, NEVER use in public content
**Sources:** Direct observation of live landing page + stakeholder description of content sources

---

## Feature Scope

A PatientEngage Landing Page is a standalone, conversion-focused page built for a specific practice location. It is NOT a full website. It is a single page designed to convert a visitor into a booked appointment.

The landing page pulls content from multiple sections of the PatientEngage platform:

1. **Announcements** -- promotional banners or alerts (e.g., seasonal offers, COVID protocols)
2. **About Us** -- practice description, services list, practice images
3. **Locations** -- address, neighborhood description, amenity badges
4. **Hours** -- full weekly schedule with split-hour support + special date overrides
5. **Our Team** -- doctor headshots, bios, credentials, languages, attributes
6. **Insurance** -- accepted insurance plans with logos
7. **Frames** -- frame brand gallery (not observed on this page, but available)
8. **Contact Lenses** -- contact lens brands (not observed on this page, but available)
9. **Testimonials** -- patient reviews with reviewer names
10. **Google** -- Google Map embed, accessibility attributes (wheelchair accessible, parking, etc.)

Additionally, the scheduling component is flexible:
- If the practice uses PatientEngage Scheduler: embedded scheduler widget
- If not: a contact form OR a link to their third-party scheduler

**Key Insight:** The landing page is assembled from data that already exists in PatientEngage. The practice does not build the page from scratch. They maintain their data in the platform (team bios, hours, insurance, etc.) and the landing page reflects it automatically.

**Campaign-Specific Targeting:** Each landing page can have targeted content at the top that matches the marketing initiative. A UV awareness campaign gets a UV article and promotional image. A Dry Eye campaign would get Dry Eye-specific content. A Back to School campaign gets pediatric-focused content. The campaign content sits above the scheduler and practice data, so the visitor sees the relevant message first, then the booking path, then the trust signals (team, insurance, reviews).

**Scheduler Integration (Observed):** The embedded PatientEngage Scheduler on the landing page includes:
- Doctor dropdown ("Any Eye Doctor" or specific doctor)
- Exam type dropdown ("Comprehensive Exam" or specific type)
- Full calendar grid showing available appointment slots by day
- Multiple time slots per day (observed: 10:15 AM, 10:30 AM, 10:45 AM, etc.)
- "More" link for additional time slots
- "Call Us" link + "Next" navigation
- Phone CTA button below the scheduler

This is not a simple "Book Now" button. It's a full scheduling experience embedded directly in the landing page, reducing friction to near zero.

---

## MODE 1: Before State (The Manual Reality Without This Feature)

### What Practices Do Today (Without a Dedicated Landing Page)

Most independent optometry practices send paid ad traffic or social media links to their homepage. The homepage is designed for everyone: existing patients, job seekers, insurance companies, vendors. It is not designed for a first-time visitor who searched "eye doctor near me" and needs to decide in 10 seconds whether to book.

Common alternatives:
- **Homepage as landing page:** Too much navigation, too many distractions. Visitor clicks around, gets lost, leaves.
- **DIY landing page builders (Unbounce, Leadpages, Instapage):** The practice (or their marketing person) builds a page from scratch. Content is copied from the website. When hours change, the website gets updated but the landing page doesn't. Data drifts.
- **No landing page at all:** Ad clicks go to a generic "Contact Us" page or even worse, a Google Maps listing.

### The Problems

1. **Data Drift:** A standalone landing page built in a third-party tool is disconnected from the practice's source of truth. Hours change, a new doctor joins, an insurance plan is added -- the website gets updated, but the landing page shows stale data. Patients see different hours on the ad landing page vs. the website vs. Google. Trust drops.

2. **No Clinical Content:** Generic landing page builders don't know what an optometry practice needs to show. They don't have insurance logo databases. They don't know that "Accepting New Patients" and "Same-Day Appointments" are conversion triggers. They don't pull testimonials from a review management system.

3. **No Scheduling Integration:** The landing page shows a phone number but no way to book online. Or it embeds a third-party widget that looks disconnected from the page. The conversion path has friction.

4. **Maintenance Burden:** Someone has to keep the landing page current. That person is usually the office manager, who is already handling check-ins, insurance verification, and phone calls. The landing page falls to the bottom of the priority list.

### The Triggering Moments

1. Practice runs Google Ads and the ad clicks go to the homepage. Conversion rate is low. "Why are we spending money on ads if nobody books?"
2. A patient arrives with wrong hours they saw on a promotional page. Staff realizes the landing page hasn't been updated since last year.
3. A new doctor joins the practice. The website gets updated, the landing page still shows the old team.
4. The practice owner visits their own landing page and realizes the insurance section is missing half the plans they accept.

---

## MODE 2: Data Landscape Survey

### URL Structure
- Live landing page: `https://www.{practice-domain}.com/default/{campaign-slug}/{locationId}/`
- Example: `/default/book-eye-exam-today/2120/`

### Landing Page Content Sections (Observed)

#### A. Header Bar
- Practice name (left)
- **Phone number CTA:** Clickable tel: link with tracking number
- Real-time status: "Reopens Mon, 7:00 am" (shows current open/closed state)
- **"Book Eye Exam" button:** Anchors to scheduling section
- Persistent at the top of the page

**Data source:** Locations (name, phone), Hours (open/closed status)

#### B. Campaign-Targeted Content (Announcement)
- **This is the section that changes per campaign.**
- Example observed: UV Awareness campaign -- "Be wise with your eyes!"
- Includes: educational article copy about UV radiation and eye health + promotional image (woman wearing sunglasses with "Be Wise" text)
- Campaign content sits at the TOP of the page, immediately below the header
- This is where the landing page becomes targeted: a Dry Eye campaign would show Dry Eye content, a Back to School campaign would show pediatric content, etc.

**Data source:** Announcements (campaign-specific content and images)

#### C. Scheduling Section (Embedded Scheduler)
- Heading: "Book an Exam Today"
- Doctor dropdown: "Any Eye Doctor" or select specific doctor
- Exam type dropdown: "Comprehensive Exam" or specific type
- Full calendar grid: shows available slots for each day of the week
- Multiple time slots per day (e.g., 10:15 AM, 10:30 AM, 10:45 AM)
- "More" link for additional time slots per day
- "Call Us" link + phone CTA button
- "Next" navigation for additional dates
- If the practice doesn't use PatientEngage Scheduler: a contact form OR a link to their third-party scheduler

**Data source:** Scheduler integration (real-time availability)

#### D. About Us
- Practice description (long-form narrative)
- Practice image (large, right-aligned)
- Services list with checkmarks (two-column layout):
  - Astigmatism Treatment, Comprehensive Eye Exams, Diabetic Retinopathy, Dry Eyes
  - Emergency Eye Care, Low Vision, Pediatric Eye Care, Myopia Management
  - Retinal Imaging, Vision Therapy, w/digital low, Allergy related eye problems, Eye LASIK
- Practice photos (thumbnail gallery with lightbox)
- "Show More" link for additional content

**Data source:** About Us (description, services), image gallery

#### E. Location & Hours
- Section heading: "Location & Hours"
- Real-time status: "Closed - Reopens monday at 7:00 am"
- Embedded Google Map with practice pin
- Phone number + address displayed
- Amenity badges organized into three groups:
  - **Convenient Hours:** Open Weekends, Same-Day Appts, Walk-ins
  - **Access:** Onsite Parking, Free Parking, Wheelchair Accessible, Bike Parking, Public Transit, COVID Screening
  - **On Site Services:** Free Wifi, On Site Lab, Same-Day Glasses

**Data sources:** Locations (address, phone), Hours (schedule, open/closed status), Google (map embed, accessibility attributes)

#### F. Our Team
- Section heading: "Our Team"
- For each doctor:
  - Headshot photo (links to full bio page)
  - Name with credentials (e.g., "Dr. Bryan Chi, O.D.")
  - Bio text with "Show More" truncation
  - Attribute badges: Accepting New Patients, Family Friendly, In Person Appointments
  - Languages spoken (e.g., English, Portuguese)

**Data source:** Our Team (photos, bios, credentials, attributes, languages)

#### G. Insurance Plans
- Section heading: "Medical and Vision Insurance plans"
- Subtext: "Have another plan? Benefit questions? Paying out of pocket? Call us at [phone], We are happy to help."
- Insurance logo grid: 40+ insurance plan logos with names
- "Show All" button to expand full list
- Plans observed include: Blue Cross Blue Shield, Aetna, VSP, Medicaid, AARP plans, and many others

**Data source:** Insurance (plan list with logos)

#### H. Patient Reviews
- Section heading: "Patient Reviews"
- Testimonial carousel (swipeable, with dot navigation)
- Each review: quote text + reviewer first name and last initial
- 9 reviews observed in carousel
- Previous/Next slide buttons

**Data source:** Testimonials (review text, reviewer names)

#### I. Footer CTA
- Heading: "Schedule Your Eye Exam Today"
- Phone CTA + Book Online button
- Final conversion push

#### J. Footer
- Practice address
- "Powered by PatientEngage" branding
- "Book Eye Exam" button (sticky/persistent)

#### K. Additional Sections (Available but not on every page)
- **Frames section:** Frame brand gallery (brands the practice carries)
- **Contact Lenses section:** Contact lens brand gallery

---

## MODE 3: Workflow Narrative

### Setup Workflow (How a Landing Page Gets Created)

1. Practice data already exists in PatientEngage: About Us content, team bios, hours, insurance plans, testimonials, location details
2. EyeCarePro team creates a landing page campaign (e.g., "Book Eye Exam Today" or "UV Awareness" or "Dry Eye Treatment")
3. Campaign-targeted content is created for the top of the page (announcement with educational copy + promotional image matching the campaign theme)
4. The rest of the page is assembled from existing PatientEngage data sections -- no copy-paste, no manual content creation
5. Scheduling integration is configured: PatientEngage Scheduler (with doctor/exam type dropdowns + calendar), OR a contact form, OR a third-party scheduler button
6. Tracking phone number is assigned for the campaign
7. Page goes live at the practice's domain under /default/{campaign-slug}/{locationId}/

### Maintenance Workflow (Ongoing)

This is where the value lives:

1. Practice updates their hours in PatientEngage --> landing page hours update automatically
2. New doctor joins and their bio is added to Our Team --> landing page team section updates
3. Practice starts accepting a new insurance plan --> landing page insurance grid updates
4. New patient reviews come in through the review system --> landing page testimonials update
5. Seasonal announcement is created --> landing page can show it

**The practice never touches the landing page directly.** They maintain their data in PatientEngage, and the landing page reflects the current state.

### Conversion Path

Visitor arrives (from ad, social, search) --> sees practice info, team, reviews, insurance --> books via scheduler/form/phone --> conversion tracked via campaign phone number

---

## MODE 4: Emotional Mapping

### For the Practice Owner (Doctor)

| Stage | Emotion | Thought |
|---|---|---|
| Before | Frustrated | "We're spending $2,000/month on Google Ads and I don't know if anyone's booking from them." |
| Triggering moment | Alarmed | "I just clicked our own ad and it goes to the homepage. There's no booking button above the fold." |
| Discovery | Skeptical | "Another landing page? My marketing guy already built one on Unbounce two years ago." |
| Realization | Surprised | "Wait, it pulls from the same data as my website? So when we changed our hours last month, the landing page changed too?" |
| Activation | Relieved | "I don't have to tell anyone to update it. It just stays current." |
| Ongoing | Confident | "Every ad dollar goes to a page that has our real hours, our real team, our real reviews. No data drift." |

### For the Office Manager (Sarah)

| Stage | Emotion | Thought |
|---|---|---|
| Before | Overwhelmed | "I'm supposed to update the website AND the landing page AND Google AND Facebook every time something changes?" |
| Discovery | Cautious | "If I update hours in PatientEngage, it really updates everywhere? Including this landing page?" |
| Activation | Relieved | "One place. I update it once and everything stays in sync. I don't have to remember five different logins." |

### For the Marketing Person

| Stage | Emotion | Thought |
|---|---|---|
| Before | Frustrated | "I built a great landing page last year but the practice changed their hours and never told me. Now it shows wrong info." |
| Discovery | Interested | "The page pulls live data from the platform? So I don't have to chase down the practice for updated content?" |
| Activation | Confident | "I can focus on the ad strategy and trust that the landing page content is always current." |

---

## MODE 5: Marketing Translation

### The Core Narrative

**Problem:** Every practice spends money driving traffic somewhere. Most send it to their homepage, which is built for everyone and optimized for no one. The ones who build landing pages face a different problem: data drift. The landing page shows last year's hours, last year's team, last year's insurance list. The patient sees one thing on the ad, another on the landing page, and something else on Google. Trust evaporates. The click you paid for bounces.

**Solution:** A landing page that builds itself from the data you already maintain. Your hours, your team, your insurance plans, your reviews, your location details -- all pulled live from PatientEngage. When anything changes, the landing page reflects it. No extra updates. No extra logins. No data drift.

**The ease angle:** The practice doesn't build the landing page. They don't maintain it. They don't even think about it. They maintain their practice data in PatientEngage (which they're already doing), and the landing page stays current as a byproduct.

### Key Selling Points for the Marketing Page

1. **No data drift:** Hours, team, insurance, reviews all pull from the same source of truth. Update once, reflected everywhere.
2. **No setup burden:** The page assembles from existing PatientEngage data. No copywriting, no design, no content migration.
3. **No maintenance:** When practice data changes, the landing page changes. The office manager doesn't have to remember another login.
4. **Conversion-optimized:** Phone CTAs, Book Online buttons, scheduling integration, insurance proof, reviews -- all the elements that convert a searcher into a patient.
5. **Flexible scheduling:** Works with PatientEngage Scheduler, a contact form, or a third-party scheduler link.
6. **Professional credibility:** Team photos and bios, insurance logos, real patient reviews, amenity badges -- everything a first-time visitor needs to trust the practice.

### Potential Hero Lines

- "Every ad click deserves a page that's actually ready for it."
- "A landing page that stays current because your practice data already is."
- "Your hours changed last month. Did your landing page?"
- "Stop sending paid traffic to your homepage."

### Potential Stats

- [NEED FROM LENNY] Conversion rate improvement: landing page vs. homepage
- [NEED FROM LENNY] Number of practices using landing pages
- [NEED FROM LENNY] Average number of landing pages per practice
- [ESTIMATE] Landing pages convert 2-5x better than homepages for paid traffic (industry standard)
- [OBSERVED] 40+ insurance plans displayed with logos on the example page
- [OBSERVED] 9+ patient reviews in the testimonial carousel
- [OBSERVED] 12 amenity badges on the example page
- [OBSERVED] 10 services listed on the example page

---

## Content Source Map

| Landing Page Section | PatientEngage Data Source | Auto-Updates? |
|---|---|---|
| Practice name + tagline | Locations | Yes |
| Address + neighborhood | Locations | Yes |
| Google Map | Google integration | Yes |
| Hours (weekly + special) | Hours | Yes |
| Amenity badges | Google (accessibility) + Locations | Yes |
| About Us + services | About Us | Yes |
| Practice images | Image gallery | Yes |
| Doctor photos + bios | Our Team | Yes |
| Insurance logos | Insurance | Yes |
| Patient reviews | Testimonials | Yes |
| Scheduling widget | Scheduler / Form / Third-party link | Configured once |
| Phone number | Campaign tracking number | Configured once |
| Announcements | Announcements | Yes |
| Frames gallery | Frames | Yes |
| Contact lens brands | Contact Lenses | Yes |

---

## Provenance
- Landing page structure and all section content: [OBSERVED] from live page at seashorehouseoptical.com/default/book-eye-exam-today/2120/
- Content source sections (Announcements, About Us, Locations, Hours, Our Team, Insurance, Frames, Contact Lenses, Testimonials, Google): [PROVIDED] by stakeholder
- Scheduling flexibility (form or third-party scheduler link): [PROVIDED] by stakeholder
- PatientEngage admin UI for landing page configuration: NOT OBSERVED (session expired)
- SeaShore House (#1718) must NEVER appear in any public content
- All pricing references: [pricing redacted]
