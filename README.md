<!-- PROJECT OVERVIEW -->
<br />
<p align="center">

  <h3 align="center">Formula 1 CLI</h3>

  <p align="center">
    Formula 1 Command-Line Tools
    <br />
    <a href="https://github.com/halldorstefans/f1-cli"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/halldorstefans/f1-cli/issues">Report Bug</a>
    ·
    <a href="https://github.com/halldorstefans/f1-cli/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#project-name)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## F1 CLI

Formula 1 Command-Line Tool to get race results, schedule and standings

### Built With

* [Python](https://www.python.org/)
* [Click](https://palletsprojects.com/p/click/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* virtualenv

If you are on Mac OS X or Linux:

```sh
pip install virtualenv --user
```

or if you use Ubuntu, try:

```sh
sudo apt-get install python-virtualenv
```

### Installation

To test the script, you can clone the repository, make a new virtualenv and then install the package:

```sh
$ git clone origin https://github.com/halldorstefans/f1-cli.git
$ virtualenv venv
...
$ . venv/bin/activate
$ pip install --editable .
...
Successfully installed Formula-1-CLI

```

<!-- USAGE EXAMPLES -->
## Usage

Afterwards, your command should be available:

```sh
$ f1 --help
Usage: f1 [OPTIONS] COMMAND [ARGS]...

  Formula 1 Command-Line Tool to get race results, schedule and standings

Options:
  -h, --help  Show this message and exit.

Commands:
  results    List the results for a specific or latest race
  schedule   List the schedule for a specific or latest race
  standings  List the driver/constructor standings for a specific or...
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Halldor Stefansson - [@halldorstefans](https://twitter.com/halldorstefans)

Project Link: [https://github.com/halldorstefans/f1-cli](https://github.com/halldorstefans/f1-cli)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Ergast Developer API](http://ergast.com/mrd/)
