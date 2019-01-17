# vascan_portal role

Install and configure the Vascan Portal.

# Requirements

The following roles should be applied first:

* common
* mysql
* tomcat8

A valid database dump should be available at the path configured with
vascan_portal_db_src or vascan_portal_db_url

# ElasticSearch
When you see that
```
TASK [app_vascan_portal : Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here)] ***********
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (15 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (14 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (13 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (12 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (11 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (10 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (9 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (8 retries left).
FAILED - RETRYING: Waiting until ElasticSearch Taxon count is matching MySQL (retry is expected here) (7 retries left).
...
```
Restart the elastic search with connecting to the vm and use that command:
```
$ sudo service elasticsearch restart
```
