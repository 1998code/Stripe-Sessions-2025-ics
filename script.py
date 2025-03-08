from ics import Calendar, Event
from datetime import datetime
import pytz

# Create a new calendar
calendar = Calendar()

# Define the events
events = [
    {"name": "Payment operations training (add-on)", "start": "2025-05-06 08:30", "end": "2025-05-06 15:30", "description": "Pre-conference training"},
    {"name": "Billing implementation training (add-on)", "start": "2025-05-06 08:30", "end": "2025-05-06 15:30", "description": "Pre-conference training"},
    {"name": "Connect implementation training (add-on)", "start": "2025-05-06 08:30", "end": "2025-05-06 15:30", "description": "Pre-conference training"},
    {"name": "Opening keynote: The future of commerce", "start": "2025-05-06 16:00", "end": "2025-05-06 16:45", "description": "Main stage\nAll tracks"},
    {"name": "A conversation with Mark Zuckerberg", "start": "2025-05-06 16:45", "end": "2025-05-06 17:30", "description": "Main stage\nAll tracks"},
    {"name": "Sessions welcome reception", "start": "2025-05-06 17:30", "end": "2025-05-06 19:30", "description": "Meals and receptions"},
    {"name": "Product keynote", "start": "2025-05-07 09:00", "end": "2025-05-07 10:00", "description": "Main stage\nAll tracks"},
    {"name": "Developer keynote", "start": "2025-05-07 10:30", "end": "2025-05-07 11:00", "description": "Breakout\nDeveloper craft"},
    {"name": "How low-cost payments unlock high-growth economies", "start": "2025-05-07 10:30", "end": "2025-05-07 11:00", "description": "Breakout\nPayments landscape"},
    {"name": "The intersection of hospitality, AI, and the modern guest", "start": "2025-05-07 10:30", "end": "2025-05-07 11:00", "description": "Breakout\nFrictionless flows"},
    {"name": "Developer tutorial 1", "start": "2025-05-07 11:15", "end": "2025-05-07 11:45", "description": "Breakout\nDeveloper craft"},
    {"name": "Link: The consumer network built by all of us", "start": "2025-05-07 11:15", "end": "2025-05-07 11:45", "description": "Breakout\nPayments landscape"},
    {"name": "Lunch at Yerba Buena Gardens", "start": "2025-05-07 11:45", "end": "2025-05-07 13:30", "description": "Meals and receptions"},
    {"name": "Developer tutorial 2", "start": "2025-05-07 12:00", "end": "2025-05-07 12:30", "description": "Breakout\nDeveloper craft"},
    {"name": "AI agents: Reshaping the way we buy and sell", "start": "2025-05-07 12:00", "end": "2025-05-07 12:30", "description": "Breakout\nPayments landscape"},
    {"name": "Breakout session with Klarna", "start": "2025-05-07 12:00", "end": "2025-05-07 12:30", "description": "Breakout\nPartner-led\nEmerging trends"},
    {"name": "The roadmap for easier global money movement", "start": "2025-05-07 12:00", "end": "2025-05-07 12:30", "description": "Breakout\nFrictionless flows"},
    {"name": "Developer tutorial 3", "start": "2025-05-07 13:45", "end": "2025-05-07 14:15", "description": "Breakout\nDeveloper craft"},
    {"name": "Breakout session with Visa", "start": "2025-05-07 13:45", "end": "2025-05-07 14:15", "description": "Breakout\nPartner-led\nPayments landscape"},
    {"name": "Breakout session with Amazon Pay", "start": "2025-05-07 13:45", "end": "2025-05-07 14:15", "description": "Breakout\nPartner-led\nEmerging trends"},
    {"name": "Breakout session with FreedomPay", "start": "2025-05-07 14:00", "end": "2025-05-07 14:30", "description": "Breakout\nPartner-led\nFrictionless flows"},
    {"name": "Antithesis: Testing 2.0", "start": "2025-05-07 14:30", "end": "2025-05-07 15:00", "description": "Breakout\nDeveloper craft"},
    {"name": "Unified experiences: Online, in-store, and everywhere in between", "start": "2025-05-07 14:30", "end": "2025-05-07 15:00", "description": "Breakout\nPayments landscape"},
    {"name": "Breakout session with Verifone", "start": "2025-05-07 14:30", "end": "2025-05-07 15:00", "description": "Breakout\nPartner-led\nEmerging trends"},
    {"name": "Breakout session with Clerk", "start": "2025-05-07 14:45", "end": "2025-05-07 15:15", "description": "Breakout\nPartner-led\nFrictionless flows"},
    {"name": "Beyond the buy button: Wayfair’s omnichannel journey", "start": "2025-05-07 15:15", "end": "2025-05-07 15:45", "description": "Breakout\nPayments landscape"},
    {"name": "A conversation with Sir Jony Ive KBE", "start": "2025-05-07 16:00", "end": "2025-05-07 17:00", "description": "Main stage\nAll tracks"},
    {"name": "Celebration in expo hall", "start": "2025-05-07 17:00", "end": "2025-05-07 19:00", "description": "Meals and receptions"},
    {"name": "AMA with Patrick and John Collison", "start": "2025-05-08 09:00", "end": "2025-05-08 10:00", "description": "Main stage\nAll tracks"},
    {"name": "Product roadmap: Payments", "start": "2025-05-08 10:30", "end": "2025-05-08 11:00", "description": "Breakout\nPayments landscape"},
    {"name": "The science behind successful pricing strategies", "start": "2025-05-08 10:30", "end": "2025-05-08 11:00", "description": "Breakout\nRevenue agility"},
    {"name": "Platforms keynote", "start": "2025-05-08 10:30", "end": "2025-05-08 11:00", "description": "Breakout\nSaaS platform economy"},
    {"name": "How Chubb and USAA are underwriting the next chapter of insurance", "start": "2025-05-08 10:30", "end": "2025-05-08 11:00", "description": "Breakout\nFrictionless flows"},
    {"name": "Auth, fraud, and costs: Using AI to find equilibrium", "start": "2025-05-08 11:15", "end": "2025-05-08 11:45", "description": "Breakout\nPayments landscape"},
    {"name": "Product roadmap: Revenue (Billing, Tax, and Data)", "start": "2025-05-08 11:15", "end": "2025-05-08 11:45", "description": "Breakout\nRevenue agility"},
    {"name": "Scaling vertical SaaS: From $1 to $1B processed", "start": "2025-05-08 11:15", "end": "2025-05-08 11:45", "description": "Breakout\nSaaS platform economy"},
    {"name": "Breakout session with Amex", "start": "2025-05-08 11:15", "end": "2025-05-08 11:45", "description": "Breakout\nPartner-led\nFrictionless flows"},
    {"name": "Lunch at Yerba Buena Gardens", "start": "2025-05-08 11:45", "end": "2025-05-08 13:30", "description": "Meals and receptions"},
    {"name": "Breakout session with Mastercard", "start": "2025-05-08 12:00", "end": "2025-05-08 12:30", "description": "Breakout\nPartner-led\nPayments landscape"},
    {"name": "Show me the money: Media’s new revenue possibilities", "start": "2025-05-08 12:00", "end": "2025-05-08 12:30", "description": "Breakout\nFrictionless flows"},
    {"name": "Your platform is evolving. Is your risk strategy?", "start": "2025-05-08 12:00", "end": "2025-05-08 12:30", "description": "Breakout\nSaaS platform economy"},
    {"name": "Decoding tax compliance and finding opportunities", "start": "2025-05-08 13:45", "end": "2025-05-08 14:15", "description": "Breakout\nRevenue agility"},
    {"name": "Mastering embedded finance: Platform strategies that work", "start": "2025-05-08 13:45", "end": "2025-05-08 14:15", "description": "Breakout\nSaaS platform economy"},
    {"name": "Why your business can’t afford to ignore stablecoins", "start": "2025-05-08 14:45", "end": "2025-05-08 15:15", "description": "Breakout\nPayments landscape"},
]

# Define the timezone for San Francisco
sf_tz = pytz.timezone('America/Los_Angeles')

# Add events to the calendar
for event in events:
    e = Event()
    e.name = event["name"]
    e.begin = sf_tz.localize(datetime.strptime(event["start"], "%Y-%m-%d %H:%M"))
    e.end = sf_tz.localize(datetime.strptime(event["end"], "%Y-%m-%d %H:%M"))
    e.description = event["description"]
    calendar.events.add(e)

# Save the calendar to a file
with open('conference_schedule.ics', 'w') as f:
    f.writelines(calendar)
