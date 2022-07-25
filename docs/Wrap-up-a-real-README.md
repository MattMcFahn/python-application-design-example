# A python package to perform IO and simple data transformations: data_manipulator


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linter: pylint](https://img.shields.io/badge/%20linter-pylint-%231674b1?style=flat)](https://github.com/PyCQA/pylint)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-commmit: enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)

The `data_manipulator` is a python package to **[Todo - detail]**.

Configuration of the package is handled via environment variables loaded into a
[Pydantic BaseSetting class](./data_manipulator/config.py).

The repo contains all associated docker and Github artefacts for a CI/CD workflow to build an image to be pushed to an
ECR registry.


## Dependencies

* [Pyenv](https://github.com/pyenv/pyenv) for base python versions, with `python 3.9.5` installed
* [Poetry](https://python-poetry.org/) for dependency management and packaging
* [Docker desktop](https://www.docker.com/products/docker-desktop/) for local development (_optional_)
* [GNU Make](https://www.gnu.org/software/make/) for ease and standardisation of common executables

### Getting started (setting up your environment)

Run the following in your terminal:
```bash
make setup
```

You can then run the following to enter a poetry shell for the environment you've created
```bash
make shell
```

## Local usage

Set necessary env variables for the package in a `.env` file in root of repo.
As a bare minimum, you'll need variables set as in the [`.test.env` file](../.test.env).

In particular, you'll need to set:
* TODO: List variables and explain the package

### Run main script

From your poetry shell, run the following:

```bash
python -m data_manipulator
```

### Run unit tests, linting, and formatting

From your poetry shell, run:
```bash
make checks
```

## Committing to the repo

At least check that the following hold:

* [x] Linting and formatting are correct
* [x] Test pack runs

See the `Run main script` and `Run unit tests, linting, and formatting` sections above to check these.

You may also want to check that:
 * [x] Docker build works and container can be ran (see annex)

### Annex I: Build and execute docker image locally

This is only necessary when changing the containerisation of the package.

We can build a docker image locally and run the entrypoint exposed with env vars passed from your `.env` file. This simulates the step-functions use of the application image.

Ensure your `Docker` daemon is running, then in the console, run:

```bash
make build
```

This will build an image on your local docker daemon with a `data_manipualtor` tag.

Now run:
```bash
make run
```

This will start a docker container from the image and execute the CMD entrypoint, passing through env variables set in
your `.env` file.

You can inspect the exit status of this image with:
```bash
docker ps -a
```
