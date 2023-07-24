import hou

def create_main_subnet():
    subnet_node = hou.node('/obj').createNode('subnet', 'extract_animation')
    subnet_node.moveToGoodPosition()
    return subnet_node

def create_divide_into_parts_geo_node(parent_node):
    divide_geo_node = parent_node.createNode('geo', 'divide_into_parts')
    divide_geo_node.moveToGoodPosition()
    return divide_geo_node

def divide_into_parts(parent_node, alembic_path):
    obj_merge = parent_node.createNode('object_merge', 'merge_alembic')
    obj_merge.moveToGoodPosition()
    obj_merge.parm('objpath1').set(alembic_path)
    divide_by_xform = parent_node.createNode('divide_by_xform')
    divide_by_xform.setInput(0, obj_merge)
    divide_by_xform.moveToGoodPosition(move_inputs=False)
    return divide_by_xform

def blast_all_except_current_part(parent_node, input_node, attrib, part):
    blast = parent_node.createNode('blast')
    blast.setInput(0, input_node)
    blast.moveToGoodPosition(move_inputs=False)
    blast.parm('group').set('@{0}={1}'.format(attrib, part))
    blast.setParms({'grouptype':3, 'negate':1})
    return blast

def create_static_output(parent_node, input_node, part):
    timeshift = parent_node.createNode('timeshift')
    timeshift.setInput(0, input_node)
    timeshift.moveToGoodPosition(move_inputs=False)
    frame_parm = timeshift.parm('frame')
    frame_parm.deleteAllKeyframes()
    frame_parm.set(1)
    null_node = parent_node.createNode('null', 'STATIC_PART_{0}'.format(part))
    null_node.setInput(0, timeshift)
    null_node.moveToGoodPosition(move_inputs=False)
    return null_node

def create_anim_output(parent_node, input_node, part):
    null_node = parent_node.createNode('null', 'ANIM_PART_{0}'.format(part))
    null_node.setInput(0, input_node)
    null_node.moveToGoodPosition(move_inputs=False)
    return null_node

def create_outputs(parent_node, input_node):
    attrib_name = input_node.evalParm('moving_parts_attrib')
    total_parts = input_node.geometry().attribValue(attrib_name)
    parts = {}
    for part in range(total_parts):
        part += 1
        blast_node = blast_all_except_current_part(parent_node, input_node, attrib_name, part)
        static_output = create_static_output(parent_node, blast_node, part)
        anim_output = create_anim_output(parent_node, blast_node, part)
        parts[part] = [static_output, anim_output]
    return parts

def main(alembic_path):
    subnet = create_main_subnet()
    divide_node = create_divide_into_parts_geo_node(subnet)
    divide_hda = divide_into_parts(divide_node, alembic_path)
    parts = create_outputs(divide_node, divide_hda)