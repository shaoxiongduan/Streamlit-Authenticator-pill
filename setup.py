import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-authenticatorpill",
    version="0.2.1",
    author="Shao Duan",
    author_email="shaoxiongduan@gmail.com",
    description="A secure authentication module to validate user credentials in a Streamlit application modified for own use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaoxiongduan/Streamlit-Authenticator-pill",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['Python', 'Streamlit', 'Authentication', 'Components'],
    python_requires=">=3.6",
    install_requires=[
        "PyJWT >=2.3.0",
        "bcrypt >= 3.1.7",
        "PyYAML >= 5.3.1",
        "streamlit >= 0.86",
        "extra-streamlit-components >= 0.1.55"
    ],
)
