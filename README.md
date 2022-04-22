# UI testing assignment

This repository contains the required files for implementing a few UI tests using Python and Selenium.

## Prerequisites

You will need [`docker`](https://docs.docker.com/get-docker/) and [`docker-compose`](https://docs.docker.com/compose/install/) installed. These packages are usually available via your package manager if you're using Linux. If you're using Fedora or have problems with cgroups, you can also substitute `docker` with [`podman`](https://podman.io/getting-started/installation) that is also compatible with [`docker-compose`](https://www.redhat.com/sysadmin/podman-docker-compose).

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

4. Execute the tests

```sh
docker-compose exec tests pytest tests.py
```
