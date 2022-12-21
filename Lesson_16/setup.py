from setuptools import setup, find_packages
import pathlib
from os import path

HERE = pathlib.Path(__file__).parent.resolve()
long_description = (HERE / "README.md").read_text(encoding="utf-8")
with open(path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")
install_requires = [x.strip() for x in all_reqs]
setup(
    name="chernov_anekdot_parser",
    version="0.1",
    description="The script displays one random anecdote from the site anekdot.ru",
    url="http://github.com/<account>/<repo>",
    author="Anatoliy Chernov ",
    author_email="chernov_anatoliy@tut.by",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    #packages=anekdot(),
    python_requires=">=3.9, <4",
    install_requires=install_requires,
    zip_safe=False,
)
