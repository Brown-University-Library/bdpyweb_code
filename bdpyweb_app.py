# -*- coding: utf-8 -*-

import datetime, json, os, pprint
import flask
from bdpyweb_code.utils import log_helper
from flask.ext.basicauth import BasicAuth  # http://flask-basicauth.readthedocs.org/en/latest/
from utils.app_helper import Helper


app = flask.Flask(__name__)
app.config[u'BASIC_AUTH_USERNAME'] = unicode( os.environ[u'bdpyweb__BASIC_AUTH_USERNAME'] )
app.config[u'BASIC_AUTH_PASSWORD'] = unicode( os.environ[u'bdpyweb__BASIC_AUTH_PASSWORD'] )
basic_auth = BasicAuth( app )
API_AUTHORIZATION_CODE = unicode( os.environ[u'bdpyweb__API_AUTHORIZATION_CODE'] )  # for v1
API_IDENTITY = unicode( os.environ[u'bdpyweb__API_IDENTITY'] )  # for v1
LEGIT_IPS = json.loads( unicode(os.environ[u'bdpyweb__LEGIT_IPS']))
logger = log_helper.setup_logger()
hlpr = Helper( logger )


@app.route( u'/', methods=[u'GET'] )  # /bdpyweb
def root_redirect():
    """ Redirects to readme. """
    logger.debug( u'starting' )
    return flask.redirect( u'https://github.com/birkin/bdpyweb_code/blob/master/README.md', code=303 )


@app.route( u'/v1', methods=[u'POST'] )  # /bdpyweb/v1/
def handle_v1():
    """ Handles post & returns json results. """
    if hlpr.validate_request( flask.request.form ) == False:
        flask.abort( 400 )  # `Bad Request`
    logger.debug( u'starting' )
    return_dict = { u'foo': u'bar' }
    return flask.jsonify( return_dict )


@app.route( u'/v2/', methods=[u'GET'] )  # /bdpyweb/v2/
@basic_auth.required
def handle_v2():
    """ Handles post & returns json results. """
    logger.debug( u'starting' )
    return_dict = { u'foo': u'bar' }
    return flask.jsonify( return_dict )




if __name__ == u'__main__':
    if os.getenv( u'DEVBOX' ) == u'true':
        app.run( host=u'0.0.0.0', debug=True )
    else:
        app.run()
