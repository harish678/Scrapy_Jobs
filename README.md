# GovBot
This is a Scrapy project to scrape Jobs from Government Sites.

## Spiders

This project contains two spiders and you can list them using the `list`
command:

    $ scrapy list
    isro

Spiders extract the job notification data from the websites.

You can learn more about the spiders by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl isro

If you want to save the scraped data to a file, you can pass the `-o` option and `-t` type:
    
    $ scrapy crawl isro -t csv -o isro.csv