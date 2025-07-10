import os
import pandas as pd

def export_provider_files(filtered_df, providers_df, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    provider_ids = providers_df['Provider ID'].dropna().unique()

    for provider_id in provider_ids:
        provider_name = f"Provider_{provider_id}".replace('/', '_').replace('\\', '_')
        provider_data = filtered_df[filtered_df['Provider ID'] == provider_id]

        # Create Excel writer
        writer = pd.ExcelWriter(f"{output_dir}/{provider_name}.xlsx", engine='xlsxwriter')

        # Even if empty, write the expected column structure
        if provider_data.empty:
            empty_df = filtered_df.head(0)  # Just column headers
            empty_df.to_excel(writer, sheet_name='No Data for Two Months', index=False)
        else:
            provider_data.to_excel(writer, sheet_name='No Data for Two Months', index=False)

        writer.close()
