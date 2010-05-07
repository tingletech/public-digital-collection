import sys
import solr

SOLR_URL = 'http://localhost:8983/solr/'

def query_results(query):
    ''' Returns a solrpy response object.
    numCount and max? are interesting
    '''
    s = solr.SolrConnection(SOLR_URL)
    return s.query(query)

def query_results_text(query):
    ''' REturns string representation of query results
    '''
    markup = ''
    response = query_results(query)
    for result in response.results:
        markup = markup + result['content']
    return markup


if __name__=='__main__':
    query = sys.argv[1:]
    print  query_results_text(query)
