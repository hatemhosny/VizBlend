from setuptools import setup, find_packages

setup(
    name="VizBlend",
    version="4.0.0b1",
    author="Mahmoud Housam",
    author_email="mahmoudhousam60@gmail.com",
    description="A Python package to generate HTML reports from Plotly figures using Jinja2 templates.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MahmoudHousam/VizBlend",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["plotly>=4.0", "Jinja2>=3.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.7",
)
