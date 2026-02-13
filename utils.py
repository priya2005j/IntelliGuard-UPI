import pandas as pd

DB = "database.csv"

def load_db():
    return pd.read_csv(DB)

def save_db(df):
    df.to_csv(DB, index=False)

def check_number(number):

    df = load_db()

    result = df[df["phone_number"] == number]

    if result.empty:
        return None

    return result.iloc[0]

def classify_risk(score):

    if score < 20:
        return "SAFE ✅", "green"
    elif score < 50:
        return "SUSPICIOUS ⚠️", "orange"
    else:
        return "FRAUD 🚨", "red"


def report_number(number):

    df = load_db()

    if number in df["phone_number"].values:

        df.loc[df["phone_number"] == number, "reports"] += 1
        df.loc[df["phone_number"] == number, "risk_score"] += 5

    else:

        new_row = {
            "phone_number": number,
            "reports": 1,
            "fraud_tag": "User Reported",
            "risk_score": 5,
            "last_reported": pd.Timestamp.now()
        }

        df = pd.concat([df, pd.DataFrame([new_row])])

    save_db(df)
