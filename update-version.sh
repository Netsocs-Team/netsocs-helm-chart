#! /bin/bash

# This script updates the version in the helm chart

# Get the version from the command line
version=$1

# Update the version in the helm chart
# Use regex to match any existing version number
sed -i "s/version: \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/version: \"$version\"/g" netsocs-helm-chart/values.yaml