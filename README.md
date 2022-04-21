# UI testing assignment

This repository contains required files for developing simple UI tests using Python and Selenium.

## Prerequisites

You should have installed `docker` and `docker-compose` for work.

## Usage

1. Clone the repo

```sh
git clone git@github.com:quarckster/ui_testing_assignment.git
```

2. Change the directory

```sh
cd ui_testing_assignment
```

3. Run `docker-compose` file:

```sh
docker-compose up
```

4. Switch to `ui_testing_assignment_tests_1` container shell

```sh
docker exec -it ui_testing_assignment_tests_1 bash
```

5. Execute the tests

```sh
pytest tests.py
```
