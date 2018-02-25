#!-*- coding: utf-8 -*-
from django.db import connection
from django.template import Template, Context
from django.utils.deprecation import MiddlewareMixin


class Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        content_types = ('text/plain', 'text/html')
        if request.META['CONTENT_TYPE'] not in content_types:
            return response
        time = sum([float(qs['time']) for qs in connection.queries])
        template = Template("""<div class="debug">
                <p>Количество запросов: {{ count }}</p>
                <p>Время запроса: {{ time }} с.</p>
            <div>
            """)
        render = template.render(Context(dict(time=time, count=len(connection.queries))))
        cont = response.content.decode('utf-8')
        body = '</body>'
        position = cont.find(body)
        content = cont[:position] + render + cont[position:]
        response.content = content.encode('utf-8')
        return  response
