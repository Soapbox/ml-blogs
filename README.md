# Soapbox ML BLogs Service

Last updated on: October 16, 2020

## Overview
This is the main API for interacting with Soapbox's machine learning models. This documentation goes through setting up your local environment to deploying the entire application into production.

## Table of contents
- [Setup](#setup)
- [Run project checklist](#run-project-checklist)
- [Key Components](#key-components)
- [Adding a model and creating an endpoint](#adding-a-model-and-creating-an-endpoint)
- [Logging](#logging)
- [Creating custom exceptions](#creating-custom-exceptions)
- [Testing endpoints](#testing-endpoints)
- [Testing on an instance, inside Docker](#testing-on-an-instance-inside-docker)
- [References/Guides](#referencesguides)
- [FAQs](#faqs)

### Setup
To run the ML ecosystem follow this guide in the [ML repo](https://github.com/Soapbox/ml)

The command to run the API in isolation is:

```
docker build --tag ml-blogs .
docker run --rm --publish 8200:8500 ml-blogs
```

The endpoints can then be access through `127.0.0.1:8200`

### Run project checklist
Every pull request in this project needs to pass the following checks implemented:
1) Project linting
    - Any wrnings and errors will bae flagged as errors and will cause the CI system to fail.
    - Address linting issues as specified by the linter

2) Unit tests
    - All tests are found inside `test`. Ensure that when building new features that appropriate unit tests are added and all tests pass.
    - Note that as soon as a test case failure is detected the CI system will fail right away.

The shell script which runs these checks is in `utils/check_project.sh`. It is advised that this script is run everytime you work on any feature set
as this will be the source of truth for any linting errors or unit test failures in the CI system.

Lastly, a convenient script called `utils/run_test.sh` takes a single argument of the Python unit test file's path so it runs the test cases in it.

**Tip:** To run any command inside your Docker container quickly, run the following:
```
docker exec ml-blogs <command>
```

In this case, Docker will run `command` quickly and exit immediately. For example, replacing `<command>` with `./utils/check-project.sh` will run the linter and unit test. `./utils/check-project.sh --no-linter` will only run the unit test.

In addition, if you run the following command:
```
docker exec -it ml-blogs <command>
```

it will allow you to interact with the container itself. This is useful when debugging any issues.

### Key Components
//TODO:Update section after FASTAPI refactor

### Adding a model and creating an endpoint
//TODO:Update section after FASTAPI refactor

## Logging
//TODO: Update section after FASTAPI refactor

## Creating custom exceptions
To create a custom exception similar to `422 - UnprocessableEntity`, follow the example of `UnprocessableEntity`:
//TODO: Update section after FASTAPI refactor

## Running tests
//TODO: Update section after FASTAPI refactor

