from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("cdslic/version.py") as f:
    exec(f.read())

extra_setuptools_args = dict(
    tests_require=[
        # Other test dependencies
    ]
)
setup(
    name="cdslic",
    version=__version__,
    author="Yifan Wang",
    author_email="yifanwangzippo64@outlook.com",
    url="https://github.com/Nshuangpapa/cdslic",
    install_requires=requirements,
    package_data={"cdslic": ["resources/*"]},
    packages=find_packages(exclude=["cdslic/tests"]),
    license="MIT",
    description="cdslic",
    long_description="cdslic",
    keywords=["cd,slic"],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
    **extra_setuptools_args
)

