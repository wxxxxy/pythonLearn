# -*- coding: utf-8 -*-
#Web应用程序的WSGI处理函数
#hello.py
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	info = ''
	for k,v in environ.items():
		info = info+'<h2>\''+str(k).lower()+'\':\''+str(v)+'\'</h2>'
	body = '<h1>environ:</h1>%s' % info
	return [body.encode('utf-8')]
