set -eu
which virtualenv
#cd $PREFIX
virtualenv  .
./bin/easy_install django
./bin/easy_install solrpy
./bin/easy_install django-debug-toolbar
