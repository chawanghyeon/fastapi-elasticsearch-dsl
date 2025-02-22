from setuptools import setup, find_packages

setup(
    name="fastapi-elasticsearch-dsl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "elasticsearch",
        "python-dotenv",
        "sqlalchemy",
        "celery",
        "kafka-python",
        "redis",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A FastAPI project integrated with Elasticsearch DSL",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fastapi-elasticsearch-dsl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>3.11',
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',
        ],
    },
    # ...additional setup configurations...
)
