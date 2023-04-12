bl_info = {
    "name": "Turn off Show Backface and rename UVs",
    "author": "@pentothalic \ thiopental#7679",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "description": "Option to turn off Show Backface for alpha materials and rename first UVMap for all selected objects",
    "category": "Material",
}

import bpy

#local imports
from .turn_off_backface_and_rename_uvs import MaterialShowBackfaceOff
from .turn_off_backface_and_rename_uvs import RenameUVMapOperator

#draw buttons in material view
class MATERIAL_PT_ShowBackfaceOff(bpy.types.Panel):
    bl_label = "Show Backface Off and Rename UV Map"
    bl_idname = "MATERIAL_PT_ShowBackfaceOff"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        layout.operator("material.show_backface_off")
        layout.operator("object.rename_uv_map")

def register():
    bpy.utils.register_class(MaterialShowBackfaceOff)
    bpy.utils.register_class(RenameUVMapOperator)
    bpy.utils.register_class(MATERIAL_PT_ShowBackfaceOff)

def unregister():
    bpy.utils.unregister_class(MaterialShowBackfaceOff)
    bpy.utils.unregister_class(RenameUVMapOperator)
    bpy.utils.unregister_class(MATERIAL_PT_ShowBackfaceOff)

if __name__ == "__main__":
    register()
