# add grass environment before run this


from grass.script import task as gtask

module='g.list'
commandspecs = gtask.command_info(module)



'''
command keys:
 dict_keys(['description', 'keywords', 'flags', 'params', 'usage'])

param:
dict_keys(['name', 'type', 'required', 'multiple', 'label', 'description', 'gisprompt', 'age', 'element', 'prompt', 'guisection', 'guidependency', 'default', 'values', 'values_desc', 'value', 'key_desc', 'hidden'])

flags:
dict_keys(['name', 'label', 'description', 'guisection', 'suppress_required', 'value', 'hidden'])
'''