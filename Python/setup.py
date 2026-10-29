from setuptools import setup

setup(
    name="PNWColors",
    version="0.1",
    py_modules=["PNWColors"],
    install_requires=["numpy", "matplotlib"],
    description="Color palettes inspired by the Pacific Northwest, adapted from the PNWColors R package https://github.com/jakelawlor/PNWColors",
    author="Annabel Wade",
    author_email="annawade@uw.edu",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

