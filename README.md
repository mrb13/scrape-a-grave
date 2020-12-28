# get-sites

> This Project is forked from & based on [scrape-a-grave] (https://github.com/pirtleshell/scrape-a-grave)


## Scraping
[FindAGrave](http://findagrave.com) is an index of gravemarkers from cemeteries around the world. Often when doing genealogy research, you don't want to rely on a webpage's future and so you want to download the information to your local file. This python script takes a list of Findagrave Cemeteries, or FindAGrave urls, scrapes the site for data and prints out a citation of the information. It is currently not setup to write the output anywhere except in print statement. 

Iteration 1 is ugly but functional. 


## Requirements

You are expected to have [Python3](https://www.python.org/downloads/). It also requires the BeautifulSoup package, downloadable through pip:
```sh
$ pip3 install bs4
```

## Usage
Download these files and change the contents of input text to be a list of FindAGrave ids, or FindAGrave urls. Then run
```sh
$ python3 get-sites.py
```


## License

This is intended as a convenient tool for personal genealogy research. Please be aware of FindAGrave's [Terms of Service](https://secure.findagrave.com/terms.html).

MIT © [Robert Pirtle](https://pirtle.xyz)
