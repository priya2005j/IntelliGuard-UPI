import pandas as pd
import random
from datetime import datetime, timedelta

numbers = []
reports = []
tags = []
risk_scores = []
last_reported = []

fraud_tags = [
    "Fake UPI Collect",
    "Loan Scam",
    "Lottery Scam",
    "KYC Fraud",
    "Impersonation",
    "Job Scam"
]

for i in range(1000):

    number = "9" + str(random.randint(100000000,999999999))

    report_count = random.randint(0, 20)

    if report_count > 7:
        tag = random.choice(fraud_tags)
    else:
        tag = "None"

    risk = min(report_count * 5, 100)

    date = datetime.now() - timedelta(days=random.randint(0, 30))

    numbers.append(number)
    reports.append(report_count)
    tags.append(tag)
    risk_scores.append(risk)
    last_reported.append(date)

df = pd.DataFrame({
    "phone_number": numbers,
    "reports": reports,
    "fraud_tag": tags,
    "risk_score": risk_scores,
    "last_reported": last_reported
})

df.to_csv("database.csv", index=False)

print("✅ Dataset created successfully!")
