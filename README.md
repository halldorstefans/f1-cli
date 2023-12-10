:warning: **THIS PROJECT IS NOT ACTIVE DUE TO THE FACT THE UNDERLYING API HAS BEEN DEPRECATED.** :warning:

See [Ergast API Documentation.](https://ergast.com/mrd/)

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

- [Table of Contents](#table-of-contents)
- [F1 CLI](#f1-cli)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## F1 CLI

Formula 1 Command-Line Tool to get race results, qualifying, schedule and standings

### Built With

* [Python](https://www.python.org/)
* [Click](https://palletsprojects.com/p/click/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3 >=3.8

### Installation

```sh
$ pip install formula1-cli
...
Successfully installed formula1-cli...
```

<!-- USAGE EXAMPLES -->
## Usage

Afterwards, your command should be available:

```sh
$ f1 --help
Usage: f1 [OPTIONS] COMMAND [ARGS]...

  Formula 1 Command-Line Tool to get race results, qualifying, schedule and
  standings

Options:
  -h, --help  Show this message and exit.

Commands:
  qualifying  List the qualifying results for a specific race.
  results     List the results for a specific race.
  schedule    List the schedule for a specific race.
  standings   List the driver/constructor standings for a specific season.
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
