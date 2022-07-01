#!/bin/bash

COURSE="ikt103"

SOLUTION_IMAGE=$COURSE/$1
CONTAINER_NAME=$COURSE-test

error()
{
    echo "$1" >&2
}

# Checks for command errors and prints result message
check()
{
    if [[ $? -eq 0 ]]; then
        error "$1"
    else
        error "Error: $2"
        exit 1
    fi
}

# Check if Docker is installed
docker >/dev/null 2>&1

if [[ $? -eq 127 ]]; then
    error "Error: Docker is not installed."
    error "Fix  : See instructions in Canvas for details."
    exit 1
fi

# Check if Docker is working
docker info >/dev/null 2>&1

if [[ $? -ne 0 ]]; then
    # Rerun to show errors
    docker info
    error "Error: Docker failed to run."
    error "Fix  : Is Docker running? If not, start it. If it is ask for help in the lab."
    exit 1
fi

# Check Docker OS type
OS_TYPE=$(docker info --format '{{ .OSType }}')

if [[ "$OS_TYPE" = "windows" ]]; then
    error "Error: Docker is configured for Windows containers. We need Linux containers."
    error "Fix  : Right click Docker and choose 'Switch to Linux containers...'"
    exit 1
fi

# Remove dangling images if there are more than 100 images in total
if [[ $(docker images | wc -l) -gt 100 ]]; then
    error "Cleaning up Docker..."
    docker image prune -f
    check "Docker cleanup completed successfully." "Failed to complete Docker cleanup."
fi

# Check for assignment parameter
if [[ "$1" = "" ]]; then
    error "Usage: ./test.sh <assignment>"
    exit 0
fi

# Check for the existence of assignment tests
COUNT=$(find . -name "test_assignment_$1.py" -or -name "test_assignment_$1_*.py" | wc -l)
if [[ $COUNT -eq 0 ]]; then
    error "Error: Failed to find tests for assignment $1."
    error "Fix  : Check if the assignment number is correct. If it is ask for help in the lab."
    exit 1
fi

# Check for solutions directory
if [[ ! -d "solutions" ]]; then
    error "Error: Failed to find solutions directory."
    error "Fix  : Course preparations might have failed. Ask for help in the lab."
    exit 1
fi

# Check for existence of solution directories
COUNT=$(find solutions -name "assignment_$1" -or -name "assignment_$1_*" | wc -l)
if [[ $COUNT -eq 0 ]]; then
    error "Error: Failed to find assignment $1 in the solutions directory."
    error "Fix  : Check if the assignment directory name is correct. If it is ask for help in the lab."
    exit 1
fi

# Common cleanup code
cleanup()
{
    error ""
    error "Cleaning up containers..."
    docker rm -f test >/dev/null 2>&1
    docker ps | grep $COURSE | awk '{ print $1 }' | xargs docker rm -f >/dev/null 2>&1
    error "Done cleaning up containers."
}

# Cleanup if any signals are received
trap cleanup SIGHUP SIGINT SIGTERM

# Cleanup from previous run
cleanup

error "Building solution image..."
docker build . -t "$SOLUTION_IMAGE" --build-arg ASSIGNMENT="$1"
check "Docker solution image built successfully." "Failed to build Docker solution image."

# Git Bash Docker workaround
export MSYS_NO_PATHCONV=1

if [[ "$BAMBOO" -eq 1 ]]; then
    docker run --rm --init --name "$CONTAINER_NAME" -v bamboo-agent_results:/results \
        "$SOLUTION_IMAGE" --junitxml /results/results.xml test_temp_files.py test_assignment_"$1"*.py $2 $3 $4 $5
else
    docker run --rm --init --name "$CONTAINER_NAME" \
        "$SOLUTION_IMAGE" test_assignment_"$1"*.py $2 $3 $4 $5
fi

# Cleanup after running tests
cleanup
