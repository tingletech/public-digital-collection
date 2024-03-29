import solr
from django.shortcuts import get_object_or_404, render_to_response
from django.conf import settings

SOLR_URL = settings.SOLR_URL if settings.SOLR_URL else 'http://localhost:8983/solr/'

def query_response(query, fq=''):
    ''' Returns a solrpy response object.
    numCount and max? are interesting
    '''
    s = solr.SolrConnection(SOLR_URL, debug=True)
    return s.query(query,
                    #fields=('score', 'id', 'title', 'url', 'content', 'markup'),
                    fields=('score', 'id', 'title', 'url', 'content'),
                    highlight=True,
                    hl_snippets = 4,
                    hl_fragsize = 100,
                    #hl_simple_pre='<span class="search_highlight">',
                    #hl_simple_post='</span>',
                    spellcheck='true', 
                    spellcheck_collate='true', 
                    # facet_field=['site','host'],
                    facet='true', 
                    fq = fq,
                  )

def query_results_text(query):
    ''' REturns string representation of query results
    '''
    markup = ''
    response = query_response(query)
    markup += '<h2>Number of results:%s</h2>' % (response.numFound,)
    markup += '<h3>maxScore:%s</h3>\n' % (response.maxScore,)
    for result in response.results:
        markup += result['url']
        markup += '<br></br>\n'
        for fragment in response.highlighting[result['url']]['content']:
            markup += fragment
            markup += '<br></br>\n'
        markup += '<br></br><hr></hr><br></br>\n'
    return markup

def get_highlights_for_result(result, highlights):
    '''Get the search result snippets for given result
    '''
    try:
        result_highlights = highlights.get(result['url'])
    except:
        result_highlights = ""
    #check if has contents, if not fill in with?
    try:
        content = result_highlights.get('content', None)
    except:
        content = ""
    if content:
        snippets = content
    else:
        snippets = ["<span class='flagBG2'>No snippets found for this result</span>",]
    return snippets
    

def get_search_page(request):
    query = request.GET.get('q', '')
    perpage = request.GET.get('perpage', 10)
    fq = request.GET.get('fq', '')
    try:
        perpage = int(perpage)
    except ValueError:
        perpage = 10
    pagenum = request.GET.get('pagenum', 1)
    try:
        pagenum = int(pagenum)
    except ValueError:
        pagenum = 1
    return view_search_page(request, query, perpage, pagenum, fq)

def view_search_page(request, query, perpage=20, pagenum=1, fq=''):
    ''' Query the solr server with any search terms.
    '''
    #import sys
    #print >> sys.stdout, 'PERPAGE=', perpage
    #print >> sys.stdout, 'pagenum=', pagenum
    hostname = request.META.get('SERVER_NAME', 'ucportal-dev.cdlib.org')
    searchError = None
    if query is None:
        return render_to_response('ucsearch/search.html')
    query = query.lstrip('/')
    try:
        response = query_response(query, fq)
    except solr.SolrException, e:
        msg = ''.join([ 'Solr query problem.',
                        '; HTTP Code:', unicode(e.httpcode),
                        '; Reason:', e.reason,
                        #'Message', e.message, '; ',
                        '\n Solr Error HTML: ', e.body.replace('\n',' '),
                        #'; Args', unicode(e.args), '; ',
                        ]
                 )
        import sys
        print >> sys.stderr, msg
        searchError = "There was a problem with your query"
        return render_to_response('ucsearch/solr_error.html', locals())

    try:
        spelling_suggestion = response.spellcheck['suggestions'].get('collation',None)
    except:
        spelling_suggestion = ""
    number_results = int(response.results.numFound)
    if number_results == 0:
        return render_to_response('ucsearch/search.html', locals())

    pager = solr.SolrPaginator(response)
    pager.page_size = perpage
    #print >> sys.stdout, "NUM PAGES=", pager.num_page
    page_current = pager.page(pagenum)
    results = page_current.result
    #print >> sys.stdout, "LEN RESULTS=", len(results)
    #results = response.results
    for result in results:
        result['snippets'] = get_highlights_for_result(result, page_current.highlighting)
        #result['snippets'] = get_highlights_for_result(result, response.highlighting)
        if result['url'][0] == '/':
            result['url'] = 'http://'+ hostname + result['url']
    #perpage_options = [10,100,]
    perpage_options = [10,]
    if perpage not in perpage_options:
        perpage_options.append(perpage)

    #perpage_options = ['4','5','6','7','8','9','10','15','20','25','30',]
    # stringify perpage for use in ifequal tag
    #perpage = str(perpage)
    #perpage_test = str(perpage)

    return render_to_response('ucsearch/search.html', locals())
