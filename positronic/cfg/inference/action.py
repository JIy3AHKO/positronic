import configuronic as cfn
from positronic import geom
from positronic.inference.action import AbsolutePositionAction, RelativeRobotPositionAction, UMIRelativeRobotPositionAction


umi_relative = cfn.Config(
    UMIRelativeRobotPositionAction,
    rotation_representation=geom.Rotation.Representation.ROTVEC,
    offset=1
)

relative_robot_position = cfn.Config(
    RelativeRobotPositionAction,
    rotation_representation=geom.Rotation.Representation.ROTVEC,
    offset=1
)

absolute_robot_position = cfn.Config(
    AbsolutePositionAction,
    rotation_representation=geom.Rotation.Representation.ROTVEC,
)