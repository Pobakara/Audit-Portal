import pandas as pd
from datetime import datetime, timedelta

def classify_status(row):
    if pd.isna(row["Date Commenced"]):
        return "Not Reported"
    elif pd.notna(row["Date Commenced"]) and pd.isna(row["Date Resolved"]):
        return "Unresolved"
    elif pd.notna(row["Date Resolved"]):
        # Consider "Resolved > 3 Months Ago"
        cutoff = datetime.now() - timedelta(days=90)
        if row["Date Resolved"] < cutoff:
            return "Resolved >3 Months Ago"
    return "Resolved Recently"

def run_analysis(month1, month2, malfunc):
    # STEP 1: Inner join on Device ID and Provider ID (SP Code)
    common = pd.merge(
        month1,
        month2,
        on=["Device ID", "Provider ID"],
        suffixes=("_M1", "_M2"),
        how="inner"
    )
    print("🔍 Columns in filtered_df:", selected.columns.tolist())

    # STEP 2: Left join with Malfunctions data
    enriched = pd.merge(
        common,
        malfunc,
        how="left",
        left_on=["Device ID", "Provider ID"],
        right_on=["IVU ID", "SP Code"]
    )

    # STEP 3: Select final fields for export
    selected = enriched[
        [col for col in enriched.columns if col.endswith("_M2")] +
        ["Identifier", "Date Commenced", "Date Resolved", "Description"]
    ].copy()

    # STEP 4: Rename month2 columns back to normal
    selected.columns = [col.replace("_M2", "") for col in selected.columns]

    # STEP 5: Add status classification
    selected["Malfunction Status"] = selected.apply(classify_status, axis=1)

    return selected
