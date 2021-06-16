# cpmp-datasets

Datasets from Core-Plus Mathematics's [CPMP-Tools](http://www.core-plusmath.org/CPMP-Tools/) extracted and reformatted as .tsv files for use in other applications.

## Usage
All of the original `.cmt` files from CPMP-Tools 4.0 have been included in the `data` folder.
The new, converted `.tsv` files are in the `tsv` folder.

Essentially, this boiled down to removing the "header" information from the top of the .cmt files:
```
# Data Analysis
#These data contain winning times (in seconds) for women and men in the Olympic 100-meter freestyle swim for games since 1912. (Source: www.olympic.org)
100-meter Freestyle
iC dC dC
```

This information is used to generate an index of all of the datasets in the tsv folder.

You can generate the `.tsv` files and [tsv/README.md](tsv/README.md) for yourself by running the included `converter.py` from the `utils` directory.

## License

CPMP-Tools (C) 2012 B. A. Keller, Michigan State University and the Core-Plus Mathematics Project, Western Michigan University.

CPMP-Tools is released under the GPLv2. These reformatted datasets are also available under GPLv2. See [LICENSE.md](LICENSE.md) for a copy of the license.
