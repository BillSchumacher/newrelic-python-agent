# Copyright 2010 New Relic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

from newrelic.admin import command, usage


@command('license-key', 'config_file [log_file]',
         """Prints out the account license key after having loaded the settings from <config_file>.""")
def license_key(args):
    from newrelic.admin.helpers import initialize_usage
    _settings = initialize_usage('license-key', args)
    print('license_key = %r' % _settings.license_key)
