# Step 4 : Resulting View: Google Reserve End-to-End Experience

## Patient Perspective (Observed on Simmons Eye Care - Little Rock)

### Google Search Experience [OBSERVED]
1. Patient searches "simmons eye care little rock ar" on Google
2. Google Business Profile knowledge panel appears on right side of results
3. Panel shows: Practice name, 4.9 stars (790 reviews), Eye care center category
4. Action buttons visible: Website, Directions, Reviews, Save, Share, Call, **Book online**
5. "Book online" button is a distinct action in the panel
6. Clicking "Book online" redirects via ngj.ai (Google's Reserve with Google relay) with rwg_token parameter

### Google Maps Experience [OBSERVED]
1. Patient searches for practice on Google Maps
2. Maps listing shows: Storefront photo, practice name, 4.9 stars (790 reviews)
3. Tabs: Overview, Reviews, About
4. Action icons: Directions, Save, Nearby, Send to phone, Share
5. **"Book online" button appears as a prominent light blue banner** below the action icons
6. The button has a calendar icon and "Book online" text
7. Below the button: address (11115 Hermitage Rd, Little Rock, AR 72211)

### Key UX Observations
- The "Book online" button is MORE prominent in Maps than in Search
- In Maps it gets its own full-width banner, making it impossible to miss
- In Search it appears as one of the action buttons in the knowledge panel
- The button appears on BOTH Search and Maps simultaneously
- The redirect goes through Google's own infrastructure (ngj.ai), creating a trusted experience

## Practice Perspective (Observed in PatientEngage Admin)

### Google Reserve Settings Page
- Simple toggle: On/Off
- Two booking type options observed: "PatientEngage Scheduler" or "3rd Party Booking Link"
- For 3rd Party Booking Link: practice enters any URL they want
- Last Synced date shows (Apr 7, 2026 for Simmons)
- Clicks chart shows daily Google Reserve click volume over time

### Scheduler Queue
- Appointments from Google Reserve flow into the same Scheduler queue
- Queue shows: Status (Pending/Confirmed), Patient name, Doctor, Appointment date/time, Date Received
- Practice can filter by status: Pending, Confirmed
- Active appointments showing real patient bookings

### Monthly Report
- Breaks down by month: New Patients, Returning Patients, Rejected Appts, Total
- Gives practice full visibility into scheduling volume trends
- Simmons Benton averaging ~200 appointments/month through the scheduler

## Before vs After

### Before Google Reserve
- Patient finds practice on Google
- Must click "Website" or "Call" to book
- Website click: Leave Google → navigate practice website → find booking page → fill form
- Call: Only during business hours, wait on hold, manual booking
- Minimum 3-4 extra steps between intent and booking

### After Google Reserve
- Patient finds practice on Google
- Clicks "Book online" directly from Search or Maps
- Immediately directed to booking page (PE Scheduler or practice's own page)
- Zero navigation friction
- Available 24/7, even when office is closed
- One button, one click from intent to booking

## Screenshots Needed for Marketing Page
1. ss_gr_01_google_search_panel.png : Google Search showing "Book online" in GBP knowledge panel
2. ss_gr_02_google_maps_button.png : Google Maps showing prominent "Book online" light blue banner
3. ss_gr_03_admin_toggle.png : PatientEngage Google Reserve settings with toggle ON
4. ss_gr_04_clicks_chart.png : Google Reserve Clicks chart showing growth trend
5. ss_gr_05_scheduler_queue.png : Scheduler queue showing appointments flowing in
6. ss_gr_06_monthly_report.png : Monthly report showing appointment volume
