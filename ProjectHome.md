vertical search engine for library websites

requires a patched solrpy http://code.google.com/r/briantinglecdliborg-solrpy/source/browse/solr/paginator.py that supports highlighting

requires a <a href='https://github.com/tingletech/nutch/commit/d034c6663ef08814cd2d28f1bd01de99a97b7034'>patched</a> nutch 1.3 that supports -numFetchers so it can utilize the max maps capacity

lucidworks solr http://www.lucidimagination.com/products/certified/solr

needs j2EE (tomcat) and wsgi (apache2/mod\_wsgi) application servers to serve front end site.  will do: investigate migrating to solr's new built in velocity templates, so it will be a one server app

steps to run the crawl on cloudera hadoop in ec2 on ebs https://gist.github.com/1126909 <--

remove a site from the index https://gist.github.com/1129533

screen cast of hadoop running http://www.screenr.com/Dids


