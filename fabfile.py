# -*- coding: utf-8 -*- #
from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver
import datetime

from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Github Pages configuration
    'github_pages_branch': 'master',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Host and port for `serve`
    'host': 'localhost',
    'port': 8000,
}

def clean():
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

def _copy_extra_files():
    #Hakcy way to publish README.md to `master` banch
    local("cp README.md {deploy_path}".format(**CONFIG))
    
    local("cp .gitignore {deploy_path}".format(**CONFIG))
    local("cp google7ed5b9715d9d7c37.html {deploy_path}".format(**CONFIG))
    local("cp favicons/* {deploy_path}".format(**CONFIG))

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')
    _copy_extra_files()

def publish_build():
    """Build local version of site"""
    local('pelican -s publishconf.py')
    _copy_extra_files()

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving at {host}:{port} ...\n'.format(**CONFIG))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def pages(comment):
    """Prepare GitHub Pages, put it on master branch"""
    clean()
    publish_build()
    env.comment=comment
    local("ghp-import -m '{comment}' -b {github_pages_branch} {deploy_path}".format(comment=comment, **CONFIG))

def push():
    """Publish GibHub Pages"""
    local("git push origin {github_pages_branch}".format(**CONFIG))

def live():
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build()
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build())
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build())
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build())
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build())
    # Serve output path on configured host and port
    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])
