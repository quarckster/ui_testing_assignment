# UI testing assignment

This repository contains the required files for implementing a few UI tests using Python and Selenium.

## Prerequisites

You will need [`docker`](https://docs.docker.com/get-docker/) and [`docker-compose`](https://docs.docker.com/compose/install/) installed. These packages are usually available via your package manager if you're using Linux. If you're using Fedora or have problems with cgroups, you can also substitute `docker` with [`podman`](https://podman.io/getting-started/installation) that is also compatible with [`docker-compose`](https://www.redhat.com/sysadmin/podman-docker-compose).

## Structure

The composed environment will start 3 containers:
* the `microblog` service that you should be testing
* the `selenium` backend that provides us the browser automation
* the `tests` container that will be used to execute the tests

## Usage

1. Clone the repo

```sh
git clone git@github.com:quarckster/ui_testing_assignment.git
```

2. Enter to the directory

```sh
cd ui_testing_assignment
```

3. Run the `docker-compose` file:

```sh
docker-compose up -d
```

4. Access the `microblog` service under [http://localhost:5000](http://localhost:5000) with your browser and familiarize yourself with it.

5. Execute the tests

```sh
docker-compose exec tests pytest tests.py
```

6. Implement the missing tests and make sure that they still pass
