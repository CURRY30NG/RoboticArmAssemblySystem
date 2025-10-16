# Copyright (c) 2024 Fraunhofer IOSB and contributors
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the Fraunhofer IOSB nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

from ament_index_python import get_package_share_directory

import launch
from launch_ros.actions import Node

os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '{time}: [{name}] [{severity}]\t{message}'
# Verbose log:
# os.environ['RCUTILS_CONSOLE_OUTPUT_FORMAT'] = '{time}: [{name}] [{severity}]\t{message} '
# '({function_name}() at {file_name}:{line_number})'


# Start as node:
def generate_launch_description():

    example_package_node = Node(
        name='camera_driver_uv_example',
        package='camera_aravis2',
        executable='camera_driver_uv',
        output='screen',
        emulate_tty=True,
        # arguments=['--ros-args', '--log-level', 'debug'],
        parameters=[
                {
                    # Driver-specific parameters
                    'guid': 'IDS Imaging Development Systems GmbH-1409f4e6b698-4108760728',
                    'frame_id': 'camera_uv',
                    'stream_names': ['vis'],
                    'camera_info_urls': [os.path.join(
                        get_package_share_directory('camera_aravis2'),
                        'config/ost.yaml')],
                    'dynamic_parameters_yaml_url': os.path.join(
                        get_package_share_directory('camera_aravis2'),
                        'config/dynamic_parameters_example.yaml'),
                    'verbose': False,

                    # GenICam-specific parameters
                    'DeviceControl': {
                        'DeviceLinkThroughputLimit': 25000000000,
                    },
                    'ImageFormatControl': {
                        'PixelFormat': ['BGR8'],
                        'Width': 5472,
                        'Height': 3672,
                        'BinningHorizontal': 1,
                        'BinningVertical': 1,
                        'OffsetX': 32,
                        'OffsetY': 10
                    },
                    'AcquisitionControl': {
                        'AcquisitionFrameRateEnable': True,
                        'AcquisitionFrameRate': 30.0,
                        'ExposureAuto': 'Continuous'
                    },
                    'AnalogControl': {
                        'GainAuto': 'Continuous',
                        'BalanceWhiteAuto': 'Continuous'
                    }
                }
            ]
    )
    return launch.LaunchDescription([example_package_node])
