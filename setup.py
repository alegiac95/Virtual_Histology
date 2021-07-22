import setuptools


def read_long_description():
    with open("README.rst", "r") as f:
        return f.read()


setuptools.setup(
    name="imaging-transcriptomics",
    version="0.1",
    author="Daniel Martins, MD, PhD; Alessio Giacomel",
    author_email=["daniel.martins@kcl.ac.uk", "alessio.giacomel@kcl.ac.uk"],
    description="Perform imaging-transcriptomics analysis on a neuroimaging scan.",
    long_description=read_long_description(),
    classifiers=["Intended Audience :: Healthcare Industry",
                 "Intended Audience :: Science/Research",
                 "Topic :: Scientific/Engineering :: Image Processing",
                 "Topic :: Scientific/Engineering :: Medical Sciences App", "Development Status :: 4 - Beta",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.6",
                 "License :: OSI Approved :: MIT License"
                 ],
    keywords="image analysis, neuroimaging, imaging transcriptomics, medical image, research, multimodal imaging",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["imaging-transcriptomics = Imaging_Transcriptomics.imaging_transctiptomics.transcriptomics:main"]})
