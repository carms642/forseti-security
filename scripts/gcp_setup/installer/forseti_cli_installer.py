# Copyright 2017 The Forseti Security Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Forseti CLI installer"""

from forseti_installer import ForsetiInstaller

from utils.constants import TEMPLATE_TYPE_CLI


class ForsetiCLIInstaller(ForsetiInstaller):
    """Forseti command line interface installer"""
    def __init__(self, **kwargs):
        """Init

        Args:
            kwargs (dict): The kwargs.
        """
        super(ForsetiCLIInstaller, self).__init__(**kwargs)
        self.template_type = TEMPLATE_TYPE_CLI

    def run_setup(self):
        pass

    def get_deployment_values(self):
        pass

    def get_configuration_values(self):
        pass