# -*- coding: utf-8 -*- #
# Copyright 2015 Google Inc. All Rights Reserved.
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
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://datacatalog.googleapis.com/v1beta1/'
DOCS_URL = 'https://cloud.google.com/data-catalog/docs/'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  ENTRIES = (
      'entries',
      'entries',
      {},
      [],
      True
  )
  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      [u'projectsId'],
      True
  )
  PROJECTS_LOCATIONS = (
      'projects.locations',
      'projects/{projectsId}/locations/{locationsId}',
      {},
      [u'projectsId', u'locationsId'],
      True
  )
  PROJECTS_LOCATIONS_ENTRYGROUPS = (
      'projects.locations.entryGroups',
      'projects/{projectsId}/locations/{locationsId}/entryGroups/'
      '{entryGroupsId}',
      {},
      [u'projectsId', u'locationsId', u'entryGroupsId'],
      True
  )
  PROJECTS_LOCATIONS_ENTRYGROUPS_ENTRIES = (
      'projects.locations.entryGroups.entries',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/entryGroups/'
              '{entryGroupsId}/entries/{entriesId}',
      },
      [u'name'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing
