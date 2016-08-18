# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.release import version_info
import logging
_logger = logging.getLogger(__name__)
import os, getpass
import pexpect

class odoo_updater(models.Model):
    _name = 'odoo.updater'
    name = fields.Char()

    @api.model
    def update_odoo_codebase(self):
        odoo_user = getpass.getuser()

        #  Fetch updates from Github
        fetch_from_github_cmd = "git fetch origin " + str(version_info[0]) + str(".0")
        child = pexpect.spawn(fetch_from_github_cmd)
        child.expect(pexpect.EOF)
        _logger.info('git fetch origin output: ' + str(child.before))

        #  Apply updates from Github
        update_from_github_cmd = "git rebase --autostash"
        child = pexpect.spawn(update_from_github_cmd)
        child.expect(pexpect.EOF)
        _logger.info('git rebase --autostash output: ' + str(child.before))

        # Restart the Odoo service in order te reload all changes from the updates.
        """
        restart_service = "service " + str(getpass.getuser()) + '-server restart'
        _logger.critical('restart_service: ' + str(restart_service))
        child = pexpect.spawn(restart_service)
        child.expect(pexpect.EOF)
        _logger.info('Odoo service has been restarted! Output: ' + str(child.before))
        """
