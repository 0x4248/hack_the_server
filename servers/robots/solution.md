# Robots solution

The flag was `BA58365926GZ`.

## How to get the flag

Most websites have a file called `robots.txt` that tells search engines what pages they can and can't index. This is so that search engines don't index pages that are not meant to be seen by the public. This can sometimes be used to find hidden pages on a website.

If you go to `robots.txt` on the server you will see this:

```
User-agent: *
Allow: /
Disallow: /flag
```

This means allow robots to index all pages except `/flag`. If you go to `/flag` you will see the flag.