def generate_summary(filtered_df):
    summary = (
        filtered_df
        .groupby(["Provider ID", "Application ID"])
        .agg(Device_Count=("Device ID", "nunique"))
        .reset_index()
    )
    return summary
