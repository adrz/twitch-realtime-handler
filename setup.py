import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitchrealtimehandler", 
    version="0.0.1",
    author="aDrz",
    author_email="adrien.nouvellet@gmail.com",
    description="Handler for twitch video/audio in realtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrz/twitch-realtime-handler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=["numpy",
                      "streamlink"]
)
