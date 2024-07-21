# e-flux Data

A Python package to scrape announcements from e-flux.

## Quickstart

- Install with `poetry install`.
- Choose how many pages you want in `main.py`.
- Run it: `poetry run python main.py`.

## Mapping the e-flux API

The e-flux API v2 is quite bizarre.

### search

Search for entries, on various

https://www.e-flux.com/v2/api/search?t[]=announcement&t[]=arannouncement&t[]=tvannouncement&t[]=aaannouncement&t[]=aeannouncement&ed[]=2024-07-19,2024-07-19

https://www.e-flux.com/search?q=test&t[]=journalarticle&order=relevance

Some of the options for the arguments can be found through filterlist. For all the arguments, to search for multiple values of the key at the same time, add more keys and values: e.g. `t[]=announcement&t[]=aeannouncement` searches for announcements and educational announcements.

`t` is the 'types'. e.g. `t[]=aeannouncement` searches for educational announcements.
`y` is the 'Year'. e.g. `y[]=2021`.
`l` is the 'Location'. e.g. `l[]=Amsterdam`.
`i` is the 'Institution'. e.g. `i[]=Bard College`.
`p` is the 'Artists, Authors, and Curators. e.g. `p[]=A.L. Steiner`.
`s` is 'Subjects'. e.g. `s[]=Abstraction`.
`c` is 'Categories'. e.g. `c[]=Aesthetics`.
`order` allows to sort by `relevance`, `newest` or `oldest`.
`ed` filters by 'Calender', allowing a start and end date (inclusive). e.g. `ed[]=2024-07-19,2024-07-19`. (The date doesn't seem to strictly be the date of publishing or the date of the exhibition but it allow any exhibition that has dates overlapping with the date selection.)

### filterlist

A list of values that can be filtered by

https://www.e-flux.com/v2/api/filterlist?list=institutions&t[]=announcement&t[]=arannouncement&t[]=tvannouncement&t[]=aaannouncement&t[]=aeannouncement&empty=1&order=relevance

https://www.e-flux.com/v2/api/filterlist?list=cities&t[]=announcement&t[]=arannouncement&t[]=tvannouncement&t[]=aaannouncement&t[]=aeannouncement&empty=1&order=relevance

https://www.e-flux.com/v2/api/filterlist?list=categories&t[]=announcement&t[]=arannouncement&t[]=tvannouncement&t[]=aaannouncement&t[]=aeannouncement&empty=1&order=relevance

https://www.e-flux.com/v2/api/filterlist?list=subjects&t[]=announcement&t[]=arannouncement&t[]=tvannouncement&t[]=aaannouncement&t[]=aeannouncement&empty=1&order=relevance

https://www.e-flux.com/v2/api/filterlist?list=participants&t[]=announcement&t[]=arannouncement&t[]=tvannouncement&t[]=aaannouncement&t[]=aeannouncement&empty=1&order=relevance

https://www.e-flux.com/v2/api/filterlist?list=types&q=test&order=relevance

https://www.e-flux.com/v2/api/filterlist?list=years&q=test&order=relevance

### searchsuggestions

As you type, this will give suggestions for your current search

https://www.e-flux.com/v2/api/searchsuggestions?q=test

### related

Entries related to the first one

https://www.e-flux.com/v2/api/related/582068

### homepage

Contains html for a given home page(!).

https://www.e-flux.com/v2/api/homepage/architecture/
