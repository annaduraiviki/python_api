from odoo import http
import logging
_logger = logging.getLogger(__name__)

class Controller(http.Controller):

    @http.route('/test/result', type='http', auth='public')
    def index(self, **args):
        _logger.info('The controller is called.')
        return '{"response": "OK"}'