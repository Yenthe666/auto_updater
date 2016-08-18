# auto_updater
This module will update your Odoo environment automatically.<br/>
The automated planner (found under Settings > Automation > Automated actions) will allow you to configure when and how often this should happen.
Three commands are executed:<br/>
<ul>
<li>git fetch origin x.x (which automatically detects your Odoo version)</li>
<li>git rebase --autostash</li>
<li>service odoo-server restart (Work in progress!)</li>
</ul>
