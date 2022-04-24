from setuptools import find_packages, setup
from pathlib import Path

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
	name="yahoo_fin_api",
	# packages=find_packages(include=["yahoo_api"], exclude=("tests",)),
	keywords="yahoo financials trading api",
	packages=["yahoo_fin_api", "yahoo_fin_api.models"],
	version="0.0.15",
	description="Pyhton Yahoo Financials SDK",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/MihaiBlebea/yahoo-fin-api",
	author="Mihai Blebea",
	author_email="mihaiserban.blebea@gmail.com",
	license="MIT",
	install_requires=["requests"],
	setup_requires=["pytest-runner"],
	tests_require=["pytest==4.4.1"],
	test_suite="tests",
)