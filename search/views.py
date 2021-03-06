from django.shortcuts import render, render_to_response,RequestContext,get_object_or_404
from django.core.urlresolvers import reverse
from .Bing import Bing
from .extract_content import ExtractContent
# from django.template import Context, loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
import requests

def home(request):

    if request.method == 'POST':
        query = request.POST['query']
        bing = Bing()
        results = bing.web_search(query, 5, ['Url','Title'])
        # results = [{"Url":'http://google.com','Title':'Google'},
        #            {"Url":'http://yahoo.com','Title':'Yahoo'},
        #
        #            ]
        extractor = ExtractContent()

        opt = {"threshold":50}
        extractor.set_option(opt)
        print('hello world')

        url = results[0]["Url"]
        resp=requests.get(url)
        html=resp.text
        number = 3 / 2
        # html = open("yono python-extractcontent.html").read()
        extractor.analyse(html)
        text, title = extractor.as_text()

    return render_to_response('search.html',
                              locals(),
                              context_instance=RequestContext(request))

