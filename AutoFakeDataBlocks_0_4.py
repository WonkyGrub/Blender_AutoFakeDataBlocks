bl_info = {
    "name": "Advanced Save Unused Data Blocks",
    "author": "WonkyGrub",
    "version": (0, 4),
    "blender": (4, 2, 0),
    "location": "File Menu > Save Unused Data Blocks Settings",
    "description": "Automatically or manually enable fake user for unused data blocks based on category selection",
    "warning": "",
    "category": "System"
}

import bpy
from bpy.props import BoolProperty
from bpy.app.handlers import persistent
from itertools import chain

def set_fake_users_in_data(datablock, action=True):
    for data in datablock:
        data.use_fake_user = action

# Handler function
@persistent
def auto_enable_fakeuser(dummy):
    print("Attempting to auto-enable fake users before save...")
    prefs = bpy.context.preferences.addons[__name__].preferences
    if not prefs.auto_save_enable:
        print("Auto-save feature is disabled in the preferences.")
        return

    actions = {
        "set_brush": bpy.data.brushes,
        "set_camera": bpy.data.cameras,
        "set_curve": bpy.data.curves,
        "set_font": bpy.data.fonts,
        "set_image": bpy.data.images,
        "set_light": bpy.data.lights,
        "set_lattice": bpy.data.lattices,
        "set_mask": bpy.data.masks,
        "set_material": bpy.data.materials,
        "set_mesh": bpy.data.meshes,
        "set_metaball": bpy.data.metaballs,
        "set_movieclip": bpy.data.movieclips,
        "set_node_group": bpy.data.node_groups,
        "set_object": bpy.data.objects,
        "set_particle": bpy.data.particles,
        "set_texture": bpy.data.textures,
        "set_world": bpy.data.worlds,
        # Add other data blocks here following the same pattern.
    }
    
    for attr, block in actions.items():
        if getattr(prefs, attr):
            print(f"Setting fake users for: {attr}")
            set_fake_users_in_data(block)

class FakeUserPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    # Definition of the auto_save_enable BooleanProperty
    auto_save_enable: BoolProperty(
        name="Enable Auto Save Fake User",
        description="Automatically adds a fake user to selected data types before saving",
        default=False
    )

    set_brush: BoolProperty(
        name="Brushes",
        description="Sets fake users for all brush data",
        default=False
    )

    set_camera: BoolProperty(
        name="Cameras",
        description="Sets fake users for all camera data",
        default=False
    )

    set_curve: BoolProperty(
        name="Curves",
        description="Sets fake users for all curve data",
        default=False
    )

    set_font: BoolProperty(
        name="Fonts",
        description="Sets fake users for all font data",
        default=False
    )

    set_image: BoolProperty(
        name="Images",
        description="Sets fake users for all image data",
        default=False
    )

    set_light: BoolProperty(
        name="Lights",
        description="Sets fake users for all light data",
        default=False
    )

    set_lattice: BoolProperty(
        name="Lattices",
        description="Sets fake users for all lattice data",
        default=False
    )

    set_mask: BoolProperty(
        name="Masks",
        description="Sets fake users for all mask data",
        default=False
    )

    set_material: BoolProperty(
        name="Materials",
        description="Sets fake users for all material data",
        default=False
    )

    set_mesh: BoolProperty(
        name="Meshes",
        description="Sets fake users for all mesh data",
        default=False
    )

    set_metaball: BoolProperty(
        name="Metaballs",
        description="Sets fake users for all metaball data",
        default=False
    )

    set_movieclip: BoolProperty(
        name="Movieclips",
        description="Sets fake users for all movieclip data",
        default=False
    )

    set_node_group: BoolProperty(
        name="Node Groups",
        description="Sets fake users for all node group data",
        default=False
    )

    set_object: BoolProperty(
        name="Objects",
        description="Sets fake users for all object data",
        default=False
    )

    set_particle: BoolProperty(
        name="Particles",
        description="Sets fake users for all particle data",
        default=False
    )

    set_texture: BoolProperty(
        name="Textures",
        description="Sets fake users for all texture data",
        default=False
    )

    set_world: BoolProperty(
        name="Worlds",
        description="Sets fake users for all world data",
        default=False
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "auto_save_enable")


        # Create a closed dropdown panel for data type selections
        box = layout.box()
        col = box.column()
        col.label(text="Data Types to Auto-Save:", icon='MODIFIER')
        col.prop(self, "set_brush", text="Brushes", toggle=False)
        col.prop(self, "set_camera", text="Cameras", toggle=False)
        col.prop(self, "set_curve", text="Curves", toggle=False)
        col.prop(self, "set_font", text="Fonts", toggle=False)
        col.prop(self, "set_image", text="Images", toggle=False)
        col.prop(self, "set_light", text="Lights", toggle=False)
        col.prop(self, "set_lattice", text="Lattices", toggle=False)
        col.prop(self, "set_mask", text="Masks", toggle=False)
        col.prop(self, "set_material", text="Materials", toggle=False)
        col.prop(self, "set_mesh", text="Meshes", toggle=False)
        col.prop(self, "set_metaball", text="Metaballs", toggle=False)
        col.prop(self, "set_movieclip", text="Movieclips", toggle=False)
        col.prop(self, "set_node_group", text="Node Groups", toggle=False)
        col.prop(self, "set_object", text="Objects", toggle=False)
        col.prop(self, "set_particle", text="Particles", toggle=False)
        col.prop(self, "set_texture", text="Textures", toggle=False)
        col.prop(self, "set_world", text="Worlds", toggle=False)
        # Draw other properties

