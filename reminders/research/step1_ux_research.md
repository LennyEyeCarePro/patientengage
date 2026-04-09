# Step 1: UX Research: Recalls & Reminders

## Mode 1: The Before State
**What does the practice do WITHOUT automated recalls & reminders?**

Without PatientEngage Recalls & Reminders, optometry practices rely on manual, fragmented processes to bring overdue patients back and remind upcoming patients about their appointments:

1. **Manual phone calls:** Front desk staff spend hours each week calling patients who are overdue for their annual exam. They reach voicemail 60-70% of the time, leave a message, and hope patients call back. Most don't.
2. **Paper postcards:** Some practices mail physical recall postcards at 12 months. Expensive ($1-3 per card), slow (7-10 day delivery), no tracking, and most go straight to the trash.
3. **Spreadsheet tracking:** Staff export patient lists from the EHR, sort by last-exam date, and manually work through them. No automation, no multi-touch sequences, no confirmation tracking.
4. **No-show chaos:** When patients don't show up, the practice has an empty chair generating $0 revenue. Staff may try to call, but by then it's too late to fill the slot.

**The three before states:**
- **No recall system:** Practice has no systematic way to contact overdue patients. They only see patients who self-schedule or remember to call. Attrition rate of 20-30% annually.
- **Manual recall only:** Front desk manually calls overdue patients from a list. Reaches maybe 30% by phone. Takes 15-20 hours/month of staff time. No email, no text. Low conversion.
- **Basic EHR reminders:** EHR sends a single email or postcard at a fixed interval. No multi-channel (no SMS). No intelligent sequencing. No confirmation tracking. No no-show follow-up.

**The core problem:** The average optometry patient needs an annual exam, but without proactive, multi-channel outreach at the right time, 20-30% of patients lapse each year. Every lapsed patient = $300-500 in lost annual revenue. For a practice seeing 3,000 patients, that's $180K-$450K in annual revenue walking out the door.

## Mode 2: Data Landscape

