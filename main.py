from pathlib import Path
import pandas as pd

from analysis import (
    load_data,
    filter_data,
    calculate_statistics,
    create_bar_chart
)


BASE_DIRECTORY = Path(__file__).resolve().parent
DATA_FILE = BASE_DIRECTORY / "data" / "inference_data.csv"
OUTPUT_DIRECTORY = BASE_DIRECTORY / "output"


def get_threshold():
    """Meminta nilai ambang yang sah daripada pengguna."""

    while True:
        try:
            threshold = float(
                input("Masukkan nilai confidence antara 0 hingga 1: ")
            )

            if 0 <= threshold <= 1:
                return threshold

            print("Ralat: Nilai confidence mesti antara 0 hingga 1.")

        except ValueError:
            print("Ralat: Sila masukkan nombor yang sah.")

def display_results(statistics, threshold):
    """Memaparkan keputusan analisis dengan kemas."""

    print("\n========================================")
    print("ANALISIS DATA INFERENS AI")
    print("========================================")

    print(f"Nilai ambang              : {threshold:.2f}")
    print(f"Jumlah keseluruhan rekod   : {statistics['total_records']}")
    print(f"Jumlah pengesanan diterima : {statistics['accepted_records']}")

    if statistics["accepted_records"] == 0:
        print("Tiada objek melepasi nilai ambang.")
        return

    print(f"Purata confidence         : {statistics['average_confidence']:.2f}")
    print(f"Confidence tertinggi      : {statistics['highest_confidence']:.2f}")
    print(f"Confidence terendah       : {statistics['lowest_confidence']:.2f}")
    print(f"Purata masa inferens      : {statistics['average_inference_time']:.2f} ms")

    print("\nJUMLAH OBJEK")
    print("----------------------------------------")

    for object_class, total in statistics["object_counts"].items():
        print(f"{object_class:<12}: {total}")

    print("========================================")

def main():
    """Mengawal perjalanan utama program."""

    try:
        data = load_data(DATA_FILE)

        print("\nLIMA REKOD PERTAMA")
        print(data.head().to_string(index=False))

        threshold = get_threshold()
        filtered_data = filter_data(data, threshold)

        print("\nREKOD SELEPAS TAPISAN")

        if filtered_data.empty:
            print("Tiada rekod melepasi nilai ambang.")
        else:
            print(filtered_data.to_string(index=False))

        statistics = calculate_statistics(
            filtered_data, len(data)
        )

        display_results(statistics, threshold)

        OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

        filtered_file = OUTPUT_DIRECTORY / "filtered_data.csv"
        filtered_data.to_csv(filtered_file, index=False)

        print(f"\nData ditapis disimpan di: {filtered_file}")

        chart_file = OUTPUT_DIRECTORY / "object_count.png"

        # Buang graf lama supaya tidak memaparkan keputusan terdahulu.
        if chart_file.exists():
            chart_file.unlink()

        chart_created = create_bar_chart(
            filtered_data, chart_file
        )

        if chart_created:
            print(f"Graf disimpan di: {chart_file}")

        print("\nProgram berjaya dilaksanakan.")

    except (OSError, ValueError, pd.errors.ParserError) as error:
        print(f"\nRalat: {error}")


if __name__ == "__main__":
    main()