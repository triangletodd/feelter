# feelter
Filter an RSS or ATOM feed by title or description.

# Prep
`pip3 install -r requirements.txt`

# Usage
## Print all links
`./feelter.py https://rarbg.to/rssdd.php?categories=#`
## Print all links matching title
`./feelter.py https://rarbg.to/rssd.php?categories=# --title 1080p`
## Print all links matching description
`./feelter.py https://rarbg.to/rssd.php?categories=# --description 1080p`
## Print all links matching title and description
`./feelter.py https://rarbg.to/rssd.php?categories=# --title 1080p --description 1080p`



