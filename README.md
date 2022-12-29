# wiki-basgrospoing
An old mediawiki I painfully have to convert to something else.

## Required HTACCESS

```
RewriteEngine On
RewriteCond %{REQUEST_URI} !\.[a-zA-Z0-9]{3,4}
RewriteCond %{REQUEST_URI} !/$
RewriteRule ^(.*)$ $1.html
```