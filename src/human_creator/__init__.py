
import bpy
from .ui.main_panel import OBJECT_PT_human_creator_panel

classes = (
    OBJECT_PT_human_creator_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    print("Human Creator Extension Registered Successfully.")

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("Human Creator Extension Unregistered.")

if __name__ == "__main__":
    register()
