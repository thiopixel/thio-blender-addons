# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

class MaterialShowBackfaceOff(bpy.types.Operator):
    "Turn off show backface for all alpha materials on  currently selected objects"
    bl_idname = "material.show_backface_off"
    bl_label = "Turn Off Show Backface"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_materials = set()
        for obj in context.selected_objects:
            if obj is not None and obj.type == 'MESH':
                for mat_slot in obj.material_slots:
                    if mat_slot.material is not None:
                        selected_materials.add(mat_slot.material)

        for material in bpy.data.materials:
            if material in selected_materials:
                material.show_transparent_back = False

        print("backfacesoff")
        return {'FINISHED'}

class RenameUVMapOperator(bpy.types.Operator):
    "Rename the first UVMap to 'UVMap' for every selected object"
    bl_idname = "object.rename_uv_map"
    bl_label = "Rename UV Map"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj is not None and obj.type == 'MESH':
                if len(obj.data.uv_layers) > 0:
                    obj.data.uv_layers[0].name = 'UVMap'

        print("uvmapsrenamed")
        return {'FINISHED'}
