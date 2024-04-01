from setuptools import setup, find_packages

setup(
    name="linktransformer",
    version="0.1.13-a",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "scikit-learn",
        "faiss-cpu",
        "networkx",
        "torch",
        "sentence_transformers",
        "transformers",
        "wandb",
        "numpy",
        "pandas",
        "openai",
        "openpyxl",
        "datasets",
        "accelerate",
        "evaluate"
    ],
    python_requires=">=3.8",
    author="original auth: Abhishek Arora and Melissa Dell",
    author_email="linktransformer23@gmail.com",
    description="A friendly way to do link, aggregate, cluster and de-duplicate dataframes using large language models.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    license_files=("LICENSE",),
    url="https://github.com/dell-research-harvard/linktransformer",
    include_package_data=True,
    # Pytest configurations can be set up separately, often in a pytest.ini file or
    # by integrating within setup.cfg or pyproject.toml. It's not directly
    # translatable into setup.py but can be managed with extra configurations.
)

