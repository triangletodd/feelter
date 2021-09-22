# feelter
Filter an RSS or ATOM feed by title, description, or both.

# Prep
```console
$ git clone https://github.com/triangletodd/feelter.git
$ cd feelter
$ pip3 install -r requirements.txt
```

# Usage
## Print all links
`./feelter.py 'https://rarbg.to/rssdd.php?categories=#'`
## Print all links matching title
`./feelter.py 'https://rarbg.to/rssdd.php?categories=#' --title 1080p`
## Print all links matching description
`./feelter.py 'https://rarbg.to/rssdd.php?categories=#' --description 1080p`
## Print all links matching title and description
`./feelter.py 'https://rarbg.to/rssdd.php?categories=#' --title 1080p --description 1080p`



