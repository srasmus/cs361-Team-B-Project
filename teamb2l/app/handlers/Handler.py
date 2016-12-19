import os

import jinja2
import webapp2

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', 'web', 'views')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..', 'web', 'views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **kwargs):
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))
