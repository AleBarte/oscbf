"""Creating a link collision model for the UR5e with a series of spheres of various radii"""

# All positions are in link frame, not link COM frame
# UR5e has 6 joints (shoulder_pan, shoulder_lift, elbow, wrist_1, wrist_2, wrist_3)

# Base link - link frame origin is at base, geometry extends upward
# shoulder_pan_joint is at (0, 0, 0.163) relative to base_link
base_link_pos = (
    (0, 0, 0),
)
base_link_radii = (
    0.08,
)

# Shoulder link - link frame origin at shoulder_pan joint
# shoulder_lift_joint is at (0, 0.138, 0) with 90° pitch rotation
shoulder_link_pos = (
    (0, 0, 0),
    (0, 0, 0.15),
    (0, 0, 0.30),
    (0, 0.0, 0.4)
)
shoulder_link_radii = (
    0.09,
    0.06,
    0.06,
    0.09
)

# Upper arm link - link frame origin at shoulder_lift joint (already rotated 90° in pitch)
# In link frame, arm extends in +Z direction, with slight -Y offset
# elbow_joint is at (0, -0.131, 0.425)
upper_arm_link_pos = (
    (0, 0, 0),
    (0, 0, 0.15),
    (0, 0, 0.30)
)
upper_arm_link_radii = (
    0.09,
    0.06,
    0.06
)

# Forearm link - link frame origin at elbow joint
# wrist_1_joint is at (0, 0, 0.392) with 90° pitch rotation
forearm_link_pos = (
    (0, 0, 0),
)
forearm_link_radii = (
    0.07,
)

# Wrist 1 link - link frame origin at wrist_1 joint
# wrist_2_joint is at (0, 0.127, 0) 
wrist_1_link_pos = (
    (0, 0, 0),
)
wrist_1_link_radii = (
    0.06,
)

# Wrist 2 link - link frame origin at wrist_2 joint
# wrist_3_joint is at (0, 0, 0.1)
wrist_2_link_pos = (
    (0, 0, 0),
)
wrist_2_link_radii = (
    0.06,
)

# Wrist 3 link - link frame origin at wrist_3 joint
# tool0 is at (0, 0.1, 0) after rotation
wrist_3_link_pos = (
    (0, 0.1, 0),
    (0, 0.2, 0),
)
wrist_3_link_radii = (
    0.06,
    0.06,
)

positions_list = (
    shoulder_link_pos,
    upper_arm_link_pos,
    forearm_link_pos,
    wrist_1_link_pos,
    wrist_2_link_pos,
    wrist_3_link_pos,
)

radii_list = (
    shoulder_link_radii,
    upper_arm_link_radii,
    forearm_link_radii,
    wrist_1_link_radii,
    wrist_2_link_radii,
    wrist_3_link_radii,
)

ur5e_collision_data = {"positions": positions_list, "radii": radii_list}

##### Self collisions #####

# Simplified model for self-collision detection
# Most critical pairs: base vs wrist/forearm, shoulder vs forearm/wrist, upper_arm vs wrist

# Base link
base_link_pos_sc = (
    (0, 0, 0.08),  # 0 - top of base
)
base_link_radii_sc = (
    0.10,
)

# Shoulder link
shoulder_link_pos_sc = (
    (0, 0.069, 0),  # 1 - shoulder joint area
)
shoulder_link_radii_sc = (
    0.08,
)

# Upper arm link
upper_arm_link_pos_sc = (
    (0, 0, 0.1),    # 2 - near shoulder
)
upper_arm_link_radii_sc = (
    0.07,
)

# Forearm link
forearm_link_pos_sc = (
    (0, 0, 0.0),    # 3 - near elbow
)
forearm_link_radii_sc = (
    0.065,
)

# Wrist 1 link
wrist_1_link_pos_sc = (
    (0, 0.064, 0),  # 4 - middle of wrist 1
)
wrist_1_link_radii_sc = (
    0.055,
)

# Wrist 2 link
wrist_2_link_pos_sc = (
    (0, 0, 0.05),   # 5 - middle of wrist 2
)
wrist_2_link_radii_sc = (
    0.055,
)

# Wrist 3 link
wrist_3_link_pos_sc = (
    (0, 0.05, 0),   # 6 - end effector area
)
wrist_3_link_radii_sc = (
    0.15,
)

positions_list_sc = (
    base_link_pos_sc,
    shoulder_link_pos_sc,
    upper_arm_link_pos_sc,
    forearm_link_pos_sc,
    wrist_1_link_pos_sc,
    wrist_2_link_pos_sc,
    wrist_3_link_pos_sc,
)

radii_list_sc = (
    base_link_radii_sc,
    shoulder_link_radii_sc,
    upper_arm_link_radii_sc,
    forearm_link_radii_sc,
    wrist_1_link_radii_sc,
    wrist_2_link_radii_sc,
    wrist_3_link_radii_sc,
)

# Critical self-collision pairs (sphere_index, sphere_index)
# Most common: forearm/wrist hitting shoulder/base in folded configurations
pairs_sc = (
    (0, 6),  # base vs forearm near elbow
    # (0, 6),  # base vs forearm near wrist
    # (0, 7),  # base vs wrist_1
    # (0, 8),  # base vs wrist_2
    # (0, 9),  # base vs wrist_3
    # (1, 5),  # shoulder vs forearm near elbow
    # (1, 6),  # shoulder vs forearm near wrist
    # (1, 7),  # shoulder vs wrist_1
    (1, 6),  # upper_arm near shoulder vs forearm near wrist
    # (2, 7),  # upper_arm near shoulder vs wrist_1
    # (2, 8),  # upper_arm near shoulder vs wrist_2
    # (3, 7),  # upper_arm middle vs wrist_1
    # (3, 8),  # upper_arm middle vs wrist_2
)

ur5e_self_collision_data = {
    "positions": positions_list_sc,
    "radii": radii_list_sc,
    "pairs": pairs_sc,
}

# World base (if fixed to ground/table)
base_position = (0.0, 0.0, 0.0)
base_radius = 0.12
base_sc_idxs = (0,  3, 6)  # Check forearm and wrist links against world base

base_self_collision_data = {
    "position": base_position,
    "radius": base_radius,
    "indices": base_sc_idxs,
}