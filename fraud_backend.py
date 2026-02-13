import pandas as pd

DB = "database.csv"


def load_database():
    return pd.read_csv(DB)


def check_number(phone):

    df = load_database()

    result = df[df["phone_number"].astype(str) == str(phone)]

    if result.empty:
        return None

    return result.iloc[0]


def classify_risk(score):

    if score < 20:
        return "SAFE ✅"

    elif score < 50:
        return "SUSPICIOUS ⚠️"

    else:
        return "FRAUD 🚨"


def report_number(phone):

    df = load_database()

    if phone in df["phone_number"].astype(str).values:

        df.loc[df["phone_number"].astype(str) == phone, "reports"] += 1
        df.loc[df["phone_number"].astype(str) == phone, "risk_score"] += 5

    else:

        new_row = {
            "phone_number": phone,
            "reports": 1,
            "fraud_tag": "User Reported",
            "risk_score": 5,
            "last_reported": pd.Timestamp.now()
        }

        df = pd.concat([df, pd.DataFrame([new_row])])

    df.to_csv(DB, index=False)