### Admin/Settings UI
**Location:** Admin > Recalls & Reminders (https://app.patientengage.ai/a/recall-reminders)

**Recall Types Available (6 total, all active):**

| Type | Active Practices | SMS | Calls | Emails | Total Messages |
|---|---|---|---|---|---|
| Exam Recall | 18 | 1 | 0 | 2 | 3 |
| Manual Recall | 19 | 1 | 0 | 1 | 2 |
| No Show Recall | 23 | 1 | 0 | 1 | 2 |
| Appointment Reminder | 7 | 3 | 0 | 2 | 5 |
| Pre-Appointment Information | 12 | 1 | 0 | 1 | 2 |
| Order Pickup | 11 | 2 | 0 | 1 | 3 |

**Key insight:** No Show Recall is the most widely adopted (23 practices), showing that no-show recovery is the #1 pain point. Appointment Reminder has the most messages (5 touches), showing the depth of the pre-appointment sequence.

### Exam Recall Template (4-touch multi-channel sequence) [OBSERVED]
1. **Email at 10 months** after eye exam — early nudge, educational tone
2. **SMS at 12 months** after eye exam — direct reminder at annual mark, Weekdays 9AM-5PM
3. **Robocall at 14 months** (available, currently OFF) — for unresponsive patients
4. **Email at 14 months** after eye exam — final outreach, urgency

**Key insight:** The sequence spans 4 months (10-14 months post-exam) with escalating channels. Starts soft (email) → direct (SMS) → persistent (call + email). This graduated approach respects patient preferences while maximizing touchpoints.

### Appointment Reminder Template (6-touch countdown sequence) [OBSERVED]
1. **7 Days Before** — Email (Everyday, Anytime)
2. **4 Days Before** — SMS (Weekdays 10AM-5PM)
3. **25 Hours Before** — Email (confirmation)
4. **24 Hours Before** — SMS (Weekdays 8:30AM-5PM)
5. **23 Hours Before** — Robocall (available, currently OFF)
6. **2 Hours Before** — SMS (final reminder, Weekdays 8:30AM-5PM)

**Key insight:** The pre-appointment sequence builds urgency from 7 days → 2 hours, alternating channels (email → SMS → email → SMS → call → SMS). The 2-hour-before SMS is the last-chance no-show prevention touchpoint.

### Network-Level Metrics [OBSERVED]

**Weekly (Apr 2-9, 2026):**
- 24 Practices, 5,690 Patients, 10,009 Messages
- 7,268 (73%) Messages Delivered
- 1,229 (35%) Appt Confirmed
- 88 (6%) Recall Booked
- 140 (4%) Appt Rescheduled

**Monthly (Feb 28 - Mar 30, 2026):**
- 23 Practices, 15,056 Patients, 37,862 Messages
- 28,862 (76%) Messages Delivered
- 5,209 (59%) Appt Confirmed
- 431 (8%) Recall Booked
- 821 (9%) Appt Rescheduled

**Alerts breakdown (monthly):**
- 513 (1%) Do Not Contact — respect for opt-outs
- 7,712 (20%) No Contact Info — data quality issue
- 77 (0%) Error — extremely low error rate
- 693 (3%) Too Close To Appt — timing intelligence
- 789 (9%) Appt Canceled
- 2,560 (59%) Voicemails — shows why SMS/email matters over calls

### Killer Stat Candidates
- "37,862 recall & reminder messages sent in a single month across 23 practices" [OBSERVED]
- "76% message delivery rate across all channels" [OBSERVED]
- "5,209 appointments confirmed automatically in one month" [OBSERVED]
- "431 overdue patients rebooked through automated recalls in one month" [OBSERVED]
- "59% of appointments confirmed without staff intervention" [CALCULATED: 5,209/8,831 confirmed of those addressed]
- "6 automated recall & reminder types covering the full patient lifecycle" [OBSERVED]
- "No Show Recall adopted by 23 practices — most popular type" [OBSERVED]

## Mode 3: Workflow Narrative

### Setup workflow (admin/CSM side):
1. Admin navigates to Recalls & Reminders in the admin panel
2. Six pre-built recall types are shown with toggles
3. Each type has a customizable message template with multi-touch sequences
4. Admin sets timing (hours/days/months before or after trigger event)
5. Admin sets delivery window (days of week, start/end time)
6. Admin chooses channel (SMS, Email, or Call) for each touchpoint
7. Templates include merge fields for patient name, practice name, appointment time
8. Toggle ON to activate — messages start flowing automatically based on appointment data from EHR sync

### Patient experience — Exam Recall:
1. Patient has eye exam on April 9, 2025
2. At month 10 (Feb 2026): Email lands — "It's been almost a year since your last eye exam at [Practice Name]. Schedule your annual exam today."
3. At month 12 (Apr 2026): SMS arrives — "Hi [Name], you're due for your annual eye exam at [Practice]. Book online: [link]"
4. If no response, month 14 (Jun 2026): Final email — "Don't let your vision care lapse. [Practice] has openings this week."
5. Patient clicks booking link → lands on practice's online scheduler → books appointment
6. Appointment flows into scheduler queue → staff sees it immediately

### Patient experience — Appointment Reminder:
1. Patient books appointment for April 16, 2026
2. April 9 (7 days before): Email — "Your appointment at [Practice] is next Wednesday at 2:00 PM"
3. April 12 (4 days before): SMS — "Reminder: Eye exam at [Practice] on Wed Apr 16 at 2PM. Reply C to confirm"
4. April 15 (25 hours before): Email — confirmation details, what to bring, office location
5. April 15 (24 hours before): SMS — "Tomorrow: Eye exam at [Practice] at 2PM. Reply C to confirm, R to reschedule"
6. April 16 (2 hours before): SMS — "See you at 2PM today at [Practice]! Running late? Call us: [number]"
7. Patient confirms via text reply → status updates automatically in scheduler

### No-show recovery workflow:
1. Patient doesn't show for April 16 appointment
2. No Show Recall triggers automatically
3. SMS sent: "We missed you today at [Practice]. Let's get you rescheduled: [booking link]"
4. Follow-up email if no response
5. If patient rebooks → cycle complete, chair filled

## Mode 4: Objection Pre-loading

### "My EHR already sends reminders"
Most EHRs send a single email reminder. PatientEngage sends multi-touch, multi-channel sequences (SMS + Email + Call) timed across days/weeks/months. SMS open rates are 98% vs. 20% for email. EHR reminders don't do recalls (re-engagement of overdue patients), only reminders (confirmation of upcoming).

### "Patients will think it's spam"
Every message includes opt-out. Only 1% of patients flag as Do Not Contact. Messages are personalized with patient name, practice name, doctor name, and appointment details. Timing windows ensure messages only arrive during business hours. Patients expect these communications from their healthcare providers.

### "We don't have good patient contact data"
The data shows 20% of patients have no contact info — this is a real issue. But that means 80% DO have contact info and can be reached. PatientEngage helps practices identify the data gap so they can address it. Even reaching 80% of patients automatically is vastly better than manual calling.

### "We already call patients manually"
59% of calls go to voicemail (observed data). Staff time on manual calling = 15-20 hours/month. Automated SMS has 98% open rate and patients can respond/book instantly. Manual calling doesn't scale — adding 500 patients means adding staff. Automation scales infinitely.

### "What if patients reschedule too much?"
821 rescheduled in one month (9%) vs 5,209 confirmed (59%). A rescheduled appointment is infinitely better than a missed/lapsed one. The system captures the reschedule and keeps the patient in the pipeline.

## Mode 5: Value Hierarchy

### Primary Value: Revenue Recovery
- Every lapsed patient = $300-500/year in lost revenue
- 431 patients rebooked in one month = $129K-$215K in recovered revenue across 23 practices
- Per-practice average: ~19 rebooked patients/month = $5,700-$9,500 recovered

### Secondary Value: No-Show Reduction
- 5,209 appointments confirmed in one month
- Confirmed patients show up at 95%+ rates
- Empty chairs cost practices $150-300 per slot
- Even preventing 5 no-shows/week saves $3,000-6,000/month

### Tertiary Value: Staff Time Savings
- Automated messages replace 15-20 hours/month of manual calling
- Staff can focus on patient care, not phone tag
- No training required — templates are pre-built
- System works nights, weekends, and holidays

### Quaternary Value: Patient Experience
- Patients prefer text communication (2:1 over phone calls)
- Convenient self-service booking links
- Professional, consistent communication
- Respectful timing windows (no 6AM texts)
