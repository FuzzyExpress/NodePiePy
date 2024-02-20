import bpy
from bpy.types import Menu, Operator
from bpy.props import EnumProperty

bl_info = {
    "name": "NodePiePy",
    "author": "FuzzyExpress",
    "version": (0, 0, 1, 23),
    "description": "Pie menus for quick Editor & World switching.",
    "blender": (3, 6, 0),
    "category": "Interface",
}

class VIEW3D_MT_PIE_fewindow_MT_fepie(Menu):
    bl_label = "Places"
    bl_idname = "VIEW3D_MT_PIE_fewindow_MT_fepie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("fewindow.shader")
        pie.operator("fewindow.geonodes")
        pie.operator("fewindow.files")
        pie.operator("fewindow.compositor")
        pie.operator("fewindow.3d")
        pie.operator("fewindow.timeline")

class Shader(Operator):
    bl_idname = "fewindow.shader"
    bl_label  = "Shader Nodes"

    def execute(self, context):
        bpy.context.area.ui_type = 'ShaderNodeTree'
        return {'FINISHED'}

class GeoNodes(Operator):
    bl_idname = "fewindow.geonodes"
    bl_label  = "Geometry Nodes"

    def execute(self, context):
        bpy.context.area.ui_type = 'GeometryNodeTree'
        return {'FINISHED'}

class Compositor(Operator):
    bl_idname = "fewindow.compositor"
    bl_label  = "Compositor"

    def execute(self, context):
        bpy.context.area.ui_type = 'CompositorNodeTree'
        return {'FINISHED'}

class Files(Operator):
    bl_idname = "fewindow.files"
    bl_label  = "Files"

    def execute(self, context):
        bpy.context.area.ui_type = 'FILES'
        return {'FINISHED'}

class VIEW_3D(Operator):
    bl_idname = "fewindow.3d"
    bl_label  = "3D View Port"

    def execute(self, context):
        bpy.context.area.ui_type = 'VIEW_3D'
        return {'FINISHED'}

class TIMELINE(Operator):
    bl_idname = "fewindow.timeline"
    bl_label  = "TimeLine"

    def execute(self, context):
        bpy.context.area.ui_type = 'TIMELINE'
        return {'FINISHED'}

###################


# Custom operator to switch worlds
class SwitchWorldOperator(bpy.types.Operator):
    bl_idname = "world.switch"
    bl_label = "Switcher Worlder"

    world_name_enum: bpy.props.StringProperty()

    def execute(self, context):
        bpy.context.scene.world = bpy.data.worlds.get(self.world_name_enum)
        return {'FINISHED'}

# Custom pie menu
class WorldSwitchPieMenu(bpy.types.Menu):
    bl_idname = "PIE_MT_world_switch"
    bl_label = "Switch World"

    def draw(self, context):
        layout = self.layout

        # Get a list of available worlds
        worlds = bpy.data.worlds
        print("\n\n\n", worlds)
        world_names = []
        for w in worlds:
            world_names.append(w.name)
        
        print(world_names)

        # Add an operator for each world
        for name in world_names:
            print(name)
            op = layout.operator("world.switch", text=name)
          #  op.world_name = name
            op.world_name_enum = name


def register():
    bpy.utils.register_class(VIEW3D_MT_PIE_fewindow_MT_fepie)
    bpy.utils.register_class(Shader)
    bpy.utils.register_class(GeoNodes)
    bpy.utils.register_class(Compositor)
    bpy.utils.register_class(Files)
    bpy.utils.register_class(VIEW_3D)
    bpy.utils.register_class(TIMELINE)

    bpy.utils.register_class(SwitchWorldOperator)
    bpy.utils.register_class(WorldSwitchPieMenu)

def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_PIE_fewindow_MT_fepie)
    bpy.utils.unregister_class(Shader)
    bpy.utils.unregister_class(GeoNodes)
    bpy.utils.unregister_class(Compositor)
    bpy.utils.unregister_class(Files)
    bpy.utils.unregister_class(VIEW_3D)
    bpy.utils.unregister_class(TIMELINE)

    bpy.utils.unregister_class(SwitchWorldOperator)
    bpy.utils.unregister_class(WorldSwitchPieMenu)

# Function to populate the pie menu
def menu_func(self, context):
    self.layout.menu(WorldSwitchPieMenu.bl_idname)

if __name__ == "__main__":
    register()

