# Screenshot Brief: Recalls & Reminders

## Priority Order and Setup Instructions

### Shot 1 (HERO): ss_rr_01_metrics_dashboard.png
**What:** Recalls & Reminders Metrics dashboard showing Performance card with monthly data
**Priority:** HIGHEST — this is the hero image
**Setup:**
1. Navigate to https://app.patientengage.ai/a/recall-reminders/metrics
2. Set date range to full month (e.g., Feb 28 - Mar 30, 2026)
3. Set filter to "All Groups"
4. Capture the Performance card showing: Messages Delivered (28,862 / 76%), Recall Booked (431 / 8%), Appt Confirmed (5,209 / 59%), Appt Rescheduled (821 / 9%)
5. Include the summary bar above: "23 Practices, 0 Locations, 15,056 Patients, 37,862 Messages"
**Crop:** Performance card with summary bar, no sidebar
**Frame:** Browser chrome frame (red/yellow/green dots) per Style B
**Notes:** The 5,209 Confirmed and 431 Rebooked numbers are the stars. The summary bar shows scale.

### Shot 2: ss_rr_02_recall_types.png
**What:** Recalls & Reminders setup page showing all 6 recall types with toggles
**Priority:** HIGH — shows the breadth of the system
**Setup:**
1. Navigate to https://app.patientengage.ai/a/recall-reminders
2. Capture the full table showing: Exam Recall (18), Manual Recall (19), No Show Recall (23), Appointment Reminder (7), Pre-Appointment Information (12), Order Pickup (11)
3. All toggles should be ON (green/teal)
4. Show the Messages column with SMS/Call/Email counts
**Crop:** Full table from header through all 6 rows
**Frame:** Browser chrome frame
**Notes:** This screenshot sells the "6 recall types covering the full lifecycle" message. The active practice counts show adoption.

### Shot 3: ss_rr_03_exam_recall_template.png
**What:** Exam Recall Template showing the multi-touch sequence
**Priority:** HIGH — demonstrates the depth of the sequencing
**Setup:**
1. Navigate to Exam Recall template (recall-reminders/1)
2. Show all 4 messages: Email 10mo, SMS 12mo, Robocall 14mo, Email 14mo
3. Each message should show Schedule, During, and Channel fields
**Crop:** Full message list from top to bottom
**Frame:** Browser chrome frame
**Notes:** This shows the 4-touch, 4-month escalation. The channel variety (Email → SMS → Call → Email) is the story.

### Shot 4: ss_rr_04_appointment_reminder_template.png
**What:** Appointment Reminder Template showing the 6-touch countdown
**Priority:** MEDIUM-HIGH — shows the reminder depth
**Setup:**
1. Navigate to Appointment Reminder template (recall-reminders/2)
2. Show all messages: 7 days, 4 days, 25hrs, 24hrs, 23hrs, 2hrs before
3. Each with channel and timing details
**Crop:** Full message list
**Frame:** Browser chrome frame
**Notes:** The countdown from 7 days to 2 hours is visually compelling. Shows intelligent channel alternation.

### Shot 5: ss_rr_05_message_log.png
**What:** Metrics page message log showing individual patient messages with status
**Priority:** MEDIUM — shows real activity
**Setup:**
1. Navigate to recall-reminders/metrics
2. Scroll to the message log table below the Performance cards
3. Show 5-8 rows with Practice, Patient Name, Appointment Date, Template, Message Name, Channel, Status columns
**Crop:** Table header + 5-8 data rows
**Frame:** Browser chrome frame
**Notes:** CRITICAL: Blur or redact all patient names. Never show real patient data in marketing. Show diverse templates (Order Pickup, Appointment Reminder, Exam Recall) and channels (SMS, Email) with green "Sent" checkmarks.

### Shot 6: ss_rr_06_alerts_card.png
**What:** Alerts card showing DNC, No Contact Info, Error counts
**Priority:** LOW-MEDIUM — supporting evidence for data quality discussion
**Setup:**
1. Same metrics page, capture the Alerts card
2. Show: Do Not Contact (513/1%), No Contact Info (7,712/20%), Error (77/0%), Too Close (693/3%), Appt Canceled (789/9%), Voicemails (2,560/59%)
**Crop:** Alerts card only
**Frame:** Browser chrome frame
**Notes:** The 1% DNC rate proves patients don't view messages as spam. The 59% Voicemail rate proves why SMS > phone calls. The 0% Error rate shows reliability.

## General Screenshot Rules
- All paths must be ABSOLUTE: /reminders/screenshots/ss_rr_XX_description.png
- Browser chrome frame on all screenshots (red/yellow/green dots)
- Blur patient names and any PII
- Anonymize practice names unless explicit written permission exists
- Match Style B design system for any annotations or overlays
- For the existing mockup screenshots (ss_recalls-reminders_1-4.jpg), continue using those as supplementary visuals until real screenshots are captured
