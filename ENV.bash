export PREFIX=$HOME/public-digital-collection
export CATALINA_BASE=$PREFIX/java-homes/catalina_base
export CATALINA_HOME=$PREFIX/tomcat
export JAVA_HOME=/cdlcommon/products/jdk1.6.0_23
export PATH="$JAVA_HOME/bin:/cdlcommon/products/bin:$PATH"
export JAVA_OPTS=" -Dsolr.solr.home=$PREFIX/java-homes/solr_home -Dsolr.data.dir=$PREFIX/java-homes/solr_home/data"
alias shutdown=$PREFIX/tomcat/bin/shutdown.sh 
alias startup=$PREFIX/tomcat/bin/startup.sh
