# cpmp-datasets

Datasets from [CPMP-Tools](https://www.core-plusmath.org/CPMP-Tools/) extracted and reformatted as .tsv files for use in other applications.

## Usage
All of the original `.cmt` files have been included in the `data` folder.
The new, converted `.tsv` files are in the `tsv/` folder.

Essentially, this boiled down to removing the "header" information from the cmt files:
```
# Data Analysis
#These data contain winning times (in seconds) for women and men in the Olympic 100-meter freestyle swim for games since 1912. (Source: www.olympic.org)
100-meter Freestyle
iC dC dC
```

Eventually, this information will be used to generate an index of all of the datasets to be used alongside the tsv files.

You can generate the `.tsv` files for yourself by using the included `converter.py`.

## License

CPMP-Tools is released under the GPLv2. These reformatted datasets are also available under GPLv2. See [LICENSE.md](LICENSE.md) for a copy of the license.