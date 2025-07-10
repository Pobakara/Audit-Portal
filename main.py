from analysis.loader import load_inputs
from analysis.full_analysis import run_analysis
from analysis.nodata_export import export_provider_files
from analysis.summary_builder import generate_summary

def main():
    # Load all sheets
    month1, month2, malfunc, providers = load_inputs("data")

    # Run core analysis
    filtered = run_analysis(month1, month2, malfunc)

    # Export per-provider Excel files
    export_provider_files(filtered, providers, output_dir="output")

    # Generate summary table
    summary = generate_summary(filtered)
    summary.to_excel("output/Device_Summary.xlsx", index=False)

    print("🎉 Analysis complete! Files saved to /output")

if __name__ == "__main__":
    main()
