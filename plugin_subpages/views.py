# -*- coding: utf-8 -*-
from django.template import RequestContext
from ionyweb.website.rendering.utils import render_view

# from ionyweb.website.rendering.medias import CSSMedia, JSMedia, JSAdminMedia
MEDIAS = (
    # App CSS
    # CSSMedia('plugin_subpages.css'),
    # App JS
    # JSMedia('plugin_subpages.js'),
    # Actions JSAdmin
    # JSAdminMedia('plugin_subpages_actions.js'),
    )

def index_view(request, plugin):
    if plugin.ressources:
        template = 'plugin_subpages/ressources.html'
    else:
        template = 'plugin_subpages/index.html'
    return render_view(template,
                       {'object': plugin,
                        'pages': request.page.get_children()},
                       MEDIAS,
                       context_instance=RequestContext(request))