import setuptools

with open("requirements.txt", encoding="utf-8-sig") as f:
    requirements = f.readlines()


def readme():
    with open("README.md", encoding="utf-8-sig") as f:
        README = f.read()
    return README


setuptools.setup(
    name="twitchrealtimehandler",
    version="0.1.0",
    author="aDrz",
    author_email="adrien.nouvellet@gmail.com",
    description="Package to handle real-time frames or audio segments from a twitch stream",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/adrz/twitch-realtime-handler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
)
