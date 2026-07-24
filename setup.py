"""Setup script for noHXW (backward-compatible with older pip)."""
from setuptools import setup, find_packages

setup(
    name="noHXW",
    version="1.0.0",
    description="noHXW — No Hardware, No Problem. Distributed Infrastructure Simulation Engine",
    packages=find_packages(include=["app", "app.*"]),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "python-multipart>=0.0.6",
    ],
    entry_points={
        "console_scripts": [
            "noxhw=app.main:start",
        ],
    },
)
