# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at

# http://www.apache.org/licenses/LICENSE-2.0

# or in the "license" file accompanying this file. This file is distributed 
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
# express or implied. See the License for the specific language governing 
# permissions and limitations under the License.

"""athena_glue_service_logs is a library for converting AWS Service Logs into a more Athena-friendly format"""
import sys

# Ensure python version 2.7.x as this was written before glue supported python 3
assert sys.version_info[:2] == (2, 7), "athena-glue-service-logs currently only supports python 2.7."
