# mathsUtils

mathsUtils is a basic calculator app that can square or factorial a positive integer value.

## Installation 

Run python app in docker container

docker build -t python-calc .

## Usage

docker run python-calc --type '' --number

e.g. docker run python-calc --type 'square' --number 4

For help: docker run python-calc --help