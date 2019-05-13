# -*- coding: utf-8 -*- #
# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""List autoscaling policies command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import list_pager

from googlecloudsdk.api_lib.dataproc import constants
from googlecloudsdk.api_lib.dataproc import dataproc as dp
from googlecloudsdk.api_lib.dataproc import util
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.core import properties


class List(base.ListCommand):
  """List autoscaling policies."""

  @staticmethod
  def Args(parser):
    region_prop = properties.VALUES.dataproc.region
    parser.add_argument(
        '--region',
        help=region_prop.help_text,
        # Don't set default, because it would override users' property setting.
        action=actions.StoreProperty(region_prop))
    base.PAGE_SIZE_FLAG.SetDefault(parser, constants.DEFAULT_PAGE_SIZE)
    parser.display_info.AddFormat("""
          table(
            id:label=ID
          )
    """)
    # Implementation of --uri prints out "name" field for each entry
    parser.display_info.AddUriFunc(lambda resource: resource.name)

  def Run(self, args):
    dataproc = dp.Dataproc(self.ReleaseTrack())
    messages = dataproc.messages

    regions = util.ParseRegion(dataproc)

    request = messages.DataprocProjectsRegionsAutoscalingPoliciesListRequest(
        parent=regions.RelativeName())

    return list_pager.YieldFromList(
        dataproc.client.projects_regions_autoscalingPolicies,
        request,
        limit=args.limit,
        field='policies',
        batch_size=args.page_size,
        batch_size_attribute='pageSize')