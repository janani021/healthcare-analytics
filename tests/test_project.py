from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

def test_required_files_exist():
    required_paths = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "data_analytics" / "data_quality_gold.ipynb",
    ]

    missing = [str(p) for p in required_paths if not p.exists()]
    assert not missing, f"Missing files: {missing}"