class RAFU_OT_ApplyFakeUsersFromPreferences(bpy.types.Operator):
    """Apply fake users according to saved addon preferences"""
    bl_idname = "system.apply_fake_users_from_preferences"
    bl_label = "Apply Fake Users From Preferences"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Applying fake users according to preferences...")
        prefs = context.preferences.addons[__name__].preferences
        actions = {
            "set_brush": bpy.data.brushes,
            "set_camera": bpy.data.cameras,
            "set_curve": bpy.data.curves,
            "set_font": bpy.data.fonts,
            "set_image": bpy.data.images,
            "set_light": bpy.data.lights,
            "set_lattice": bpy.data.lattices,
            "set_mask": bpy.data.masks,
            "set_material": bpy.data.materials,
            "set_mesh": bpy.data.meshes,
            "set_metaball": bpy.data.metaballs,
            "set_movieclip": bpy.data.movieclips,
            "set_node_group": bpy.data.node_groups,
            "set_object": bpy.data.objects,
            "set_particle": bpy.data.particles,
            "set_texture": bpy.data.textures,
            "set_world": bpy.data.worlds,
            # Add other data blocks here following the same pattern.
        }
        
        for attr, block in actions.items():
            if getattr(prefs, attr):
                print(f"Manually setting fake users for: {attr}")
                set_fake_users_in_data(block)
        
        return {'FINISHED'}

class RAFU_OT_SetFakeUsersInteractive(bpy.types.Operator):
    """Interactively select data blocks to apply fake users"""
    bl_idname = "system.set_fake_users_interactive"
    bl_label = "Set Fake Users Interactively"
    bl_options = {'REGISTER', 'UNDO'}

    # Temporary properties, mirroring the ones in FakeUserPreferences but used for this operation only.
    set_brush: BoolProperty(name="Brushes", default=False)
    set_camera: BoolProperty(name="Cameras", default=False)
    set_curve: BoolProperty(name="Curves", default=False)
    set_font: BoolProperty(name="Fonts", default=False)
    set_image: BoolProperty(name="Images", default=False)
    set_light: BoolProperty(name="Lights", default=False)
    set_lattice: BoolProperty(name="Lattices", default=False)
    set_mask: BoolProperty(name="Masks", default=False)
    set_material: BoolProperty(name="Materials", default=False)
    set_mesh: BoolProperty(name="Meshes", default=False)
    set_metaball: BoolProperty(name="Metaballs", default=False)
    set_movieclip: BoolProperty(name="Movieclips", default=False)
    set_node_group: BoolProperty(name="Node Groups", default=False)
    set_object: BoolProperty(name="Objects", default=False)
    set_particle: BoolProperty(name="Particles", default=False)
    set_texture: BoolProperty(name="Textures", default=False)
    set_world: BoolProperty(name="Worlds", default=False)
    # Continue for eac data type...

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        # Logic to apply fake users based on the selections made in the dialog.
        actions = {
            "set_brush": bpy.data.brushes,
            "set_camera": bpy.data.cameras,
            "set_curve": bpy.data.curves,
            "set_font": bpy.data.fonts,
            "set_image": bpy.data.images,
            "set_light": bpy.data.lights,
            "set_lattice": bpy.data.lattices,
            "set_mask": bpy.data.masks,
            "set_material": bpy.data.materials,
            "set_mesh": bpy.data.meshes,
            "set_metaball": bpy.data.metaballs,
            "set_movieclip": bpy.data.movieclips,
            "set_node_group": bpy.data.node_groups,
            "set_object": bpy.data.objects,
            "set_particle": bpy.data.particles,
            "set_texture": bpy.data.textures,
            "set_world": bpy.data.worlds,
            # Continue for each data type...
        }

        for attr, block in actions.items():
            if getattr(self, attr):
                print(f"Interactively setting fake users for: {attr}")
                set_fake_users_in_data(block)

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(RAFU_OT_ApplyFakeUsersFromPreferences.bl_idname)
    self.layout.operator(RAFU_OT_SetFakeUsersInteractive.bl_idname)


def register():
    print("Registering Advanced Save Unused Data Blocks addon...")
    bpy.utils.register_class(FakeUserPreferences)
    bpy.utils.register_class(RAFU_OT_ApplyFakeUsersFromPreferences)  # Updated name
    bpy.utils.register_class(RAFU_OT_SetFakeUsersInteractive)  # New class
    bpy.types.TOPBAR_MT_file_external_data.append(menu_func)
    bpy.app.handlers.save_pre.append(auto_enable_fakeuser)

def unregister():
    print("Unregistering Advanced Save Unused Data Blocks addon...")
    bpy.types.TOPBAR_MT_file_external_data.remove(menu_func)
    bpy.utils.unregister_class(RAFU_OT_ApplyFakeUsersFromPreferences)  # Updated name
    bpy.utils.unregister_class(RAFU_OT_SetFakeUsersInteractive)  # New class
    bpy.utils.unregister_class(FakeUserPreferences)
    bpy.app.handlers.save_pre.remove(auto_enable_fakeuser)

if __name__ == "__main__":
    register()

