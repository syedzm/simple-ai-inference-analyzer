from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Membaca fail CSV dan memulangkan data."""

    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(
            f"Fail tidak ditemui: {file_path}"
        )

    data = pd.read_csv(file_path)

    return data

def filter_data(data, threshold):
    """Menapis rekod berdasarkan nilai ambang keyakinan."""

    if not 0 <= threshold <= 1:
        raise ValueError(
            "Nilai confidence mesti antara 0 hingga 1."
        )

    filtered_data = data[
        data["confidence"] >= threshold
    ].copy()

    return filtered_data

def calculate_statistics(data, total_records):
    """Mengira statistik bagi data selepas tapisan."""

    return {
        "total_records": total_records,
        "accepted_records": len(data),
        "average_confidence": data["confidence"].mean(),
        "highest_confidence": data["confidence"].max(),
        "lowest_confidence": data["confidence"].min(),
        "average_inference_time": data["inference_time_ms"].mean(),
        "object_counts": data["object_class"].value_counts().to_dict()
    }

def create_bar_chart(data, output_path):
    """Menghasilkan carta bar jumlah pengesanan setiap kelas."""

    if data.empty:
        print("Carta tidak dihasilkan kerana tiada data.")
        return False

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    object_counts = data["object_class"].value_counts()

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        object_counts.index,
        object_counts.values,
        color=["#1565C0", "#2E7D32", "#F57C00", "#7B1FA2"]
    )

    plt.title("Jumlah Pengesanan Mengikut Kelas Objek")
    plt.xlabel("Kelas Objek")
    plt.ylabel("Jumlah Pengesanan")

    plt.bar_label(bars, padding=3)
    plt.ylim(0, object_counts.max() + 1)
    plt.yticks(range(int(object_counts.max()) + 2))
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_path, dpi=300)
    plt.close()

    return True