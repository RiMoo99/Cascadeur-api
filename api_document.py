# --------------------------------------------------------------------------------------------------------
# csc.Direction Class
# Represents a direction class used to handle directional operations within Cascadeur's system.

# Methods:
# inverse(self: csc.Direction) → csc.DirectionValue
#   Computes and returns the inverse of the current direction.

# to_string(self: csc.Direction) → str
#   Converts the direction object into its string representation.

# value(self: csc.Direction) → csc.DirectionValue
#   Retrieves the value of the direction.

def csc_Direction_example():
    import csc
    d = csc.Direction(csc.DirectionValue.In)
    print(d.value())

# --------------------------------------------------------------------------------------------------------
# csc.DirectionValue Class
# Represents a DirectionValue enumeration for defining In, Out, and Unknown directions.

# Members:
# In = <DirectionValue.In: 0>
# Out = <DirectionValue.Out: 1>
# Unknown = <DirectionValue.Unknown: 2>

# Properties:
# name → str
#   Gets and sets the name of the direction.
# value → int
#   Gets and sets the integer value of the direction.

def csc_DirectionValue_example():
    import csc
    print(csc.DirectionValue.In)
    print(csc.DirectionValue.In.value)

# --------------------------------------------------------------------------------------------------------
# csc.Guid Class
# Represents a globally unique identifier (GUID) within Cascadeur's system. Used to uniquely identify various objects, assets, or other entities in a scene.

# Methods:
# is_null(self: csc.Guid) → bool
#   Checks whether the GUID is null.

# static null() → csc.Guid
#   Returns a null GUID, which can be used to indicate the absence of a valid identifier.

# to_string(self: csc.Guid) → str
#   Converts the GUID into a string format, useful for logging or exporting data.

# Example usage:
# This script returns a null GUID, checks that the returned GUID is null and converts it to string
# import csc
#
def csc_Guid_example():
    # Create a new null GUID
    null_guid = csc.Guid.null()
    # Check if a GUID is null
    if null_guid.is_null():
        print("This is a null GUID.")
    # Create a new GUID and convert to string
    new_guid = csc.Guid()
    guid_string = new_guid.to_string()
    print(f"The GUID is: {guid_string}")


# --------------------------------------------------------------------------------------------------------
# csc.SystemVariables Class
# Contains static methods related to system variables of Cascadeur.

# Methods:
# static git_count() → str
#   Returns the git count of the current repository.

# static git_date() → str
#   Returns the git date of the current repository.

# static git_sha() → str
#   Returns the git SHA hash of the current repository.

# static git_version() → str
#   Returns the git version of the current repository.

def csc_SystemVariables_example():
    import csc
    print(csc.SystemVariables.git_sha())
    print(csc.SystemVariables.git_date())
    print(csc.SystemVariables.git_count())
    print(csc.SystemVariables.git_version())


# --------------------------------------------------------------------------------------------------------
# csc.Version Class
# Represents a version class used to define and manipulate versioning information.

# Properties:
# major → int
#   Gets and sets the major version number.
# minor → int
#   Gets and sets the minor version number.
# patch → int
#   Gets and sets the patch version number.

# Methods:
# to_string(self: csc.Version) → str
#   Converts the version object into a string representation.

# static from_string(arg0: str) → csc.Version
#   Creates a version object from a string representation.

def csc_Version_example():
    import csc
    version = csc.Version.from_string("4.2.1")
    print(version.major)
    print(version.minor)
    print(version.patch)
    print(version.to_string())


# --------------------------------------------------------------------------------------------------------
# csc.tools.AttractorTool Class
# Represents the attractor tool class used in Cascadeur's toolset.

# Methods:
# get_general_settings(self: csc.tools.AttractorTool) → csc.tools.attractor.AttractorGeneralSettings
#   Retrieves the general settings of the attractor tool.

# is_only_key_frames(self: csc.tools.AttractorTool) → bool
#   Checks if the attractor tool is only operating on key frames.

def csc_AttractorTool_example():
    import csc
    scene_manager = csc.app.get_application().get_scene_manager()
    app_scene = scene_manager.current_scene()
    attractor_tool = csc.app.get_application().get_tools_manager().get_tool('AttractorTool').editor(app_scene)
    print(attractor_tool.is_only_key_frames())

# ---------------------------------------------------------------------------------------------------------
# csc.tools.AutoPhysicTool Class
# Represents the auto physics tool class used to handle automatic physics in Cascadeur.

# Methods:
# turn_off(self: csc.tools.AutoPhysicTool) → None
#   Turns off the auto physics tool.

# turn_off_all_fulcrum_points(self: csc.tools.AutoPhysicTool) → None
# 

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.MirrorTool Class
# Represents the mirror tool class used to handle symmetry operations in Cascadeur.

# Methods:
# core(self: csc.tools.MirrorTool) → csc.tools.mirror.Core
#   Returns the core object of the mirror tool.

def csc_MirrorTool_example():
    import csc
    scene_manager:csc.view.Scene = csc.app.get_application().get_scene_manager()
    app_scene = scene_manager.current_scene()
    mirror_tool = csc.app.get_application().get_tools_manager().get_tool('MirrorTool').editor(app_scene)
    core = mirror_tool.core()
    core.set_plane(csc.math.Plane([1.0, 0.0, 0.0], [0.0,0.0,0.0]))

# ---------------------------------------------------------------------------------------------------------
# csc.tools.mirror.Core Class
# Provides core functionalities for mirroring operations within Cascadeur.

# Methods:
# mirror_frame(self: csc.tools.mirror.Core, arg0: Set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]]) → None
#   Mirrors a frame based on the specified set of object IDs.
# mirror_interval(self: csc.tools.mirror.Core, arg0: Set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]]) → None
#   Mirrors an interval based on the specified set of object IDs.
# plane(self: csc.tools.mirror.Core) → csc.math.Plane
#   Retrieves the mirror plane.
# set_plane(self: csc.tools.mirror.Core, plane: csc.math.Plane) → None
#   Sets the mirror plane to the specified plane.

def csc_mirror_Core_example():
    import csc
    scene_manager:csc.view.Scene = csc.app.get_application().get_scene_manager()
    app_scene = scene_manager.current_scene()
    mirror_tool = csc.app.get_application().get_tools_manager().get_tool('MirrorTool').editor(app_scene)
    core = mirror_tool.core()
    core.set_plane(csc.math.Plane([1.0, 0.0, 0.0], [0.0,0.0,0.0]))

# ---------------------------------------------------------------------------------------------------------
# csc.tools.DataKey Class
# Represents a data key used for identifying data points within Cascadeur's system.

# Properties:
# data_name → str
#   Gets and sets the name of the data key.
# object_key → object
#   Gets and sets the key of the associated object.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.RiggingModeTool Class
# A tool class that provides functionality to manage rigging modes, including erasing and setting joint data, layer IDs, and preserved data.

# Methods:
# erase_joints_data(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session) → None
#   Erases joint data from the specified session.

# erase_layers_ids(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session) → None
#   Erases layer IDs from the specified session.

# erase_preserved_data(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session) → None
#   Erases preserved data from the specified session.

# get_joints_data(self: csc.tools.RiggingModeTool) → Dict[csc.model.ObjectId, List[csc.tools.JointData]]
#   Retrieves joint data mapped by object ID.

# get_layers_ids(self: csc.tools.RiggingModeTool) → Set[csc.model.LayerId]
#   Retrieves layer IDs as a set of GUIDs.

# get_preserved_data(self: csc.tools.RiggingModeTool) → Dict[csc.tools.DataKey, List[Union[bool, int, float, numpy.ndarray, csc.math.Rotation, csc.math.Quaternion, str]]]
#   Retrieves preserved data stored in a dictionary structure.

# get_preserved_setting(self:csc.tools.RiggingModeTool) → Dict[csc.tools.DataKey, List[Union[bool, int]]]
#   Retrieves preserved setting stored in a dictionary structure.

# erase_preserved_setting

# set_preserved_setting(self:csc.tools.RiggingModeTool,arg0: csc.domain.Session, arg1:Dict[csc.tools.DataKey, List[Union[bool, int]]]) → None
#   Sets preserved setting for the specified session.

# set_joints_data(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session, arg1: Dict[csc.model.ObjectId, List[csc.tools.JointData]]) → None
#   Sets joint data for the specified session.

# set_layers_ids(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session, arg1: Set[csc.Guid]) → None
#   Sets layer IDs for the specified session.

# set_preserved_data(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session, arg1: Dict[csc.tools.DataKey, List[Union[bool, int, float, numpy.ndarray, csc.math.Rotation, csc.math.Quaternion, str]]]) → None
#   Sets preserved data for the specified session.

# set_undo_redo_context(self: csc.tools.RiggingModeTool, arg0: csc.domain.Session, arg1: function, arg2: object, arg3: object) → None
#   Sets the undo/redo context for the specified session.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.JointData Class
# Represents joint data used in Cascadeur to manage local position, rotation, and scale of joints.

# Properties:
# local_position:numpy.ndarray
#   Gets and sets the local position of the joint.
# local_rotation:csc.math.Rotation
#   Gets and sets the local rotation of the joint.
# local_scale:numpy.ndarray
#   Gets and sets the local scale of the joint.
#  visibility : int

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.ObjectKey Class
# Represents an object key used in Cascadeur's tools for identifying and working with specific objects.

# Properties:
# behaviour_name → str
#   Gets the name of the behavior associated with the object key.
# path_name → str
#   Gets the path name related to the object key.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.SelectionGroups Class
# Represents a selection group tool for managing and organizing object selections.

# Methods:
# core(self: csc.tools.SelectionGroups) → object
#   Retrieves the core object associated with selection groups.

# import_file(self:csc.tools.SelectionGroups,str) → None

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.selection.Core Class
# A core class used within selection tools to manage groups and processing modes.

# Methods:
# get_group(self: csc.tools.selection.Core, idx: int) → csc.tools.selection.Group
#   Retrieves a specific group by index.
# get_groups(self: csc.tools.selection.Core) → Dict[int, csc.tools.selection.Group]
#   Retrieves all groups as a dictionary indexed by integers.
# process(self: csc.tools.selection.Core, index: int, mode: csc.tools.selection.Mode) → None
#   Processes the given index with a specified selection mode.
# set_group(self: csc.tools.selection.Core, index: int, group: csc.tools.selection.Group) → None
#   Sets a group for a specified index.
# set_groups(self: csc.tools.selection.Core, groups: Dict[int, csc.tools.selection.Group]) → None
#   Sets multiple groups based on a dictionary of index-to-group mappings.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.selection.Group Class
# Represents a selection group that contains objects and a pivot point.

# Properties:
# objects → Set[ModelObjectId]
#   Gets the set of object IDs within the group.
# pivot → ModelObjectId
#   Gets the pivot point of the group.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.selection.Mode Class
# Enumeration for defining different selection modes.

# Members:
# SetGroup = <Mode.SetGroup: 0>
# SingleSelect = <Mode.SingleSelect: 1>
# MultiSelect = <Mode.MultiSelect: 2>

# Properties:
# name → str
#   Gets the name of the selection mode.
# value → int
#   Gets the integer value associated with the selection mode.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.Args Class
# Arguments for configuring attractor operations.

# Properties:
# for_interval → bool
#   Gets or sets whether the attractor applies to an interval.
# general_settings → csc.tools.attractor.AttractorGeneralSettings
#   Gets the general settings for the attractor.
# mode → csc.tools.attractor.ArgsMode
#   Gets or sets the mode of the attractor.
# only_key_frames → bool
#   Gets or sets whether the attractor operates only on keyframes.

def csc_AttractorArgs_example():
    import csc
    scene_manager:csc.view.Scene = csc.app.get_application().get_scene_manager()
    app_scene = scene_manager.current_scene()
    scene = app_scene.domain_scene()
    attractor_tool = csc.app.get_application().get_tools_manager().get_tool('AttractorTool').editor(app_scene)
    settings = attractor_tool.get_general_settings()
    args = csc.tools.attractor.Args(scene, 
                                    app_scene.gravity_per_frame(), 
                                    settings,
                                    attractor_tool.is_only_key_frames(), 
                                    csc.tools.attractor.ArgsMode.Next)

# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.ArgsMode Class
# Enumeration defining the different attractor modes.

# Members:
# Previous = <ArgsMode.Previous: 0>
# Next = <ArgsMode.Next: 1>
# Inertial = <ArgsMode.Inertial: 2>
# InverseInertial = <ArgsMode.InverseInertial: 3>
# Average = <ArgsMode.Average: 4>
# Interpolation = <ArgsMode.Interpolation: 5>

# Properties:
# name → str
#   Gets the name of the attractor mode.
# value → int
#   Gets the integer value associated with the attractor mode.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.AttractorGeneralSettings Class
# General settings for configuring attractor behavior.

# Properties:
# factor → float
#   Gets or sets the factor for the attractor.
# mode → csc.tools.attractor.ArgsMode
#   Gets or sets the mode for the attractor.
# mode_relative_to_pivot → bool
#   Gets or sets whether the mode is relative to the pivot.
# physic_type → str
#   Gets or sets the physics type of the attractor.
# position_axis → str
#   Gets or sets the position axis of the attractor.
# rotation_axis → str
#   Gets or sets the rotation axis of the attractor.
# scale_axis → str
#   Gets or sets the scale axis of the attractor.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.GSAxisFlag Class
# Represents the GeneralSettings::RotationAxis enum used in the attractor tools within the Cascadeur software.

# Members:
# X = <GSAxisFlag.X: 1>
# Y = <GSAxisFlag.Y: 2>
# Z = <GSAxisFlag.Z: 4>
# XYZ = <GSAxisFlag.XYZ: 7>
# None = <GSAxisFlag.None: 0>

# Example usage:
# Empty space here


# csc.tools.attractor.GSAxisIndex Class
# Represents the GeneralSettings::RotationAxis enum with specific indices used in the attractor tools.

# Members:
# X = <GSAxisIndex.X: 0>
# Y = <GSAxisIndex.Y: 1>
# Z = <GSAxisIndex.Z: 2>

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.GSPhysicsType Class
# Represents the GeneralSettings::PhysicsType enum used in the attractor tools for different relaxation settings.

# Members:
# FrameRelax = <GSPhysicsType.FrameRelax: 0>
# InterpolationRelax = <GSPhysicsType.InterpolationRelax: 1>

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.GSRotationAxis Class
# Represents the GeneralSettings::RotationAxis enum used for rotation settings in the attractor tools.

# Members:
# X = <GSRotationAxis.X: 0>
# Y = <GSRotationAxis.Y: 1>
# Z = <GSRotationAxis.Z: 2>
# Whole = <GSRotationAxis.Whole: 3>
# None = <GSRotationAxis.None: 4>

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.tools.attractor.SpaceMode Class
# Represents the attractor::Mode enum to define the space modes for attractor tools.

# Members:
# Global = <SpaceMode.Global: 0>
# Local = <SpaceMode.Local: 1>

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.view.Camera Class
# Represents a spherical camera class in the view domain.

# Methods:
# set_target(self: csc.view.Camera, arg0: numpy.ndarray[numpy.float32[3,1]]) → None
#   Sets the camera target to a specified point.

# zoom_to_points(self: csc.view.Camera, arg0: List[numpy.ndarray[numpy.float32[3,1]]]) → None
#   Zooms the camera to include the specified list of points.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.view.CameraType Class
# Represents the camera::CameraType enumeration for different camera types.

# Members:
# ISOMETRIC = <CameraType.ISOMETRIC: 0>
# PERSPECTIVE = <CameraType.PERSPECTIVE: 1>

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.view.DialogButton Class
# Represents a button in a dialog interface within the view domain.

# Methods:
# force_active_focus(self: csc.view.DialogButton) → bool
#   Returns whether the button should force active focus.

# text(self: csc.view.DialogButton) → str
#   Gets the text of the button.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.view.DialogManager Class
# Represents a manager for handling dialog interactions in the view domain.

# Methods:
# static instance() → object
#   Returns the singleton instance of the DialogManager.

# show_buttons_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: List[csc.view.DialogButton]) → None
#   Displays a dialog with a list of buttons.

# show_info(self: csc.view.DialogManager, arg0: str, arg1: str) → None
#   Displays an informational dialog.

# show_input_dialog(self: csc.view.DialogManager, arg0: str, arg1: str, arg2: str, arg3: function) → None
#   Shows an input dialog with a single handler function.

def csc_DialogManager_example():
    # This script showcases the use of DialogManager
    import csc

    def run(scene):
        def callback_button():
            def input_callback(input_values):
                values = ''.join(input_values)
                csc.view.DialogManager.instance().show_info("Input values", values)

            input_field_count = 5
            input_field_names = ["f1", "f2", "f3"]
            input_field_fills = ["v1", "v2", "v3", "v4"]
            csc.view.DialogManager.instance().show_inputs_dialog("Test1", input_field_names, input_field_fills,
                                                                input_field_count, input_callback)

        dialog_buttons = [csc.view.DialogButton('ButtonName', callback_button),
                        csc.view.DialogButton(csc.view.StandardButton.Cancel)]

        csc.view.DialogManager.instance().show_buttons_dialog("Test dialog window", "Press anything", dialog_buttons)

# ---------------------------------------------------------------------------------------------------------
# csc.view.FileDialogManager Class
# Represents a manager for handling file dialog interactions.

# Methods:
# show_folder_dialog(self: csc.view.FileDialogManager, arg0: str, arg1: function) → None
#   Shows a dialog for selecting a folder.

# show_save_file_dialog(self: csc.view.FileDialogManager, title: str, path: str, filters: List[str], handler: function) → None
#   Shows a dialog for saving a file with the given parameters.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.view.Scene Class
# Represents the SceneView class used within Cascadeur's system to handle various aspects of scene management and visualization.

# Methods:
# domain_scene(self: csc.view.Scene) → object
#   Returns the domain scene associated with this view.

# event_log(self: csc.view.Scene) → object
#   Retrieves the event log for the scene.

# gravity_per_frame(self: csc.view.Scene) → float
#   Gets the gravity value applied per frame within the scene.

# save(self: csc.view.Scene, path_name: str) → bool
#   Saves the current scene to the specified path.

# set_left_bar_visible(self: csc.view.Scene, enable: bool) → None
#   Sets the visibility of the left bar in the scene.

# view_ports(self: csc.view.Scene) → List[object]
#   Retrieves the list of view ports available in the scene.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.view.SphericalCameraStruct Class
# Represents a SphericalCameraStruct that defines the properties of a spherical camera in the scene.

# Members:
# target → Vector3f
#   Gets or sets the target position of the camera.

# position → Vector3f
#   Gets or sets the position of the camera.

# type → CameraType
#   Gets or sets the camera type.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.view.StandardButton Class
# Represents the StandardButton enumeration, which defines the basic types of standard buttons such as Ok, Cancel, Yes, and No.

# Members:
# Ok = <StandardButton.Ok: 0>
#   Represents the OK button.

# Cancel = <StandardButton.Cancel: 1>
#   Represents the Cancel button.

# Yes = <StandardButton.Yes: 2>
#   Represents the Yes button.

# No = <StandardButton.No: 3>
#   Represents the No button.

# Properties:
# name → str
#   Gets or sets the name of the button.

# value → int
#   Gets or sets the value of the button.

def csc_StandardButton_example():
    # This script showcases the use of StandardButton in a dialog
    import csc
    def run(scene):
        dialog_buttons = [csc.view.DialogButton(csc.view.StandardButton.Ok, lambda: scene.success('Pressed Ok')),
                        csc.view.DialogButton(csc.view.StandardButton.Yes, lambda: scene.success('Pressed Yes')),
                        csc.view.DialogButton(csc.view.StandardButton.No, lambda: scene.success('Pressed No')),
                        csc.view.DialogButton(csc.view.StandardButton.Cancel, lambda: scene.success('Pressed Cancel'))]
        csc.view.DialogManager.instance().show_buttons_dialog("Test dialog window", "Press anything", dialog_buttons)


# ---------------------------------------------------------------------------------------------------------
# csc.view.ViewPort Class
# Represents the ViewPort class used to handle specific viewport functionality in the Cascadeur environment.

# Methods:
# domain_viewport(self: csc.view.ViewPort) → csc.view.ViewPortDomain
#   Returns the domain view port associated with this view port.

def csc_ViewPort_example():
    # import csc

    def run(scene):
        application = csc.app.get_application()
        cs = application.current_scene()
        active_viewport = cs.active_viewport().domain_viewport()
        print(f"Active viewport: {active_viewport.id}")


# ---------------------------------------------------------------------------------------------------------
# csc.view.ViewPortDomain Class
# Represents the Domain ViewPort class that manages properties and functionalities of a viewport in the scene.

# Methods:
# camera(self: csc.view.ViewPortDomain) → object
#   Returns the camera associated with this viewport domain.

# camera_struct(self: csc.view.ViewPortDomain) → csc.view.SphericalCameraStruct
#   Returns the spherical camera structure associated with this viewport.

# id(self: csc.view.ViewPortDomain) → csc.Guid
#   Retrieves the GUID associated with this viewport domain.

# mode_visualizers(self: csc.view.ViewPortDomain) → int
#   Gets or sets the mode visualizers for this viewport.

# set_camera_struct(self: csc.view.ViewPortDomain, camera_struct: csc.view.SphericalCameraStruct) → None
#   Sets the camera structure for this viewport domain.

# set_mode_visualizers(self: csc.view.ViewPortDomain, mode: int) → None
#   Sets the mode visualizers for this viewport domain.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.app.ActionManager Class
# Represents the ActionManager class that handles actions within the Cascadeur application.

# Methods:
# call_action(self: csc.app.ActionManager, arg0: str) → None
#   Calls a specified action by name.

def csc_ActionManager_example():
    # This script calls the specified action
    import csc
    def run(scene):
        mp = csc.app.get_application()
        mp.get_action_manager().call_action("Scene.Undo")


# ---------------------------------------------------------------------------------------------------------
# csc.app.Analitics Class
# Represents the Analitics class used for sending analytical data within Cascadeur.

# Methods:
# static send_action(type: str, key: str = '', label: str = '') → None
#   Sends an action to the analytical system with the specified type, key, and label.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.app.Application Class
# Represents the Application class that serves as the central point for accessing various managers and scene-related operations.

# Methods:
# current_scene(self: csc.app.Application) → object
#   Returns the currently active scene in the application.

# get_action_manager(self: csc.app.Application) → object
#   Returns the ActionManager instance associated with this application.

# get_data_source_manager(self: csc.app.Application) → object
#   Returns the DataSourceManager instance for managing scenes and data sources.

# get_file_dialog_manager(self: csc.app.Application) → object
#   Returns the FileDialogManager instance for handling file dialog operations.

# get_scene_clipboard(self: csc.app.Application) → object
#   Returns the SceneClipboard instance associated with this application.

# get_scene_manager(self: csc.app.Application) → object
#   Returns the SceneManager instance for managing scenes.

# get_setting_manager(self: csc.app.Application) → object
#   Returns the SettingManager instance for accessing and modifying settings.

# get_tools_manager(self: csc.app.Application) → object
#   Returns the ToolsManager instance for accessing tools in the application.

def csc_Application_example():
    # This script showcases the initialization of various managers of the csc.app.Application class
    import csc
    def run(scene):
        app = csc.app.get_application()
        current_scene = app.current_scene()
        am = app.get_action_manager()
        dsm = app.get_data_source_manager()
        fdm = app.get_file_dialog_manager()
        s_cb = app.get_scene_clipboard()
        scene_manager = app.get_scene_manager()
        setting_manager = app.get_setting_manager()
        tools_manager = app.get_tools_manager()


# ---------------------------------------------------------------------------------------------------------
# csc.app.CascadeurTool Class
# Represents the CascadeurTool class for managing tools and editor functionality in Cascadeur.

# Methods:
# editor(self: csc.app.CascadeurTool, arg0: csc.view.Scene) → csc.app.SceneTool
#   Retrieves the editor associated with a given scene.

# name(self: csc.app.CascadeurTool) → str
#   Gets the name of the Cascadeur tool.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.app.DataSourceManager Class
# Represents the DataSourceManager class used for managing data sources and scenes within the application.

# Methods:
# close_scene(self: csc.app.DataSourceManager, scene: csc.view.Scene) → None
#   Closes the specified scene.

# load_scene(self: csc.app.DataSourceManager, file_name: str) → bool
#   Loads a scene from the specified file.

# save_current_scene(self: csc.app.DataSourceManager) → None
#   Saves the current scene.

# save_scene(self: csc.app.DataSourceManager, scene_view: csc.view.Scene) → None
#   Saves the specified scene view.

# save_scene_as(self: csc.app.DataSourceManager, scene_view: csc.view.Scene, full_file_name: str) → None
#   Saves the specified scene view under a new file name.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.app.EventLog Class
# EventLog class represents a log for application events.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.app.ProjectLoader Class
# ProjectLoader class provides methods to load domain scenes.

# Methods:
# static load_from(arg0: str, arg1: csc.domain.Scene) → None
#   Loads a scene from the specified source.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.app.SceneManager Class
# SceneManager class provides functionalities to manage scenes within the application.

# Methods:
# create_application_scene(self: csc.app.SceneManager) → object
#   Creates and returns a new application scene.

# current_scene(self: csc.app.SceneManager) → object
#   Returns the current active scene.

# remove_application_scene(self: csc.app.SceneManager, arg0: csc.view.Scene) → None
#   Removes the specified application scene.

# scenes(self: csc.app.SceneManager) → List[object]
#   Returns a list of all available scenes.

# set_current_scene(self: csc.app.SceneManager, arg0: csc.view.Scene) → None
#   Sets the specified scene as the current active scene.

def csc_SceneManager_example(scene):
    # This script showcases the use of methods in the csc.app.SceneManager class
    import csc
    app = csc.app.get_application()
    scene_manager = app.get_scene_manager()
    # Get scene in the currently opened tab
    current_scene = scene_manager.current_scene()
    # Open new scene tab
    new_scene = scene_manager.create_application_scene()
    # Set the specified scene tab as active
    scene_manager.set_current_scene(new_scene)
    # Get a list of all scene tabs
    scenes = scene_manager.scenes()
    print(len(scenes))
    # Close specified scene tab
    scene_manager.remove_application_scene(current_scene)



# ---------------------------------------------------------------------------------------------------------
# csc.app.SceneTool Class
# SceneTool class provides utility methods and properties to work with scenes.

# Example usage:
# Empty space here


# csc.app.SettingsManager Class
# SettingsManager class provides methods to get various settings values.

# Methods:
# get_color_value(self: csc.app.SettingsManager, arg0: str) → numpy.ndarray[numpy.float32[3,1]]
#   Returns a color value based on the specified key.

# get_float_value(self: csc.app.SettingsManager, arg0: str) → float
#   Returns a float value based on the specified key.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.app.ToolsManager Class
# ToolsManager class provides access to various tools within the application.

# Methods:
# get_tool(self: csc.app.ToolsManager, arg0: str) → object
#   Returns the specified tool based on its name.

def csc_ToolsManager_example():
    # This script gets the FbxSceneLoader tool
    import csc
    def run(scene):
        app = csc.app.get_application()
        tools_manager = app.get_tools_manager()
        # Get specified tool object
        tools_manager.get_tool("FbxSceneLoader")


# ---------------------------------------------------------------------------------------------------------
# csc.app.get_application Function
# get_application() → csc.app.Application
#   Returns the current application instance.

def csc_get_application_example():
    # This script gets the current app instance
    import csc
    def run(scene):
        app = csc.app.get_application()


# ---------------------------------------------------------------------------------------------------------
# csc.parts.Buffer Class
# Buffer class provides methods to operate parts of the scene.

# Methods:
# static get(source_dir: str = '') → object
#   Retrieves a buffer object from the specified source directory.

# insert_elementary_by_id(self: csc.parts.Buffer, arg0: csc.model.ObjectId, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor) → csc.parts.GroupInfo
#   Inserts an elementary object into the buffer by its ID.

# insert_elementary_by_path(self: csc.parts.Buffer, arg0: str, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor) → csc.parts.GroupInfo
#   Inserts an elementary object into the buffer by its path.

# insert_object_by_id(self: csc.parts.Buffer, arg0: csc.model.ObjectId, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor, arg3: csc.domain.assets.AssetsManager) → csc.model.ObjectId
#   Inserts an object into the buffer by its ID.

# insert_object_by_path(self: csc.parts.Buffer, arg0: str, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor, arg3: csc.domain.assets.AssetsManager) → csc.model.ObjectId
#   Inserts an object into the buffer by its path.

# insert_objects_by_id(self: csc.parts.Buffer, arg0: csc.model.ObjectId, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor, arg3: csc.domain.assets.AssetsManager) → Tuple[Set[csc.model.ObjectId], Set[csc.update.GroupId]]
#   Inserts multiple objects into the buffer by their IDs.

# insert_objects_by_path(self: csc.parts.Buffer, arg0: str, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor, arg3: csc.domain.assets.AssetsManager) → Tuple[Set[csc.model.ObjectId], Set[csc.update.GroupId]]
#   Inserts multiple objects into the buffer by their paths.

# insert_selected_objects_by_path(self: csc.parts.Buffer, arg0: str, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor, arg3: csc.domain.assets.AssetsManager) → Set[csc.model.ObjectId]
#   Inserts selected objects into the buffer by their paths.

# insert_update_group_by_id(self: csc.parts.Buffer, arg0: csc.model.ObjectId, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor) → Tuple[csc.parts.GroupInfo, Dict[csc.update.GroupId, csc.parts.GroupInfo]]
#   Inserts an update group into the buffer by its ID.

# insert_update_group_by_path(self: csc.parts.Buffer, arg0: str, arg1: csc.update.GroupId, arg2: csc.model.ModelEditor) → Tuple[csc.parts.GroupInfo, Dict[csc.update.GroupId, csc.parts.GroupInfo]]
#   Inserts an update group into the buffer by its path.

# refresh(self: csc.parts.Buffer) → None
#   Refreshes the buffer.


def csc_Buffer_example():
    # This script inserts the 'Locator' object from the "parts" folder in Cascadeur's main directory, into the scene
    import csc
    def run(scene):
        def mod(model, update, scene_updater):
            new_obj_id = csc.parts.Buffer.get().insert_object_by_path('objects/locator.casc', update.root().group_id(),
                                                                    model, scene.assets_manager())
            scene_updater.generate_update()
            print(f'Added parts object Locator with Id {new_obj_id}')
        scene.modify_update("Insert object by path", mod)


# ---------------------------------------------------------------------------------------------------------
# csc.parts.GroupInfo Class
# GroupInfo class represents group information within the scene buffer.

# Properties:
# datas -> List
#   Gets and sets the data property of the group.
# regular_funcs -> List
#   Gets and sets the regular functions of the group.
# settings -> List
#   Gets and sets the settings of the group.
# settings_funcs -> List
#   Gets and sets the settings functions of the group.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.parts.Info Class
# Info class represents the basic information of parts within the scene.

# Properties:
# name -> str
#   Gets and sets the name of the part.
# object_id -> csc.model.ObjectId
#   Gets and sets the object ID of the part.
# path -> str
#   Gets and sets the path of the part.
# type -> csc.parts.Type
#   Gets and sets the type of the part.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.parts.SceneClipboard Class
# SceneClipboard class provides methods to operate parts of the scene.

# Methods:
# copy(self: csc.parts.SceneClipboard, arg0: csc.view.Scene) → None
#   Copies the specified scene to the clipboard.

# copy_image_to_clipboard(self: csc.parts.SceneClipboard, arg0: csc.view.Scene) → None
#   Copies an image of the specified scene to the clipboard.

# paste(self: csc.parts.SceneClipboard, arg0: csc.view.Scene) → None
#   Pastes the contents of the clipboard into the specified scene.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.parts.Type Class
# Type of the parts, enum
#
# - Elementary: includes only regular and setting functions, regular and setting data, and connections that link them.
# - UpdateGroup: sub update groups and their elementary entities, along with the connections that link them.
# - Object: includes all related entities of some object.
# - ObjectGroup: includes all objects and sub object groups, as well as all related entities.
# - SelectedObjects: selected objects from different groups.
#
# Members:
# - Elementary = <Type.Elementary: 0>
# - UpdateGroup = <Type.UpdateGroup: 1>
# - Object = <Type.Object: 2>
# - ObjectGroup = <Type.ObjectGroup: 3>
# - SelectedObjects = <Type.SelectedObjects: 4>
#
# Properties:
# - name → str
#   Gets the name of the type.
# - value → int
#   Gets the value of the type.
#
# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.external.fbx.ExtraDatas Class
# ExtraDatas class for storing additional FBX node information.
#
# Properties:
# - look → Any
#   Contains the look property of the FBX node.
# - node_index → int
#   Contains the node index of the FBX element.
# - post_rotation → Any
#   Contains the post rotation values of the FBX node.
# - pre_rotation → Any
#   Contains the pre rotation values of the FBX node.
# - size → Any
#   Contains the size information of the FBX node.
#
# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.external.fbx.FbxDatas Class
# FbxDatas class for storing FBX data configurations.
#
# Properties:
# - ignore_namespace → bool
#   Determines if namespace should be ignored during FBX operations.
# - order → Any
#   Defines the order of FBX processing.
# - rotation → Any
#   Stores rotation data for FBX operations.
# - scale → Any
#   Contains scale data for FBX operations.
# - translation → Any
#   Contains translation data for FBX operations.
#
# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.fbx.FbxLoader Class
# FbxLoader class for managing the import and export of FBX files within the system.
#
# Methods:
# - add_model(self: csc.fbx.FbxLoader, file_name: str) → None
#   Adds an FBX model to the scene using the given file name.
# - add_model_to_selected(self: csc.fbx.FbxLoader, file_name: str) → None
#   Adds an FBX model to the selected objects using the given file name.
# - export_all_objects(self: csc.fbx.FbxLoader, file_name: str) → None
#   Exports all objects in the scene to an FBX file.
# - export_joints(self: csc.fbx.FbxLoader, file_name: str) → None
#   Exports only the joint information to an FBX file.
# - export_model(self: csc.fbx.FbxLoader, file_name: str) → None
#   Exports the model to an FBX file.
# - export_scene_selected(self: csc.fbx.FbxLoader, file_name: str) → None
#   Exports the currently selected scene elements to an FBX file.
# - import_animation(self: csc.fbx.FbxLoader, file_name: str) → None
#   Imports animation data from an FBX file.
# - import_animation_to_selected_frames(self: csc.fbx.FbxLoader, file_name: str) → None
#   Imports animation data into selected frames.
# - import_animation_to_selected_objects(self: csc.fbx.FbxLoader, file_name: str) → None
#   Imports animation data into selected objects.
# - import_model(self: csc.fbx.FbxLoader, file_name: str) → None
#   Imports a model from an FBX file.
# - import_scene(self: csc.fbx.FbxLoader, file_name: str) → None
#   Imports an entire scene from an FBX file.
# - set_settings(self: csc.fbx.FbxLoader, settings: csc.fbx.FbxSettings) → None
#   Sets the configuration settings for the FBX loader.
#
def csc_FbxLoader_example():
# This script imports a specified FBX file into the current scene
    import csc
    def run(scene):
        app = csc.app.get_application()
        def import_scene(folder_path: str):
            file_ = folder_path.replace('\\', '/')
            scene_manager = app.get_scene_manager()
            tools_manager = app.get_tools_manager()
            # Get current scene tab
            current_scene = scene_manager.current_scene()
            # Get FbxSceneLoader tool
            fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
            # Get FbxLoader
            fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)
            # Import fbx file as a scene
            fbx_scene_loader.import_scene(file_)
        app.get_file_dialog_manager().show_open_file_dialog("Select .fbx file", "", ["*.fbx"], import_scene)

def csc_FbxLoader_example2():
    # This script imports animation data from the specified FBX file
    import csc
    def run(scene):
        app = csc.app.get_application()
        def import_animation(folder_path: str):
            file_ = folder_path.replace('\\', '/')
            scene_manager = app.get_scene_manager()
            tools_manager = app.get_tools_manager()
            # Get current scene tab
            current_scene = scene_manager.current_scene()
            # Get FbxSceneLoader tool
            fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
            # Get FbxLoader
            fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)
            # Import fbx file as a scene
            fbx_scene_loader.import_animation(file_)
        app.get_file_dialog_manager().show_open_file_dialog("Select .fbx file", "", ["*.fbx"], import_animation)

def csc_FbxLoader_example3():
    # This script exports the current scene as FBX file
    import csc
    def run(scene):
        app = csc.app.get_application()
        fd_m = app.get_file_dialog_manager()
        def export_scene(file_name):
            scene_manager = app.get_scene_manager()
            tools_manager = app.get_tools_manager()
            # Get current scene tab
            current_scene = scene_manager.current_scene()
            fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
            fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)
            # Export all exportable objects in the scene as FBX
            fbx_scene_loader.export_all_objects(file_name)
        fd_m.show_save_file_dialog("Choose filename fbx", "", ["*.fbx"], export_scene)


# ---------------------------------------------------------------------------------------------------------
# csc.fbx.FbxSceneLoader Class
# FbxSceneLoader class for managing entire FBX scenes.
#
# Methods:
# - export_fbx_scene(self: csc.fbx.FbxSceneLoader, scene: csc.view.Scene, file_name: str) → None
#   Exports the entire scene as an FBX file.
# - get_fbx_loader(self: csc.fbx.FbxSceneLoader, scene: csc.view.Scene) → csc.fbx.FbxLoader
#   Gets the FBX loader associated with a specific scene.
# - import_fbx_animation(self: csc.fbx.FbxSceneLoader, scene: csc.view.Scene, file_name: str) → None
#   Imports animation data into the specified scene.
# - import_fbx_scene(self: csc.fbx.FbxSceneLoader, scene: csc.view.Scene, file_name: str) → None
#   Imports an entire FBX scene.
#
def csc_FbxSceneLoader_example():
    # This script gets the FbxLoader in the specified scene
    import csc

    def run(scene):
        app = csc.app.get_application()
        scene_manager = app.get_scene_manager()
        tools_manager = app.get_tools_manager()
        # Get current scene tab
        current_scene = scene_manager.current_scene()
        # Get FbxSceneLoader tool
        fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
        # Get FbxLoader
        fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)


# csc.fbx.FbxSettings Class
# FbxSettings class for configuring FBX import/export options.
#
# Properties:
# - apply_euler_filter → bool
#   Determines if the Euler filter should be applied during FBX operations.
# - bake_animation → bool
#   Determines if animations should be baked during export.
# - export_selected_interval → Any
#   Sets the interval for exporting selected elements.
# - mode → csc.fbx.FbxSettingsMode
#   Sets the mode for FBX export (Binary or Ascii).
# - up_axis → csc.fbx.FbxSettingsAxis
#   Defines the up axis for the exported FBX file.
#
def csc_FbxSettings_example():
    # This script uses custom FBX settings for scene export
    import csc
    from csc import fbx
    def run(scene):
        app = csc.app.get_application()
        fd_m = app.get_file_dialog_manager()
        def export_scene(file_name):
            # Initialize FbxSettings
            settings = fbx.FbxSettings()
            # Set the Fbx type - Ascii or Binary
            settings.mode = fbx.FbxSettingsMode.Ascii
            # Turn on or off the euler filter being applied on the exported animation
            settings.apply_euler_filter = False
            # Set up the up axis (X, Y or Z)
            settings.up_axis = fbx.FbxSettingsAxis.Y
            scene_manager = app.get_scene_manager()
            tools_manager = app.get_tools_manager()
            current_scene = scene_manager.current_scene()
            fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
            fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)
            fbx_scene_loader.set_settings(settings)
            fbx_scene_loader.export_all_objects(file_name)
        fd_m.show_save_file_dialog("Choose filename fbx", "", ["*.fbx"], export_scene)


# ---------------------------------------------------------------------------------------------------------
# csc.fbx.FbxSettingsAxis Class
# FbxSettingsAxis enumeration for defining the axis configurations in FBX settings.
#
# Members:
# - X = <FbxSettingsAxis.X: 0>
# - Y = <FbxSettingsAxis.Y: 1>
# - Z = <FbxSettingsAxis.Z: 2>
#
# Properties:
# - name → str
#   Gets the name of the axis.
# - value → int
#   Gets the value of the axis.
#
def csc_FbxSettingsAxis_example():
# This script exports FBX file with a custom up axis
    import csc
    from csc import fbx
    def run(scene):
        app = csc.app.get_application()
        fd_m = app.get_file_dialog_manager()
        def export_scene(file_name):
            # Initialize FbxSettings
            settings = fbx.FbxSettings()
            # Set up the up axis (X, Y or Z)
            settings.up_axis = fbx.FbxSettingsAxis.Y
            scene_manager = app.get_scene_manager()
            tools_manager = app.get_tools_manager()
            current_scene = scene_manager.current_scene()
            fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
            fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)
            fbx_scene_loader.set_settings(settings)
            fbx_scene_loader.export_all_objects(file_name)
        fd_m.show_save_file_dialog("Choose filename fbx", "", ["*.fbx"], export_scene)


# ---------------------------------------------------------------------------------------------------------
# csc.fbx.FbxSettingsMode Class
# FbxSettingsMode enumeration for defining the mode configurations in FBX settings.
#
# Members:
# - Binary = <FbxSettingsMode.Binary: 0>
# - Ascii = <FbxSettingsMode.Ascii: 1>
#
# Properties:
# - name → str
#   Gets the name of the mode.
# - value → int
#   Gets the value of the mode.
#
def csc_FbxSettingsMode_example():
    # This script exports FBX file with a custom FBX type
    import csc
    from csc import fbx
    def run(scene):
        app = csc.app.get_application()
        fd_m = app.get_file_dialog_manager()
        def export_scene(file_name):
            # Initialize FbxSettings
            settings = fbx.FbxSettings()
            # Set the Fbx type - Ascii or Binary
            settings.mode = fbx.FbxSettingsMode.Binary
            scene_manager = app.get_scene_manager()
            tools_manager = app.get_tools_manager()
            current_scene = scene_manager.current_scene()
            fbx_scene_loader_tool = tools_manager.get_tool("FbxSceneLoader")
            fbx_scene_loader = fbx_scene_loader_tool.get_fbx_loader(current_scene)
            fbx_scene_loader.set_settings(settings)
            fbx_scene_loader.export_all_objects(file_name)
        fd_m.show_save_file_dialog("Choose filename fbx", "", ["*.fbx"], export_scene)


# ---------------------------------------------------------------------------------------------------------
# csc.rig.AddElementData Class
# AddElementData class for managing element additions in the rigging process.
#
# Properties:
# - axis_point_controller → Any
#   Stores the axis point controller data.
# - box_multiplier → float
#   Multiplier for the box size.
# - is_multiple → bool
#   Indicates if multiple elements are being added.
# - joint_size_without_child → float
#   Size of the joint when there are no child elements.
# - offset_point_controller → Any
#   Stores the offset point controller data.
# - only_box_controller → bool
#   Determines if only the box controller should be used.
# - orthogonal_with_parent → bool
#   Determines if the element is orthogonal with its parent.
# - point_color → tuple
#   Stores the color information of the point.
# - use_global_axis → bool
#   Indicates if global axis should be used.
#
# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.rig.AutoRigData Class
# AutoRigData class for configuring automatic rigging data.
#
# Properties:
# - additionals → list
#   List of additional rigging elements.
# - arms → list
#   List of arm rigging elements.
# - directions → list
#   List of directions for rigging.
# - finger_names → list
#   List of finger names for rigging.
# - foots → list
#   List of foot rigging elements.
# - fulcrum_groups → list
#   List of fulcrum group elements for rigging.
# - hands → list
#   List of hand rigging elements.
# - hinge_names → list
#   List of hinge names for rigging.
# - names → list
#   List of names used in the rigging process.
# - neck → list
#   List of neck rigging elements.
# - pelvis → list
#   List of pelvis rigging elements.
# - spine_names → list
#   List of spine names for rigging.
# - straighten_names → list
#   List of straighten names for rigging.
# - thighs → list
#   List of thigh rigging elements.
# - toes → list
#   List of toe rigging elements.
# - values → list
#   List of values used for configuring rigging.
#
# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.rig.NamesInfo Class
# Provides information regarding the names and properties of joints and their influence within a rig.

# Properties:
# begin_joint -> str
#   Gets and sets the beginning joint of the rig.
# end_joint -> str
#   Gets and sets the ending joint of the rig.
# is_affect_parent -> bool
#   Gets and sets whether the rig affects the parent joint.
# is_inverse -> bool
#   Gets and sets whether the rig is inverted.
# is_left -> bool
#   Gets and sets whether the rig is on the left side.

# Example usage:
# Empty space here


# csc.rig.RigValues Class
# Represents the properties and methods related to rig values within a scene, such as offsets, scales, and mass.

# Properties:
# additional_point_global_offset -> float
#   Gets and sets the global offset of an additional point in the rig.
# box_global_offset -> float
#   Gets and sets the global offset of the rig's box.
# box_scale_depth -> float
#   Gets and sets the depth scale of the rig's box.
# box_scale_width -> float
#   Gets and sets the width scale of the rig's box.
# mass -> float
#   Gets and sets the mass value of the rig.
# width -> float
#   Gets and sets the width value of the rig.

# Methods:
# get_names(self: csc.rig.RigValues) → Dict[str, str]
#   Retrieves the names associated with various rig values.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.layers.Cycle Class
# Represents a cycle within the layer structure, containing information about active and inactive frames.

# Properties:
# first_active_frame_index -> int
#   Gets the index of the first active frame in the cycle.
# following_interval -> int
#   Gets the interval following the current cycle.
# last_active_frame_index -> int
#   Gets the index of the last active frame in the cycle.
# left_inactive_frame_index -> int
#   Gets the index of the left inactive frame in the cycle.
# right_inactive_frame_index -> int
#   Gets the index of the right inactive frame in the cycle.

# Static Methods:
# get_no_pos() → int
#   Returns a constant representing no position.

# Methods:
# is_the_same_frames_as(self: csc.layers.Cycle, other_cycle: csc.layers.Cycle) → bool
#   Checks if the current cycle has the same frames as another cycle.
# left_frame_index(self: csc.layers.Cycle) → int
#   Retrieves the index of the left frame in the cycle.
# right_frame_index(self: csc.layers.Cycle) → int
#   Retrieves the index of the right frame in the cycle.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.layers.CyclesEditor Class
# Represents an editor for managing cycles within layers.

# Methods:
# change_inactive_parts(self: csc.layers.CyclesEditor, arg0: int, arg1: int, arg2: int) → None
#   Modifies the inactive parts of a cycle with the given arguments.
# create_cycle(self: csc.layers.CyclesEditor, arg0: int, arg1: int) → None
#   Creates a new cycle at the specified positions.
# delete_cycle(self: csc.layers.CyclesEditor, arg0: int) → None
#   Deletes a cycle at the specified position.
# get_cycle_or_null(self: csc.layers.CyclesEditor, arg0: int) → object
#   Retrieves a cycle or returns null if it does not exist.
# normalize(self: csc.layers.CyclesEditor) → None
#   Normalizes the cycle values within the editor.

# Example usage:
# Empty space here

# ---------------------------------------------------------------------------------------------------------
# csc.layers.CyclesViewer Class
# Provides methods for viewing and interacting with cycles within a layer.

# Methods:
# any_cycles_exist_in_frames(self: csc.layers.CyclesViewer, arg0: int, arg1: int) → bool
#   Checks if there are any cycles in the specified frame range.
# cycle_contains_frame_index(self: csc.layers.CyclesViewer, arg0: csc.layers.Cycle, arg1: int) → bool
#   Checks if a cycle contains the specified frame index.
# get_active_pos(self: csc.layers.CyclesViewer, arg0: int) → int
#   Retrieves the active position within the cycle for the specified frame.
# get_active_section_pos(self: csc.layers.CyclesViewer, arg0: int) → int
#   Retrieves the active section position for the specified frame.
# get_cell(self: csc.layers.CyclesViewer, arg0: int) → domain::scene::layers::layer::Cell
#   Retrieves the cell associated with the specified frame index.
# get_cycle_or_null(self: csc.layers.CyclesViewer, arg0: int) → object
#   Retrieves a cycle or returns null if it does not exist.
# get_cycles_in_frames(self: csc.layers.CyclesViewer, arg0: int, arg1: int) → List[csc.layers.Cycle]
#   Retrieves a list of cycles within the specified frame range.
# get_most_left_and_right_frame_indices_of_cycle(self: csc.layers.CyclesViewer, arg0: csc.layers.Cycle) → Tuple[int, int]
#   Retrieves the most left and right frame indices of a cycle.
# is_pos_in_active_cycle_zone(self: csc.layers.CyclesViewer, arg0: int) → bool
#   Checks if a position is in the active zone of a cycle.
# is_pos_in_inactive_cycle_zone(self: csc.layers.CyclesViewer, arg0: int) → bool
#   Checks if a position is in the inactive zone of a cycle.
# last_pos(self: csc.layers.CyclesViewer) → int
#   Retrieves the last position in the viewer.

# Example usage:
# Empty space here


# ---------------------------------------------------------------------------------------------------------
# csc.layers.Editor Class
# Provides editing capabilities for layers, allowing manipulation of folders and layers within a scene.

# Methods:
# change_section(self: csc.layers.Editor, arg0: int, arg1: csc.Guid, arg2: function) → None
#   Changes a section in the editor with the specified parameters.
# clear(self: csc.layers.Editor) → None
#   Clears all sections within the editor.
# create_folder(self: csc.layers.Editor, name: str, parent: csc.Guid, with_default_layer: bool = True, pos: Optional[int] = None) → csc.Guid
#   Creates a folder with the specified name, parent, and position.
# create_layer(self: csc.layers.Editor, name: str, parent: csc.Guid, pos: Optional[int] = None) → csc.Guid
#   Creates a layer with the specified name, parent, and position.
# delete_empty_folders(self: csc.layers.Editor) → None
#   Deletes all empty folders within the editor.
# delete_empty_layers(self: csc.layers.Editor) → None
#   Deletes all empty layers within the editor.
# delete_folder(self: csc.layers.Editor, id: csc.Guid) → None
#   Deletes the folder with the specified ID.
# delete_layer(self: csc.layers.Editor, id: csc.Guid) → None
#   Deletes the layer with the specified ID.
# find_header(self: csc.layers.Editor, arg0: csc.Guid) → object
#   Finds and returns the header for the specified ID.
# insert_layer(self: csc.layers.Editor, layer: csc.layers.Layer, pos: Optional[int]) → None
#   Inserts a layer at the specified position within the editor.
# move_item(self: csc.layers.Editor, item_id: csc.Guid, folder_id: csc.Guid, pos: Optional[int] = None) → None
#   Moves an item to a specified folder at the given position.
# normalize_sections(self: csc.layers.Editor) → None
#   Normalizes all sections within the editor.
# set_default(self: csc.layers.Editor) → None
#   Sets the editor back to its default state.
# set_fixed_interpolation_if_need(*args, **kwargs)
#   Overloaded method that sets the fixed interpolation if needed.
# set_fixed_interpolation_or_key_if_need(self: csc.layers.Editor, id: csc.Guid, frame: int, set_key: bool) → bool
#   Sets fixed interpolation or a key at the specified frame if needed.
# set_locked_for_item(self: csc.layers.Editor, is_l: bool, id: csc.Guid) → None
#   Sets the locked state for a specific item.
# set_locked_for_layer(self: csc.layers.Editor, is_l: bool, id: csc.Guid) → None
#   Sets the locked state for a specific layer.
# set_name(self: csc.layers.Editor, name: str, id: csc.Guid) → None
#   Sets the name for the item with the specified ID.
# set_section(self: csc.layers.Editor, section: domain::scene::layers::layer::Section, pos: int, id: csc.Guid) → None
#   Sets a section in the editor with the specified properties.
# set_sections(self: csc.layers.Editor, arg0: Dict[int, domain::scene::layers::layer::Section], arg1: csc.Guid) → None
#   Sets multiple sections in the editor with the specified properties.
# set_visible_for_item(self: csc.layers.Editor, is_v: bool, id: csc.Guid) → None
#   Sets the visible state for a specific item.
# set_visible_for_layer(self: csc.layers.Editor, is_v: bool, id: csc.Guid) → None
#   Sets the visible state for a specific layer.
# unset_section(self: csc.layers.Editor, pos: int, id: csc.Guid) → None
#   Unsets a section in the editor with the specified position and ID.

def csc_layers_Editor_example():
# This script changes the interpolation of the specified section on the specified track
    import csc
    def run(scene):
        mv = scene.model_viewer()
        lv = scene.layers_viewer()
        obj_id = mv.get_objects()[0]
        def mod(model, update, scene):
            le = model.layers_editor()
            obj_track = lv.layer_id_by_obj_id(obj_id)
            # Set keyframe on frame 5 of the specified track
            le.set_fixed_interpolation_or_key_if_need(obj_track, 5, True)
            # Set Bezier interpolation starting from frame 0 until the next keyframe
            def mod_section(section):
                section.interval.interpolation = csc.layers.layer.Interpolation.BEZIER
            le.change_section(0, obj_track, mod_section)
        scene.modify('Set fixed interpolation or key', mod)

def csc_layers_Editor_example_2():
    #This script creates a new folder and track in the scene's root track
    import csc
    def run(scene):
        def mod(model, update, scene):
            lv = scene.layers_viewer()
            le = model.layers_editor()
            root_folder = lv.root_id()
            # Create a new folder, without a default track added to it
            new_folder = le.create_folder('NewFolder', root_folder, False)
            # Create a new track that belongs to the new folder
            new_track = le.create_layer('NewTrack', new_folder)
        scene.modify('Create new folder and track', mod)

def csc_layers_Editor_example_3():
# This script deletes all empty folders and tracks on the timeline
    import csc
    def run(scene):
        def mod(model, update, scene):
            le = model.layers_editor()
            # Delete all empty folders and tracks. The tracks must be deleted before the folders.
            le.delete_empty_layers()
            le.delete_empty_folders()
        scene.modify('Delete empty folders and tracks', mod)

def csc_layers_Editor_example_4():
# This script creates a new folder and track and then deletes them
    import csc
    def run(scene):
        def mod(model, update, scene):
            lv = scene.layers_viewer()
            le = model.layers_editor()
            root_folder = lv.root_id()
            # Create a new folder, without a default track added to it
            new_folder = le.create_folder('NewFolder', root_folder, False)
            # Create a new track that belongs to the new folder
            new_track = le.create_layer('NewTrack', new_folder)
            # Delete the new track. The track must be deleted before the folder that it belongs to.
            le.delete_layer(new_track)
            # Delete the new folder
            le.delete_folder(new_folder)
        scene.modify('Delete specified folder and track', mod)

def csc_layers_Editor_example_5():
    # This script changes the visibility and lock state of the specified tracks
    import csc
    def run(scene):
        def mod(model, update, scene):
            le = model.layers_editor()
            ls = model.layers_selector()
            # Get selected tracks
            selected_layer_ids = ls.all_included_layer_ids()
            for layer_id in selected_layer_ids:
                # Changes visibility of the specified track. False = hidden, True = visible
                le.set_visible_for_layer(False, layer_id)
                # Changes the lock state of the specified track. False = unlocked, True = locked
                le.set_locked_for_layer(True, layer_id)
                print(f"Layer {layer_id} is now hidden and locked")
        scene.modify('Change track visibility', mod)

def csc_layers_Editor_example_6():
# This script sets a keyframe and a fixed interpolation on a specified track's specified frame
    import csc
    def run(scene):
        mv = scene.model_viewer()
        lv = scene.layers_viewer()
        obj_id = mv.get_objects()[0]
        def mod(model, update, scene):
            le = model.layers_editor()
            obj_track = lv.layer_id_by_obj_id(obj_id)
            # Set keyframe on frame 5 of the specified track
            le.set_fixed_interpolation_or_key_if_need(obj_track, 5, True)
            # Set Bezier interpolation starting from frame 0 until the next keyframe
            def mod_section(section):
                section.interval.interpolation = csc.layers.layer.Interpolation.BEZIER
            le.change_section(0, obj_track, mod_section)
            # Change the existing Bezier interpolation of the specified track to Fixed, on frame 1
            le.set_fixed_interpolation_if_need(obj_track, 1)
        scene.modify('Set fixed interpolation or key', mod)


# csc.layers.Folder Class
# Represents a folder in the layers structure, containing methods to manage child items and their order.

# Properties:
# header -> Header
#   Gets the header properties of the folder.

# Methods:
# child_by_id(self: csc.layers.Folder, id: csc.Guid) → csc.Guid
#   Retrieves the child item with the specified ID.
# child_by_pos(self: csc.layers.Folder, pos: int) → csc.Guid
#   Retrieves the child item at the specified position.
# child_pos(self: csc.layers.Folder, id: csc.Guid) → int
#   Retrieves the position of the child item with the specified ID.
# children_cnt(self: csc.layers.Folder) → int
#   Retrieves the count of children in the folder.
# children_ids(self: csc.layers.Folder) → List[csc.Guid]
#   Retrieves a list of child IDs in the folder.
# children_ordered(self: csc.layers.Folder) → List[csc.Guid]
#   Retrieves an ordered list of child IDs in the folder.
# has_child(self: csc.layers.Folder, id: csc.Guid) → bool
#   Checks if the folder has a child with the specified ID.
# is_empty(self: csc.layers.Folder) → bool
#   Checks if the folder is empty.

# Example usage:
# Empty space here


# csc.layers.Header Class
# Represents the header information for a folder or layer, providing methods to access its properties.

# Properties:
# id -> csc.Guid
#   Gets and sets the unique identifier for the header.
# name -> str
#   Gets and sets the name of the header.
# parent -> csc.Guid
#   Gets and sets the parent identifier of the header.

# Example usage:
# This script showcases the use of csc.layers.Header class properties
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_id = mv.get_objects()[0]
#
#     def mod(model, update, scene):
#         # Get Layer ID of the track
#         obj_track = lv.layer_id_by_obj_id(obj_id)
#         # Get Layer object from the Layer ID
#         track_layer = lv.layer(obj_track)
#         # Get header from the Layer object
#         obj_track_header = track_layer.header
#         print(f"Track ID: {obj_track_header.id}")
#         print(f"Track name: {obj_track_header.name}")
#         print(f"Track parent ID: {obj_track_header.parent}")
#     scene.modify("Get ID, name and parent of the specified track's header", mod)

# csc.layers.ItemVariant Class
# Represents an item that can be either a folder or a layer in the scene structure.

# Methods:
# folder(self: csc.layers.ItemVariant) → domain::scene::layers::Folder
#   Retrieves the folder if the variant is a folder, otherwise returns None.
# header(self: csc.layers.ItemVariant) → csc.layers.Header
#   Retrieves the header of the variant.
# is_folder(self: csc.layers.ItemVariant) → bool
#   Checks if the variant is a folder.
# is_layer(self: csc.layers.ItemVariant) → bool
#   Checks if the variant is a layer.
# layer(self: csc.layers.ItemVariant) → domain::scene::layers::Layer
#   Retrieves the layer if the variant is a layer, otherwise returns None.

# Example usage:
# This script checks if the specified ItemVariant is a layer or a folder
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         liv = csc.layers.ItemVariant
#         lv = scene.layers_viewer()
#         root_folder = lv.root_id()
#         # Get all child ItemIDs of the root folder
#         child_ids = lv.all_child_ids(root_folder)
#         for id in child_ids:
#             # Get ItemVariant from ItemID
#             itemvar_id = lv.item(id)
#             if liv.is_folder(itemvar_id):
#                 # Get the Header from the ItemVariant and get the Header's name
#                 print(f"{itemvar_id.header().name} is a folder")
#             elif liv.is_layer(itemvar_id):
#                 print(f"{itemvar_id.header().name} is a layer")
#
#     scene.modify('Check if the item is folder or layer', mod)


# csc.layers.Layer Class
# Represents a basic element in the scene structure used to define interpolation properties for objects.

# Properties:
# header -> Header
#   Gets the header information for the layer.
# is_locked -> bool
#   Gets the locked state of the layer.
# is_visible -> bool
#   Gets the visibility state of the layer.
# obj_ids -> csc.model.ObjectId{}
#   Gets the object IDs associated with the layer.
# sections -> std::map<Pos, Section>
#   Gets the sections within the layer.

# Methods:
# actual_key(self: csc.layers.Layer, pos: int) → domain::scene::layers::layer::Key
#   Retrieves the key at the specified position within the layer.
# actual_key_pos(self: csc.layers.Layer, pos: int) → int
#   Retrieves the position of the key within the layer.
# actual_section(self: csc.layers.Layer, pos: int) → domain::scene::layers::layer::Section
#   Retrieves the section at the specified position within the layer.
# actual_section_pos(self: csc.layers.Layer, pos: int) → int
#   Retrieves the position of the section within the layer.
# cell(self: csc.layers.Layer, pos: int) → domain::scene::layers::layer::Cell
#   Retrieves the cell at the specified position within the layer.
# find_section(self: csc.layers.Layer, pos: int) → object
#   Finds and returns the section at the specified position.
# interval(self: csc.layers.Layer, pos: int) → domain::scene::layers::layer::Interval
#   Retrieves the interval at the specified position within the layer.
# is_key(self: csc.layers.Layer, pos: int) → bool
#   Checks if the position corresponds to a key.
# is_key_or_fixed(self: csc.layers.Layer, pos: int) → bool
#   Checks if the position corresponds to a key or a fixed value.
# key(self: csc.layers.Layer, pos: int) → domain::scene::layers::layer::Key
#   Retrieves the key at the specified position within the layer.
# key_frame_indices(self: csc.layers.Layer) → domain::scene::layers::index::FramesIndices
#   Retrieves the indices of frames that contain keys within the layer.
# last_key_pos(self: csc.layers.Layer) → int
#   Retrieves the position of the last key within the layer.
# section(self: csc.layers.Layer, pos: int) → domain::scene::layers::layer::Section
#   Retrieves the section at the specified position.

# Example usage:
# This script gets the visibility, lock status and associated Object IDs of the specified tracks
# import csc
#
# def run(scene):
#     lv = scene.layers_viewer()
#     root_folder = lv.root_id()
#     all_layer_ids = set(lv.all_included_layer_ids([root_folder]))
#     for layer_id in all_layer_ids:
#         layer_obj = lv.layer(layer_id)
#         # Get Header
#         layer_header = layer_obj.header
#         # Get Object IDs belonging to the layer
#         obj_ids = layer_obj.obj_ids
#         visibility_state = 'is visible' if layer_obj.is_visible else 'is not visible'
#         lock_state = 'locked' if layer_obj.is_locked else 'not locked'
#         print(f"Track {layer_header.name} {visibility_state} and {lock_state} and has the following Object IDs in it:")
#         for obj_id in obj_ids:
#             print(obj_id)


# csc.layers.Layers Class
# Represents the root class describing the layers’ hierarchy of the scene. Each scene object can be placed on any layer to define its personal interpolation properties.

# Properties:
# root_id -> csc.Guid
#   Gets the root identifier of the layer.

# Methods:
# folders(self: csc.layers.Layers) → object
#   Returns a dictionary mapping FolderId to Folder objects.

# layers(self: csc.layers.Layers) → LayersContainer
#   Returns the container of layers.

# Example usage:
# Empty space here


# csc.layers.layer.Interpolation Class
# Represents an Interpolation enumeration used for defining various types of interpolation methods in layers.

# Members:
# BEZIER = <Interpolation.BEZIER: 0>
# LOW_AMPLITUDE_BEZIER = <Interpolation.LOW_AMPLITUDE_BEZIER: 1>
# LINEAR = <Interpolation.LINEAR: 2>
# STEP = <Interpolation.STEP: 3>
# FIXED = <Interpolation.FIXED: 4>
# NONE = <Interpolation.NONE: 5>
# CLAMPED_BEZIER = <Interpolation.CLAMPED_BEZIER: 6>

# Properties:
# name -> str
#   Retrieves the name of the interpolation method.
# value -> int
#   Retrieves the numerical value of the interpolation method.

# Example usage:
# This script changes the interpolation of the specified section on the specified track
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_id = mv.get_objects()[0]
#     def mod(model, update, scene):
#         le = model.layers_editor()
#         obj_track = lv.layer_id_by_obj_id(obj_id)
#         # Set keyframe on frame 5 of the specified track
#         le.set_fixed_interpolation_or_key_if_need(obj_track, 5, True)
#         def mod_section(section):
#             Prints the current interpolation in the specified section
#             print(section.interval.interpolation)
#             # Set Linear interpolation starting from frame 0 until the next keyframe
#             section.interval.interpolation = csc.layers.layer.Interpolation.LINEAR
#         le.change_section(0, obj_track, mod_section)
#     scene.modify('Set interpolation', mod)


# csc.layers.layer.Tangents Class
# Represents the Layer Frame Tangents enumerable, with two possible values: Continuous and UserDefined.

# Members:
# Continuous = <Tangents.Continuous: 0>
# UserDefined = <Tangents.UserDefined: 1>

# Properties:
# name → str
#   Gets the name of the Tangent.
# value → int
#   Gets the value associated with the Tangent.

# Example usage:
# Empty space here


# csc.layers.layer.Label Class
# Represents a Layer Frame Label enumerable within Cascadeur's system. This is used to indicate the significance of a layer frame, with predefined labels.

# Members:
# NONE = <Label.NONE: 0>
#   Represents the absence of any label or significance.
# SIGNIFICANT = <Label.SIGNIFICANT: 1>
#   Represents a significant frame in the layer.

# Properties:
# name → str
#   Gets the name of the label.
# value → int
#   Gets the integer value associated with the label (0 for NONE, 1 for SIGNIFICANT).

# Example usage:
# Empty space here


# csc.layers.layer.IkFk Class
# Represents the Layer Frame IkFk enumerable, defining IK and FK states for animation layers.

# Members:
# IK = <IkFk.IK: 0>
# FK = <IkFk.FK: 1>

# Properties:
# name -> str
#   Gets the name of the IkFk object.
# value -> int
#   Gets the integer value representing either IK or FK state.

# Example usage:
# This script changes the kinematics of the specified section on the specified track
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_id = mv.get_objects()[0]
#     def mod(model, update, scene):
#         le = model.layers_editor()
#         obj_track = lv.layer_id_by_obj_id(obj_id)
#         # Set FK kinematics starting from frame 0 until the next keyframe
#         def mod_section(section):
#             section.interval.common.ik_fk = csc.layers.layer.IkFk.FK
#         le.change_section(0, obj_track, mod_section)
#     scene.modify('Set IK-FK kinematics on interval', mod)


# csc.layers.layer.Fixation Class
# Represents a Layer Frame Fixation enumerable for defining fixation types like Free and Fulcrum.

# Members:
# Free = <Fixation.Free: 0>
# Fulcrum = <Fixation.Fulcrum: 2>

# Properties:
# name -> str
#   Gets the name of the fixation type.
# value -> int
#   Gets the integer value associated with the fixation type.

# Example usage:
# This script changes the fulcrum state of the specified section on the specified track
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_id = mv.get_objects()[0]
#     def mod(model, update, scene):
#         le = model.layers_editor()
#         obj_track = lv.layer_id_by_obj_id(obj_id)
#         # Set keyframe on frame 5 of the specified track
#         le.set_fixed_interpolation_or_key_if_need(obj_track, 5, True)
#         def mod_section(section):
#             # Set Fulcrum state starting from frame 0 until the next keyframe
#             section.interval.common.fixation = csc.layers.layer.Fixation.Fulcrum
#         le.change_section(0, obj_track, mod_section)
#     scene.modify('Set Fulcrum state on interval', mod)


# csc.layers.layer.Common Class
# The Common class implements interpolation type and fixation of the layer.

# Properties:
# ik_fk → IkFk
#   Gets and sets the IkFk type.
# fixation → Fixation
#   Gets and sets the Fixation type.

# Example usage:
# This script showcases the use of properties in csc.layers.layer.Common class
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_id = mv.get_objects()[0]
#     def mod(model, update, scene):
#         le = model.layers_editor()
#         obj_track = lv.layer_id_by_obj_id(obj_id)
#         # Set keyframe on frame 5 of the specified track
#         le.set_fixed_interpolation_or_key_if_need(obj_track, 5, True)
#         def mod_section(section):
#             # Set Fulcrum state on interval starting from frame 0 until the next keyframe
#             section.interval.common.fixation = csc.layers.layer.Fixation.Fulcrum
#             # Set FK kinematics on the keyframe on frame 0
#             section.key.common.ik_fk = csc.layers.layer.IkFk.FK
#         le.change_section(0, obj_track, mod_section)
#     scene.modify('Set Fulcrum state and IK-FK kinematics on interval and keyframe', mod)


# csc.layers.layer.Key Class
# Represents a Key class in Cascadeur's layer system, which holds valuable properties of a frame where users can set positions.

# Properties:
# common → csc.layers.layer.Common
#   Get and set the Common property.
# label → str
#   Get and set the Label property.
# tangents → csc.layers.layer.Tangents
#   Get and set the Tangents property.

# Example usage:
# This script checks the kinematics on the specified keyframe
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_id = mv.get_objects()[0]
#     def mod(model, update, scene):
#         le = model.layers_editor()
#         obj_track = lv.layer_id_by_obj_id(obj_id)
#         def mod_section(section):
#             Print the current kinematics value on the keyframe
#             print(section.key.common.ik_fk)
#             # Set FK kinematics on the keyframe on frame 0
#             section.key.common.ik_fk = csc.layers.layer.IkFk.FK
#         le.change_section(0, obj_track, mod_section)
#     scene.modify('Set IK-FK kinematics on keyframe', mod)


# csc.layers.layer.Interval Class
# Describes the interpolation interval properties in Cascadeur's system.

# Properties:
# common → csc.Common
#   Gets and sets the common properties of the interval.
# interpolation → csc.Interpolation
#   Gets and sets the interpolation settings of the interval.

# Example usage:
# This script prints the interpolation and kinematics on the specified section of the specified layer
# import csc
#
# def run(scene):
#     lv = scene.layers_viewer()
#     # Get default LayerID in the scene
#     def_id = lv.default_layer_id()
#     # Get Layer object from Layer ID
#     def_layer = lv.layer(def_id)
#     # Get the section on frame 0
#     section = def_layer.sections[0]
#     Print interpolation on section
#     print(section.interval.interpolation)
#     Print kinematics on section
#     print(section.interval.common.ik_fk)


# csc.layers.layer.Section Class
# Describes the interpolation properties of the section.

# Members:
# key
#   Get or set the Key associated with this section.
# interval
#   Get or set the Interval associated with this section.

# Example usage:
# This script prints the interpolation and kinematics on the specified key and section of the specified layer
# import csc
#
# def run(scene):
#     lv = scene.layers_viewer()
#     # Get default LayerID in the scene
#     def_id = lv.default_layer_id()
#     # Get Layer object from Layer ID
#     def_layer = lv.layer(def_id)
#     # Get the section on frame 0
#     section = def_layer.sections[0]
#     # Print interpolation on section
#     print(section.interval.interpolation)
#     # Print kinematics on section
#     print(section.interval.common.ik_fk)
#     # Print kinematics on keyframe
#     print(section.key.common.ik_fk)


# csc.layers.layer.Cell Class
# Describes the frame properties on an interval.

# Properties:
# key → csc.Key
#   Gets and sets the key of the cell.

# interval → csc.layers.index.FramesInterval
#   Gets and sets the interval of the cell.

# Example usage:
# Empty space here


# csc.layers.index.FramesInterval Class
# Describes the interval of frames.

# Variables:
# start -> int
#   Gets the starting frame of the interval.
# end -> int
#   Gets the ending frame of the interval.

# Methods:
# distance(self: csc.layers.index.FramesInterval) → int
#   Calculates the distance (number of frames) between the start and end of the interval.

# valid(self: csc.layers.index.FramesInterval) → bool
#   Checks if the interval is valid, meaning the start is less than or equal to the end.

# Properties:
# first -> int
#   Gets the first frame of the interval.
# last -> int
#   Gets the last frame of the interval.

# Example usage:
# This sript showcases the use of methods and properties of csc.layers.index.FramesInterval class
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         ls = model.layers_selector()
#         # Get IndicesContainer from timeline selection
#         selection = ls.selection()
#         # Get frames interval from IndicesContainer
#         frames_interval = selection.frames_interval()
#         start_frame = frames_interval.first
#         end_frame = frames_interval.last
#         interval_length = frames_interval.distance()
#         interval_validity = frames_interval.valid()
#         print(f"First frame: {start_frame}")
#         print(f"Last frame: {end_frame}")
#         print(f"Interval length: {interval_length}")
#         print(f"Interval has 1 or more frames: {interval_validity}")
#     scene.modify('Frames interval', mod)


# csc.layers.index.FramesIndices Class
# Helps to work with animation intervals.

# Methods:

# add(self: csc.layers.index.FramesIndices, index: int) -> None
#   Adds a single index to the FramesIndices.

# add(self: csc.layers.index.FramesIndices, other: csc.layers.index.FramesIndices) -> None
#   Adds the indices from another FramesIndices object.

# add(self: csc.layers.index.FramesIndices, indices: Set[int]) -> None
#   Adds a set of indices to the FramesIndices.

# add(self: csc.layers.index.FramesIndices, indices: List[int]) -> None
#   Adds a list of indices to the FramesIndices.

# clamp(self: csc.layers.index.FramesIndices, min: int, max: int) → csc.layers.index.FramesIndices
#   Clamps the indices within the specified minimum and maximum values.

# empty(self: csc.layers.index.FramesIndices) → bool
#   Checks if the FramesIndices object is empty.

# first(self: csc.layers.index.FramesIndices) → int
#   Returns the first index from the FramesIndices.

# static from_range(min: int, max: int) → csc.layers.index.FramesIndices
#   Creates a FramesIndices object from a specified range of indices.

# static intersect_indices(l: csc.layers.index.FramesIndices, r: csc.layers.index.FramesIndices) → csc.layers.index.FramesIndices
#   Returns a new FramesIndices object that is the intersection of two FramesIndices objects.

# last(self: csc.layers.index.FramesIndices) → int
#   Returns the last index from the FramesIndices.

# size(self: csc.layers.index.FramesIndices) → int
#   Returns the size (number of indices) in the FramesIndices object.

# static to_intervals(indices: csc.layers.index.FramesIndices) → List[csc.layers.index.FramesInterval]
#   Converts a FramesIndices object into a list of FramesInterval objects.

# static union_indices(l: csc.layers.index.FramesIndices, r: csc.layers.index.FramesIndices) → csc.layers.index.FramesIndices
#   Returns a new FramesIndices object that is the union of two FramesIndices objects.

# Example usage:
# Empty space here


# csc.layers.index.CellIndex Class
# Represents the CellIndex class, which implements properties for indexing frames and items.

# Methods:
# is_valid(self: csc.layers.index.CellIndex) → bool
#   Checks whether the CellIndex is valid.

# Properties:
# frame_index → int
#   Gets the frame index.
# item_id → csc.Guid
#   Gets the GUID of the item.

# Example usage:
# Empty space here


# csc.layers.index.RectIndicesContainer Class
# This is a container of items that are placed in the rect indices.

# Methods:
# add_item_id(self: csc.layers.index.RectIndicesContainer, item_id: csc.Guid) → None
#   Adds an item ID to the RectIndicesContainer.

# contains(self: csc.layers.index.RectIndicesContainer, item_id: csc.Guid) → bool
#   Checks if the RectIndicesContainer contains a specific item ID.

# frames_indices(self: csc.layers.index.RectIndicesContainer) → csc.layers.index.FramesIndices
#   Retrieves the frames indices associated with this container.

# item_ids(self: csc.layers.index.RectIndicesContainer) → List[csc.Guid]
#   Returns the list of item IDs stored in the container.

# set_frames_indices(self: csc.layers.index.RectIndicesContainer, frames_indices: csc.layers.index.FramesIndices) → None
#   Sets the frames indices for the RectIndicesContainer.

# set_item_ids(self: csc.layers.index.RectIndicesContainer, item_ids: List[csc.Guid]) → None
#   Sets the list of item IDs for the RectIndicesContainer.

# Example usage:
# Empty space here


# csc.layers.index.IndicesContainer Class
# The IndicesContainer class contains indices items in a structure represented by std::map<ItemId, FramesIndices>.

# Variables:
# all_frame_indices -> int
#   Overridden method for frame indices with sizeLimit.
# frames_interval -> int
#   Overridden method for frames interval with sizeLimit.

# Methods:

# add(self: csc.layers.index.IndicesContainer, other_container: csc.layers.index.IndicesContainer) → None
#   Adds another IndicesContainer to this container.

# add_frame_indices(self: csc.layers.index.IndicesContainer, frame_indices: int) → None
#   Adds frame indices to the container.

# add_item(self: csc.layers.index.IndicesContainer, item_indices: ItemIndices) → None
#   Adds item indices to the container.

# all_frame_indices(self: csc.layers.index.IndicesContainer) → csc.layers.index.FramesIndices
#   Returns all frame indices.
# all_frame_indices(self: csc.layers.index.IndicesContainer, size_limit: int) → csc.layers.index.FramesIndices
#   Returns all frame indices with a size limit.

# cell_indices(self: csc.layers.index.IndicesContainer) → List[csc.layers.index.CellIndex]
#   Returns a list of cell indices.

# delete_empty_items(self: csc.layers.index.IndicesContainer) → None
#   Deletes empty items from the container.

# direct_indices(self: csc.layers.index.IndicesContainer) → Dict[csc.Guid, csc.layers.index.FramesIndices]
#   Returns a dictionary of direct indices mapped by GUID.
# direct_indices(self: csc.layers.index.IndicesContainer) → Dict[csc.Guid, csc.layers.index.FramesIndices]
#   Returns a dictionary of direct indices mapped by GUID.

# frames_interval(self: csc.layers.index.IndicesContainer) → csc.layers.index.FramesInterval
#   Returns the frames interval.
# frames_interval(self: csc.layers.index.IndicesContainer, size_limit: int) → csc.layers.index.FramesInterval
#   Returns the frames interval with a size limit.

# is_empty(self: csc.layers.index.IndicesContainer) → bool
#   Checks if the container is empty.

# item_ids(self: csc.layers.index.IndicesContainer) → List[csc.Guid]
#   Returns a list of item GUIDs.

# item_indices(self: csc.layers.index.IndicesContainer, id: csc.Guid) → csc.layers.index.FramesIndices
#   Returns the frames indices for a specific item ID.

# items_indices(self: csc.layers.index.IndicesContainer) → List[ItemIndices]
#   Returns a list of all item indices.

# rect(self: csc.layers.index.IndicesContainer) → csc.layers.index.RectIndicesContainer
#   Returns the rectangular indices container.

# set_frame_indices(self: csc.layers.index.IndicesContainer, start: int, end: int) → None
#   Sets the frame indices for a range between start and end.

# Example usage:
# This script returns csc.layers.index.FramesInterval from a IndicesContainer of a selected timeline interval
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         ls = model.layers_selector()
#         selection = ls.selection()
#         frames_interval = selection.frames_interval()
#         print(frames_interval)
#     scene.modify('Get frames interval', mod)


# csc.layers.LayersContainer Class
# Represents a container for layers.

# Methods:
# at(self: csc.layers.LayersContainer, arg0: csc.Guid) → Layer
#   Retrieves a layer by its GUID.

# has_any_obj_ids(self: csc.layers.LayersContainer) → bool
#   Checks if any object IDs are present in the layers.

# has_obj_id(self: csc.layers.LayersContainer, id: common::GenericId<domain::scene::model::ModelObject>) → bool
#   Checks if a specific object ID is present in the layers.

# layer_id_by_obj_id(self: csc.layers.LayersContainer, id: common::GenericId<domain::scene::model::ModelObject>) → csc.Guid
#   Retrieves the layer ID associated with a specific object ID.

# layer_id_by_obj_id_or_null(self: csc.layers.LayersContainer, id: common::GenericId<domain::scene::model::ModelObject>) → csc.Guid
#   Retrieves the layer ID associated with a specific object ID, or returns a null ID if not found.

# map(self: csc.layers.LayersContainer) → object
#   Returns a mapping of LayerId to Layer objects.

# obj_ids(self: csc.layers.LayersContainer) → object
#   Returns a mapping of csc.model.ObjectId to LayerId.

# Example usage:
# This script showcases the methods in csc.layers.LayersContainer class
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     obj_id = mv.get_objects()[0]
#     obj_name = mv.get_object_name(obj_id)
#     def mod(model, update, scene):
#         # Get csc.layers.Layers object
#         layers_obj = model.layers()
#         # Get csc.layers.LayersContainer object from csc.layers.Layers object
#         layers_container = layers_obj.layers()
#         has_any_obj_ids = layers_container.has_any_obj_ids()
#         obj_layer = layers_container.layer_id_by_obj_id(obj_id)
#         layer_map = layers_container.map()
#         obj_ids_in_container = layers_container.obj_ids()
#         print(f"LayersContainer has any Object IDs in it: {has_any_obj_ids}")
#         print(f"{obj_name} is inside Layer: {obj_layer}")
#         for layer_id, layer in layer_map.items():
#             print(f"Layer ID: {layer_id}")
#         for obj_id_cont, layer_id_cont in obj_ids_in_container.items():
#             print(f"Object ID: {obj_id_cont}")
#     scene.modify('csc.layers.LayersContainer methods', mod)


# csc.layers.LayersSelectionChanger Class
# Represents a class for changing layer selection.

# Methods:
# refresh(self: csc.layers.LayersSelectionChanger) → bool
#   Refreshes the layer selection.

# selectDefault(self: csc.layers.LayersSelectionChanger) → bool
#   Selects the default layer.

# set_full_selection_by_parts(self: csc.layers.LayersSelectionChanger, inds: domain::scene::layers::index::IndicesContainer) -> None
#   Sets the full selection using an IndicesContainer.

# set_full_selection_by_parts(self: csc.layers.LayersSelectionChanger, itms: List[csc.Guid], first: int, last: int) → bool
#   Sets the full selection using a list of item IDs and range indices.

# Example usage:
# Empty space here


# csc.layers.Selector Class
# Contains methods to observe and set selected layers and folders.

# Properties:
# set_full_selection_by_parts -> IndicesContainer
#   Gets or sets the full selection by parts.

# Methods:
# all_included_layer_ids(self: csc.layers.Selector, ignore_locked: bool = False) → List[csc.Guid]
#   Retrieves all included layer IDs, optionally ignoring locked layers.

# all_included_layer_indices(self: csc.layers.Selector, ignore_locked: bool = False) → domain::scene::layers::index::IndicesContainer
#   Retrieves all included layer indices, optionally ignoring locked layers.

# is_selected(self: csc.layers.Selector, id: csc.Guid) → bool
#   Checks if a layer or folder with the specified ID is selected.

# select_default(self: csc.layers.Selector) → None
#   Selects the default layer or folder.

# selection(self: csc.layers.Selector) → domain::scene::layers::index::IndicesContainer
#   Gets the current selection indices.

# set_full_selection_by_parts(self: csc.layers.Selector, inds: domain::scene::layers::index::IndicesContainer) -> None
#   Sets the full selection using an IndicesContainer.

# set_full_selection_by_parts(self: csc.layers.Selector, itms: List[csc.Guid], first: int, last: int) -> None
#   Sets the full selection using a list of item IDs and range indices.

# set_uncheckable_folder_id(self: csc.layers.Selector, id: csc.Guid, uncheckable: bool) → None
#   Sets whether a folder is uncheckable by its ID.

# top_layer_id(self: csc.layers.Selector) → csc.Guid
#   Retrieves the top layer ID.

# Example usage:
# This script gets IndicesContainer object of the timeline selection
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         ls = model.layers_selector()
#         selection = ls.selection()
#         print(selection)
#     scene.modify('Get IndicesContainer from timeline selection', mod)

# This script gets the FramesInterval of the timeline selection
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         ls = model.layers_selector()
#         selection = ls.selection()
#         frames_interval = selection.frames_interval()
#     scene.modify('Get FramesInterval from timeline selection', mod)


# csc.layers.Viewer Class
# Represents a class containing methods and properties that describe the structure of scene objects’ interpolation properties, represented in the hierarchy of layers divided by folders.

# Properties:
# top_layer_id -> ItemId || ItemId[]
#   Retrieves the top layer ID or a list of top layer IDs.

# merged_layer -> LayerId[]
#   Retrieves merged layer IDs as a list.

# last_key_pos -> Layer
#   Retrieves the last key position for a given layer.

# frames_count -> int
#   Retrieves the total number of frames.

# significant_frames -> int{}
#   Retrieves significant frames for layers as a dictionary.

# Methods:
# actual_key_pos(self: csc.layers.Viewer, pos: int) → int
#   Retrieves the actual key position for a specified position.

# all_child_ids(self: csc.layers.Viewer, id: csc.Guid) → List[csc.Guid]
#   Retrieves all child IDs for a given ID.

# all_included_layer_ids(self: csc.layers.Viewer, items: List[csc.Guid], ignore_locked: bool = False) → List[csc.Guid]
#   Retrieves all included layer IDs for the specified items, optionally ignoring locked layers.

# all_layer_ids(self: csc.layers.Viewer) → List[csc.Guid]
#   Retrieves all layer IDs.

# all_parent_ids(self: csc.layers.Viewer, id: csc.Guid) → List[csc.Guid]
#   Retrieves all parent IDs for a given ID.

# default_layer_id(self: csc.layers.Viewer) → csc.Guid
#   Retrieves the default layer ID.

# find_folder(self: csc.layers.Viewer, id: csc.Guid) → Folder
#   Retrieves a folder by its ID.

# find_layer(self: csc.layers.Viewer, id: csc.Guid) → Layer
#   Retrieves a layer by its ID.

# folder(self: csc.layers.Viewer, id: csc.Guid) → Folder
#   Retrieves a folder by its ID.

# folders_map(self: csc.layers.Viewer) → Dict[csc.Guid, csc.layers.Folder]
#   Retrieves a mapping of FolderId to Folder objects.

# for_all_ordered_items(self: csc.layers.Viewer, arg0: Callable[[csc.Guid], bool]) → None
#   Iterates over all ordered items and executes a callback function.

# frames_count(self: csc.layers.Viewer) → int
#   Retrieves the total number of frames.

# frames_count(self: csc.layers.Viewer, id_arr: List[csc.Guid]) → int
#   Retrieves the total number of frames for the specified list of layer IDs.

# has_item(self: csc.layers.Viewer, id: csc.Guid) → bool
#   Checks if a specified item is present.

# header(self: csc.layers.Viewer, id: csc.Guid) → Header
#   Retrieves the header for a specified ID.

# is_deep_child(self: csc.layers.Viewer, item_id: csc.Guid, folder_id: csc.Guid) → bool
#   Checks if a specified item ID is a deep child of a folder ID.

# item(self: csc.layers.Viewer, id: csc.Guid) → csc.layers.ItemVariant
#   Retrieves an item variant by its ID.

# last_key_pos(self: csc.layers.Viewer, id_arr: List[csc.Guid]) → int
#   Retrieves the last key position for a list of layer IDs.

# layer(self: csc.layers.Viewer, id: csc.Guid) → Layer
#   Retrieves a layer by its ID.

# layer_id_by_obj_id(self: csc.layers.Viewer, id: common::GenericId<domain::scene::model::ModelObject>) → csc.Guid
#   Retrieves the layer ID associated with a specific object ID.

# layer_id_by_obj_id_or_null(self: csc.layers.Viewer, id: common::GenericId<domain::scene::model::ModelObject>) → csc.Guid
#   Retrieves the layer ID associated with a specific object ID, or returns a null ID if not found.

# layer_ids_by_obj_ids(self: csc.layers.Viewer, ids: List[common::GenericId<domain::scene::model::ModelObject>]) → Set[csc.Guid]
#   Retrieves the layer IDs associated with a list of object IDs.

# layers_indices(self: csc.layers.Viewer, id_arr: domain::scene::layers::index::IndicesContainer, ignore_locked: bool = False) → domain::scene::layers::index::IndicesContainer
#   Retrieves the indices of layers, optionally ignoring locked layers.

# layers_map(self: csc.layers.Viewer) → Dict[csc.Guid, csc.layers.Layer]
#   Retrieves a mapping of LayerId to Layer objects.

# merged_layer(self: csc.layers.Viewer, ids: List[csc.Guid]) → csc.layers.Layer
#   Merges layers by their IDs.

# static merged_layer_s(ids: List[csc.layers.Layer]) → csc.layers.Layer
#   Merges layers by their IDs.

# obj_ids_by_layer_ids(self: csc.layers.Viewer, id_arr: List[csc.Guid]) → List[common::GenericId<domain::scene::model::ModelObject>]
#   Retrieves object IDs associated with a list of layer IDs.

# pos_in_parent(self: csc.layers.Viewer, id: csc.Guid) → int
#   Retrieves the position of a layer or folder in its parent.

# root_id(self: csc.layers.Viewer) → csc.Guid
#   Retrieves the root folder ID.

# significant_frames(self: csc.layers.Viewer) → domain::scene::layers::index::FramesIndices
#   Retrieves the significant frames indices.

# significant_frames(self: csc.layers.Viewer, id_arr: Set[csc.Guid]) → domain::scene::layers::index::FramesIndices
#   Retrieves the significant frames indices for a set of layer IDs.

# top_layer_id(self: csc.layers.Viewer, id: csc.Guid) → csc.Guid
#   Retrieves the top layer ID for a specified layer ID.

# top_layer_id(self: csc.layers.Viewer, id_arr: List[csc.Guid]) → csc.Guid
#   Retrieves the top layer ID for a list of layer IDs.

# unlocked_layer_ids(self: csc.layers.Viewer, id_arr: List[csc.Guid]) → List[csc.Guid]
#   Retrieves the list of unlocked layer IDs.

# Example usage:
# This script showcases the methods of csc.layers.Viewer class
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     # Get the scene's root folder (Scene)
#     root_folder = lv.root_id()
#     # Get the default Layer ID in the scene (Track0)
#     default_layer_id = lv.default_layer_id()
#     # Get all first child ItemID objects of the specified GUID
#     child_ids = lv.all_child_ids(default_layer_id)
#     # Get a list of all Object IDs belonging to the ItemID objects
#     obj_ids_in_track = lv.obj_ids_by_layer_ids(child_ids)
#     for obj_id in obj_ids_in_track:
#         # Get LayerID from Object ID
#         found_obj_id = lv.layer_id_by_obj_id(obj_id)
#     for child_id in child_ids:
#         # Get ItemVariant object
#         obj_itemvar = lv.item(child_id)
#         # Get Header object
#         obj_header = lv.header(child_id)
#     # Get a list of all included child ItemID objects of the specified GUID objects
#     all_included_layer_ids = lv.all_included_layer_ids([root_folder])
#     # Get a mapped dictionary with LayerID and Layer objects
#     layers_dict = lv.layers_map
#     # Get a mapped dictionary with FolderID and Folder objects
#     folders_dict = lv.folders_map
#     # Get a list of all Layer ID objects in the scene
#     all_layer_ids = lv.all_layer_ids()
#     # Get a list of all parent Folder ID objects of the specified GUID
#     all_parent_ids = lv.all_parent_ids(default_layer_id)
#     # Get the int value of the last keyframe
#     last_frame_count = lv.frames_count()


# csc.model.BehaviourEditor Class
# Allows editing of scene behaviours and their properties.

# Methods:
# add_behaviour(self: csc.model.BehaviourEditor, arg0: csc.model.ObjectId, arg1: str) → csc.Guid
#   Adds a behaviour of a specified type to an object, returning its identifier.

# add_behaviour(self: csc.model.BehaviourEditor, object_id: csc.model.ObjectId, behaviour_type: str, behaviour_id: csc.Guid) → csc.Guid
#   Adds a behaviour with a given ID to an object, returning its identifier.

# add_behaviour_data_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, data_id: csc.model.DataId) → bool
#   Adds behaviour data to a specified range.

# add_behaviour_model_object_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, mo_id: csc.model.ObjectId) → bool
#   Adds a model object to a specified behaviour range.

# add_behaviour_reference_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, beh_id: csc.Guid) → bool
#   Adds a behaviour reference to a specified range.

# add_behaviour_setting_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, setting_id: csc.model.SettingId) → bool
#   Adds a behaviour setting to a specified range.

# delete_behaviour(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid) → None
#   Deletes a behaviour by its ID.

# delete_behaviours(self: csc.model.BehaviourEditor, objects_id: Set[csc.model.ObjectId]) → None
#   Deletes behaviours for a given set of object IDs.

# erase_behaviour_data_from_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, data_id: csc.model.DataId) → bool
#   Erases behaviour data from a specified range.

# erase_behaviour_model_object_from_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, mo_id: csc.model.ObjectId) → bool
#   Erases a model object from a specified behaviour range.

# erase_behaviour_reference_from_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, beh_id: csc.Guid) → bool
#   Erases a behaviour reference from a specified range.

# erase_behaviour_setting_from_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, setting_id: csc.model.SettingId) → bool
#   Erases a behaviour setting from a specified range.

# get_viewer(self: csc.model.BehaviourEditor) → object
#   Returns the viewer for the behaviour editor.

# hide_behaviour(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, hidden: bool = True) → bool
#   Hides or shows a behaviour by its ID.

# set_behaviour_asset(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, asset_id: csc.Guid) → bool
#   Sets a behaviour asset by its ID.

# set_behaviour_data(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, data_id: csc.model.DataId) → bool
#   Sets behaviour data by its ID.

# set_behaviour_data_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, inserted_ids: List[csc.model.DataId]) → bool
#   Sets behaviour data to a specified range.

# set_behaviour_field_value(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, name_value: str) → bool
#   Sets a behaviour field value.

# set_behaviour_model_object(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, mo_id: csc.model.ObjectId) → bool
#   Sets a model object for a behaviour.

# set_behaviour_model_objects_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, inserted_ids: List[csc.model.ObjectId]) → bool
#   Sets multiple model objects to a specified behaviour range.

# set_behaviour_reference(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, beh_id: csc.Guid) → bool
#   Sets a behaviour reference.

# set_behaviour_references_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, inserted_ids: List[csc.Guid]) → bool
#   Sets multiple behaviour references to a specified range.

# set_behaviour_setting(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, setting_id: csc.model.SettingId) → bool
#   Sets a behaviour setting.

# set_behaviour_settings_to_range(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, inserted_ids: List[csc.model.SettingId]) → bool
#   Sets multiple behaviour settings to a specified range.

# set_behaviour_string(self: csc.model.BehaviourEditor, behaviour_id: csc.Guid, name: str, str: str) → bool
#   Sets a behaviour string.

# Example usage:
# This script sets a specified data node to a specified behaviour data
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     obj_id = mv.get_objects()[0]
#
#     def mod(model, update, scene):
#         be = model.behaviour_editor()
#         de = model.data_editor()
#         new_scale_vector = de.add_data(obj_id, 'New Scale', csc.model.DataMode.Animation, [5.0, 5.0, 5.0]).id
#         transform_beh = bv.get_behaviour_by_name(obj_id, 'Transform')
#         be.set_behaviour_data(transform_beh, 'local_scale', new_scale_vector)
#     scene.modify("Set behaviour data", mod)


# csc.model.BehaviourViewer Class
# Allows viewing of scene behaviours and their properties.

# Methods:
# behaviour_id(self: csc.model.BehaviourViewer, object_id: csc.model.ObjectId, behaviour_name: str) → csc.Guid
#   Retrieves the behaviour ID by object ID and behaviour name.

# get_behaviour_by_name(self: csc.model.BehaviourViewer, object_id: csc.model.ObjectId, bh_name: str) → csc.Guid
#   Retrieves the behaviour ID by object ID and behaviour name.

# get_behaviour_data(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → csc.model.DataId
#   Retrieves behaviour data by behaviour ID and name.

# get_behaviour_data_range(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → List[csc.model.DataId]
#   Retrieves a list of behaviour data by behaviour ID and name.

# get_behaviour_name(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid) → str
#   Retrieves the name of the behaviour.

# get_behaviour_object(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → csc.model.ObjectId
#   Retrieves a behaviour object by behaviour ID and name.

# get_behaviour_objects_range(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → List[csc.model.ObjectId]
#   Retrieves a list of behaviour objects by behaviour ID and name.

# get_behaviour_owner(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid) → csc.model.ObjectId
#   Retrieves the owner object of a behaviour by its ID.

# get_behaviour_reference(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → csc.Guid
#   Retrieves a behaviour reference by behaviour ID and name.

# get_behaviour_reference_range(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → List[csc.Guid]
#   Retrieves a list of behaviour references by behaviour ID and name.

# get_behaviour_setting(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → csc.model.SettingId
#   Retrieves a behaviour setting by behaviour ID and name.

# get_behaviour_settings_range(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → List[csc.model.SettingId]
#   Retrieves a list of behaviour settings by behaviour ID and name.

# get_behaviour_string(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid, name: str) → str
#   Retrieves a behaviour string by behaviour ID and name.

# get_behaviours(self: csc.model.BehaviourViewer, type_name: str) → List[csc.Guid]
#   Retrieves a list of behaviours by type name.

# get_behaviours(self: csc.model.BehaviourViewer, object_id: csc.model.ObjectId) → List[csc.Guid]
#   Retrieves a list of behaviours for a specified object ID.

# get_children(self: csc.model.BehaviourViewer, object_id: csc.model.ObjectId) → List[csc.Guid]
#   Retrieves a list of children behaviour IDs for a specified object.

# is_hidden(self: csc.model.BehaviourViewer, behaviour_id: csc.Guid) → bool
#   Checks if a behaviour is hidden.

# Example usage:
# This script gets a behaviour with a specified name in the specified object
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     obj_id = mv.get_objects()[0]
#     transform_beh = bv.get_behaviour_by_name(obj_id, 'Transform')
#     print(f"Found behaviour: {transform_beh}")

# This script gets object ID of a linked object from a specified behaviour of the specified object
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     obj_id = mv.get_objects()[0]
#     basic_beh = bv.get_behaviour_by_name(obj_id, 'Basic')
#     parent_obj_id = bv.get_behaviour_object(basic_beh, 'parent')
#     if parent_obj_id.is_null():
#         print("Object doesn't have a parent")
#     else:
#         print(f'Parent object ID: {parent_obj_id}')

# This script gets a specified behaviour data from a specified behaviour of the specified object
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     obj_id = mv.get_objects()[0]
#     basic_beh = bv.get_behaviour_by_name(obj_id, 'Basic')
#     type_selectable_data = bv.get_behaviour_data(basic_beh, 'type_selectable')
#     print(type_selectable_data)

# This script gets a list of objects in the specified behaviour data range of the specified behaviour
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     rig_infos = bv.get_behaviours('RigInfo')
#     if len(rig_infos) == 0:
#         scene.warning('No Rig Info objects found in the scene')
#         return
#     rig_info = rig_infos[0]
#     rig_objects = bv.get_behaviour_objects_range(rig_info, 'rig_objects')
#     print(f"Number of rig objects = {len(rig_objects)}")

# csc.model.ClusterEditor Class
# Allows editing of scene data clusters.

# Methods:
# add_cluster(self: csc.model.ClusterEditor, inserted_ids: List[csc.model.DataId], name: str = "") → int
#   Adds a new cluster with a list of data IDs, returning the cluster ID.

# add_data_to_cluster(self: csc.model.ClusterEditor, cluster_index: int, inserted_ids: List[csc.model.DataId]) → None
#   Adds data to a specified cluster.

# bind_clusters(self: csc.model.ClusterEditor, cluster_id_first: int, cluster_id_second: int) → None
#   Binds two clusters together.

# cluster_by_data(self: csc.model.ClusterEditor, data_id: csc.model.DataId) → int
#   Retrieves the cluster ID associated with a given data ID.

# remove_cluster(self: csc.model.ClusterEditor, cluster_id: int) → None
#   Removes a cluster by its ID.

# remove_data_from_cluster(self: csc.model.ClusterEditor, data_id: csc.model.DataId) → None
#   Removes data from a specified cluster.

# set_cluster_name(self: csc.model.ClusterEditor, cluster_id: int, name: str) → None
#   Sets the name of a specified cluster.

# unbind_cluster(self: csc.model.ClusterEditor, cluster_id: int) → None
#   Unbinds a cluster.

# unbind_clusters(self: csc.model.ClusterEditor, cluster_id_first: int, cluster_id_second: int) → None
#   Unbinds two clusters.

# Example usage:
# Empty space here


# csc.model.CustomSelectionPolicy Class
# Represents an enumeration for custom selection policies used to define the selection behavior of entities.

# Members:
# Default = <CustomSelectionPolicy.Default: 0>
#   The entity is selected along with other entities.

# Single = <CustomSelectionPolicy.Single: 1>
#   The entity is selected only if the selection contains only this entity.

# SingleType = <CustomSelectionPolicy.SingleType: 2>
#   The entity is selected only if the selection contains only entities of the same type.

# Properties:
# name → str
#   Retrieves the name of the selection policy.

# value → int
#   Retrieves the value of the selection policy.

# Example usage:
# Empty space here


# csc.model.Data Class
# Represents any special type of data that can be used in update calculations or as properties of behaviors.

# Properties:
# id -> csc.model.DataId
#   Gets or sets the unique identifier of the data.

# object_id -> csc.model.ObjectId
#   Gets or sets the associated object ID for the data.

# name -> str
#   Gets or sets the name of the data.

# mode -> csc.model.DataMode
#   Gets or sets the mode of the data.

# enum_name -> str
#   Gets or sets the enumeration name if the data is of an enumerated type.

# Example usage:
# Empty space here


# csc.model.DataEditor Class
# The DataEditor class allows for editing scene data and their properties.

# Methods:
# add_constant_data(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) → csc.model.Data
#   Adds a constant data with a specific value and returns a Data object.
# add_constant_data(self: csc.model.DataEditor, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) → csc.model.Data
#   Adds a constant data with a specified ID and returns a Data object.

# add_constant_setting(self: csc.model.DataEditor, arg0: str, arg1: Union[bool, int]) → csc.model.Setting
#   Adds a constant setting with a specified value and returns a Setting object.
# add_constant_setting(self: csc.model.DataEditor, name: str, value: Union[bool, int], id: csc.model.SettingId) → csc.model.Setting
#   Adds a constant setting with a specified ID and value, returning a Setting object.

# add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) → csc.model.Data
#   Adds data to the specified object and returns a Data object.
# add_data(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, mode: csc.model.DataMode, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], id: csc.model.DataId) → csc.model.Data
#   Adds data to the specified object with a specific ID and returns a Data object.

# add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) → csc.model.Setting
#   Adds a setting to the specified object and returns a Setting object.
# add_setting(self: csc.model.DataEditor, object_id: csc.model.ObjectId, name: str, value: Union[bool, int], mode: csc.model.SettingMode, id: csc.model.SettingId) → csc.model.Setting
#   Adds a setting to the specified object with a specific ID and returns a Setting object.

# clusters_editor(self: csc.model.DataEditor) → ClusterEditor
#   Returns the ClusterEditor instance for managing clusters.

# copy_data(self: csc.model.DataEditor, from_to: List[Tuple[csc.model.DataId, csc.model.DataId]]) → None
#   Copies data between specified DataIds.

# delete_data(self: csc.model.DataEditor, id: csc.model.DataId) → None
#   Deletes data with the specified DataId.

# delete_setting(self: csc.model.DataEditor, id: csc.model.SettingId) → None
#   Deletes a setting with the specified SettingId.

# set_animation_size(self: csc.model.DataEditor, size: int) → None
#   Sets the animation size to the specified integer value.

# set_data_enum_name(self: csc.model.DataEditor, id: csc.model.DataId, enum_name: str) → None
#   Sets the enumeration name for data specified by its DataId.

# set_data_only_key(self: csc.model.DataEditor, id: csc.model.DataId, only_key: bool) → None
#   Specifies whether the data should only use keyframes.

# set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) → None
#   Sets the value of the data specified by its DataId.
# set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frames: Set[int], value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) → None
#   Sets the value of the data for specified frames.
# set_data_value(self: csc.model.DataEditor, id: csc.model.DataId, frame: int, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]) → None
#   Sets the value of the data for a single frame.

# set_data_view_state(self: csc.model.DataEditor, id: csc.model.DataId, view_state: csc.model.DataModifyToView) → None
#   Sets the view state of the data specified by its DataId.

# set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int]) → None
#   Sets the value of the setting specified by its SettingId.
# set_setting_value(self: csc.model.DataEditor, id: csc.model.SettingId, value: Union[bool, int], frame: int) → None
#   Sets the value of the setting for a specific frame.

# Example usage:
# This script adds a new data node in the specified object
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     obj_id = mv.get_objects()[0]
#
#     def mod(model, update, scene):
#         de = model.data_editor()
#         # Add an Animation type Vector3f data node
#         new_node = de.add_data(obj_id, 'NewNode', csc.model.DataMode.Animation, [5.0, 5.0, 5.0])
#         print(f"New node: {new_node}")
#     scene.modify('Add data', mod)

# csc.model.DataMode Class
# Represents the basic types of data modes: Static and Animation.

# Members:
# Static = <DataMode.Static: 0>
# Animation = <DataMode.Animation: 1>

# Example usage:
# Empty space here


# csc.model.DataModifyToView Class
# Enum that represents the possible modifications for data views: None and Degrees.

# Members:
# None = <DataModifyToView.None: 0>
# Degrees = <DataModifyToView.Degrees: 1>

# Example usage:
# Empty space here


# csc.model.DataViewer Class
# The DataViewer class allows viewing scene data and their properties.

# Methods:
# get_all_data_id(self: csc.model.DataViewer, object_id: csc.model.ObjectId) → List[csc.model.DataId]
#   Retrieves all DataIds associated with the specified ObjectId.

# get_all_settings_id(self: csc.model.DataViewer, object_id: csc.model.ObjectId) → List[csc.model.SettingId]
#   Retrieves all SettingIds associated with the specified ObjectId.

# get_animation_size(self: csc.model.DataViewer) → int
#   Returns the size of the animation.

# get_behaviour_default_data_value(self: csc.model.DataViewer, id: csc.Guid, name: str) → Optional[Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]]
#   Returns the default value of a behaviour for the given ID and name.

# get_behaviour_property(self: csc.model.DataViewer, id: csc.Guid, name: str, frame: int) → Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
#   Retrieves the property of a behaviour for a given frame.
# get_behaviour_property(self: csc.model.DataViewer, id: csc.Guid, name: str) → Union[bool, int]
#   Retrieves the property of a behaviour for the given ID and name.

# get_data(self: csc.model.DataViewer, id: csc.model.DataId) → csc.model.Data
#   Retrieves the data for the specified DataId.

# get_data_id(self: csc.model.DataViewer, id: csc.model.ObjectId, name: str) → csc.model.DataId
#   Retrieves the DataId for the given ObjectId and name.

# get_data_value(self: csc.model.DataViewer, id: csc.model.DataId) → Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
#   Retrieves the value of the data for the specified DataId.
# get_data_value(self: csc.model.DataViewer, arg0: csc.model.DataId, arg1: int) → Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
#   Retrieves the value of the data for a specific frame.

# get_setting(self: csc.model.DataViewer, id: csc.model.SettingId) → csc.model.Setting
#   Retrieves the setting for the specified SettingId.

# get_setting_id(self: csc.model.DataViewer, id: csc.model.ObjectId, name: str) → csc.model.SettingId
#   Retrieves the SettingId for the given ObjectId and name.

# get_setting_value(self: csc.model.DataViewer, id: csc.model.SettingId) → Union[bool, int]
#   Retrieves the value of the setting for the specified SettingId.
# get_setting_value(self: csc.model.DataViewer, setting_id: csc.model.SettingId, position: int) → Union[bool, int]
#   Retrieves the value of the setting for a specific frame.

# union_get_data_value(self: csc.model.DataViewer, data_id: csc.model.DataId, frame: int = 0) → Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]]
#   Retrieves the union value of data for a given frame and DataId.

# Example usage:
# This script gets the data value of the specified DataId
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     dv = mv.data_viewer()
#     obj_id = mv.get_objects()[0]
#     basic_beh = bv.get_behaviour_by_name(obj_id, 'Basic')
#     type_selectable_data = bv.get_behaviour_data(basic_beh, 'type_selectable')
#     data_value = dv.get_data_value(type_selectable_data)
#     print(data_value)


# csc.model.DataId Class
# Represents a unique identifier for data within the Cascadeur model.

# Methods:
# is_null(self: csc.model.DataId) → bool
#   Checks if the DataId is null, indicating it does not reference any data.

# static null() → csc.model.DataId
#   Returns a null DataId, which can be used to represent the absence of a valid data reference.

# to_string(self: csc.model.DataId) → str
#   Converts the DataId to its string representation.

# Example usage:
# Empty space here


# csc.model.DataMode Class
# Represents the modes for data types in Cascadeur: Static and Animation.

# Members:
# Static = <DataMode.Static: 0>
#   Indicates that the data is static and does not change over time.
# Animation = <DataMode.Animation: 1>
#   Indicates that the data is part of an animation sequence.

# Example usage:
# Empty space here


# csc.model.DataModifyToView Class
# Enumerates the types of modifications for viewing data.

# Members:
# None = <DataModifyToView.None: 0>
#   Indicates no modification to the view.
# Degrees = <DataModifyToView.Degrees: 1>
#   Modifies the view to display data in degrees.

# Example usage:
# Empty space here


# csc.model.DescriptionTerm Class
# Represents a descriptive term that can be used for various descriptive purposes within the model.

# Example usage:
# Empty space here


# csc.model.HyperedgeId Class
# Represents a unique identifier for hyperedges within the Cascadeur model.

# Methods:
# is_null(self: csc.model.HyperedgeId) → bool
#   Checks if the HyperedgeId is null, indicating it does not reference any hyperedge.

# static null() → csc.model.HyperedgeId
#   Returns a null HyperedgeId, which can be used to represent the absence of a valid hyperedge reference.

# to_string(self: csc.model.HyperedgeId) → str
#   Converts the HyperedgeId to its string representation.

# Example usage:
# Empty space here


# csc.model.IKFKTag Class
# Represents an IKFK tag within the Cascadeur model, used for identifying IK and FK points.

# Example usage:
# Empty space here


# csc.model.LerpMode Class
# Enumerates the modes for linear interpolation within Cascadeur.

# Members:
# none = <LerpMode.none: 0>
#   Indicates no interpolation.
# linear = <LerpMode.linear: 1>
#   Indicates linear interpolation.
# spherical = <LerpMode.spherical: 2>
#   Indicates spherical interpolation.

# Example usage:
# Empty space here


# csc.model.ModelEditor Class
# Provides basic methods for editing the scene model in Cascadeur.

# Methods:
# add_object(self: csc.model.ModelEditor) → csc.model.ObjectId
#   Adds a new object to the scene and returns its ObjectId.
# add_object(self: csc.model.ModelEditor, id: csc.model.ObjectId) → csc.model.ObjectId
#   Adds a new object with the specified ObjectId to the scene.

# behaviour_editor(self: csc.model.ModelEditor) → BehaviourEditor
#   Returns an instance of the BehaviourEditor for modifying object behaviours.

# data_editor(self: csc.model.ModelEditor) → DataEditor
#   Returns an instance of the DataEditor for editing object data.

# delete_objects(self: csc.model.ModelEditor, ids: Set[csc.model.ObjectId], close_connections: bool = True) → None
#   Deletes the specified objects and optionally closes any connections related to them.

# get_viewer(self: csc.model.ModelEditor) → DataViewer
#   Returns an instance of the DataViewer for viewing object data.

# increase_animation_size_by_setting_key(self: csc.model.ModelEditor, animation_size: int) → None
#   Increases the animation size by a specified key value.

# init_default_constants(self: csc.model.ModelEditor) → None
#   Initializes default constants for the model.

# layers(self: csc.model.ModelEditor) → csc.layers.Layers
#   Returns the Layers object associated with the ModelEditor.

# layers_editor(self: csc.model.ModelEditor) → csc.layers.Editor
#   Returns the LayersEditor object for modifying layers.

# layers_selector(self: csc.model.ModelEditor) → csc.layers.Selector
#   Returns the LayersSelector object for selecting layers.

# move_obj_ids_in_layers(self: csc.model.ModelEditor, objIds: List[csc.model.ObjectId], layer_id: csc.Guid) → None
#   Moves specified object IDs into a specific layer.

# move_objects_to_layer(self: csc.model.ModelEditor, ids: List[csc.model.ObjectId], target_layer_id: csc.Guid) → None
#   Moves specified objects to a target layer.

# set_fixed_interpolation_if_need(self: csc.model.ModelEditor, actuals: Set[csc.model.DataId], frame: int, ignore_locked: bool = False) → None
#   Sets fixed interpolation for the specified frames if needed.

# set_object_name(self: csc.model.ModelEditor, id: csc.model.ObjectId, name: str) → None
#   Sets the name of the object specified by its ObjectId.

# set_object_type_name(self: csc.model.ModelEditor, id: csc.model.ObjectId, name: str) → None
#   Sets the type name of the object specified by its ObjectId.

# Example usage:
# This script returns csc.layers.Selector
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         ls = model.layers_selector()
#     scene.modify('Get Layers Selector', mod)

# This script creates a new track in the scene's root folder
# import csc
#
# def run(scene):
#     lv = scene.layers_viewer()
#     root_folder = lv.root_id()
#     def mod(model, update, scene):
#         le = model.layers_editor()
#         # Create new layer
#         layer_id = le.create_layer('Test_layer', root_folder)
#         print(f"Created track id: {layer_id}")
#     scene.modify('Create new track', mod)

# This script prints the IDs of all selected animation tracks
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     def mod(model, update, scene):
#         ls = model.layers_selector()
#         # Get a list of all selected tracks
#         selected_layer_ids = ls.all_included_layer_ids()
#         if selected_layer_ids:
#             for layer in selected_layer_ids:
#                 print(f'Selected track ID: {layer}')
#         else:
#             print('No tracks were selected')
#     scene.modify('Get selected tracks', mod)

# This script sets a new name for the specified object
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     obj_id = mv.get_objects()[0]
#     def mod(model, update, scene):
#         model.set_object_name(obj_id, "NewObjectName")
#     scene.modify('Set new obj name', mod)

# This script moves first found object into the second object's assigned track
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     lv = scene.layers_viewer()
#     obj_ids = mv.get_objects()
#     obj1_id = obj_ids[0]
#     obj2_id = obj_ids[1]
#
#     def mod(model, update, scene):
#         obj2_layer = lv.layer_id_by_obj_id(obj2_id)
#         model.move_objects_to_layer([obj1_id], obj2_layer)
#     scene.modify('Move object to track', mod)

# This script gets the csc.layers.Layers object that contains all folders and layers in the scene
# import csc
#
# def run(scene):
#     def mod(model, update, scene):
#         # Get csc.layers.Layers
#         layers_obj = model.layers()
#         # Get a mapped dictionary with FolderID and Folder objects
#         folder_map = layers_obj.folders()
#         # Get a LayersContainer object
#         layers_container = layers_obj.layers()
#     scene.modify('Get csc.layers.Layers object', mod)

# This script deletes the selected objects in the scene
# import csc
#
# def run(scene):
#     # Get only selected objects in the scene
#     selected_objs = [sid for sid in scene.selector().selected().ids if isinstance(sid, csc.model.ObjectId)]
#     def mod(model, update, scene_updater):
#         # Delete the specified objects
#         model.delete_objects(selected_objs)
#         frame_no = scene.get_current_frame()
#         scene_updater.generate_update()
#         scene_updater.run_update(set(), frame_no)
#     scene.modify_update('Delete objects', mod)


# csc.model.ModelViewer Class
# Represents basic methods to view the scene model.

# Methods:
# behaviour_viewer(self: csc.model.ModelViewer) → csc.model.BehaviourViewer
#   Returns an instance of the BehaviourViewer associated with the model viewer.
#
# data_viewer(self: csc.model.ModelViewer) → csc.model.DataViewer
#   Returns an instance of the DataViewer associated with the model viewer.
#
# get_object_name(self: csc.model.ModelViewer, id: csc.model.ObjectId) → str
#   Retrieves the name of an object given its ObjectId.
#
# get_object_type_name(self: csc.model.ModelViewer, id: csc.model.ObjectId) → str
#   Retrieves the type name of an object given its ObjectId.
#
# get_objects(self: csc.model.ModelViewer) → List[csc.model.ObjectId]
#   Returns a list of all ObjectIds present in the scene.
#
# get_objects(self: csc.model.ModelViewer, name: str) → List[csc.model.ObjectId]
#   Returns a list of ObjectIds that match the given name.
#
# Example usage:
# This script showcases the methods of csc.model.ModelViewer class
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     # Get BehaviourViewer
#     bv = mv.behaviour_viewer()
#     # Get DataViewer
#     dv = mv.data_viewer()
#     # Get all Object IDs in the scene
#     obj_ids = mv.get_objects()
#     # Get all Object IDs matching the specified name in the scene
#     specific_obj_ids = mv.get_objects('Cylinder(0)')
#     if obj_ids:
#         obj_id = obj_ids[0]
#         obj_name = mv.get_object_name(obj_id)
#         obj_type_name = mv.get_object_type_name(obj_id)
#         print(f'Object name: {obj_name}')
#         print(f"Object type: {obj_type_name}")


# csc.model.ObjectId Class
# Represents an identifier for objects within the model.

# Methods:
# is_null(self: csc.model.ObjectId) → bool
#   Checks whether the ObjectId is null.
#
# static null() → csc.model.ObjectId
#   Returns a null ObjectId, which can be used to indicate the absence of a valid identifier.
#
# to_string(self: csc.model.ObjectId) → str
#   Converts the ObjectId into a string format.
#
# Example usage:
# This script showcases the methods of csc.model.ObjectId class
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     obj_id = mv.get_objects()[0]
#     # Get null Object ID
#     null_obj_id = csc.model.ObjectId.null()
#     # Convert Object ID into a string
#     obj_id_to_string = obj_id.to_string()
#     print(f"Given Object ID is null: {null_obj_id}")
#     print(f"Object ID converted to string: {obj_id_to_string}")


# csc.model.PathName Class
# Implements a hierarchical name structure.

# Methods:
# empty(self: csc.model.PathName) → bool
#   Checks whether the PathName is empty.
#
# full_path(self: csc.model.PathName) → List[str]
#   Retrieves the full hierarchical path as a list of strings.
#
# get_namespace(self: csc.model.PathName) → str
#   Retrieves the namespace of the PathName.
#
# set_namespace(self: csc.model.PathName, namespace: str) → None
#   Sets the namespace for the PathName.
#
# to_string(self: csc.model.PathName) → str
#   Converts the PathName into a string format.
#
# static get_path_name(obj_id: csc.model.ObjectId, mv: domain::scene::model::ModelViewer, beh_name: str = 'Joint') → csc.model.PathName
#   Returns a PathName for the given ObjectId and ModelViewer, optionally filtering by behavior name.
#
# static get_path_names(arg0: Dict[str, str]) → Dict[str, csc.model.PathName]
#   Returns a dictionary of PathNames based on the provided input.
#
# static get_path_names_by_behavior(arg0: str, arg1: domain::scene::model::ModelViewer) → Dict[csc.model.PathName, csc.model.ObjectId]
#   Returns a dictionary of PathNames and their associated ObjectIds based on a specific behavior.
#
# Properties:
# name -> str
#   Gets or sets the name of the PathName.
#
# path -> List[str]
#   Gets or sets the path of the PathName as a list of strings.
#
# Example usage:
# Empty space here


# csc.model.Setting Class
# Represents a setting value, which can be an integer or boolean used in update calculations.

# Properties:
# id -> csc.model.DataId
#   Gets the DataId associated with the setting.
#
# name -> str
#   Gets or sets the name of the setting.
#
# object_id -> csc.model.ObjectId
#   Gets or sets the ObjectId associated with the setting.
#
# type -> int
#   Gets or sets the type of the setting.
#
# mode -> csc.model.SettingMode
#   Gets or sets the mode of the setting.
#
# Example usage:
# Empty space here


# csc.model.SettingFunctionId Class
# Represents a unique identifier for a setting function.

# Methods:
# is_null(self: csc.model.SettingFunctionId) → bool
#   Checks whether the SettingFunctionId is null.
#
# static null() → csc.model.SettingFunctionId
#   Returns a null SettingFunctionId, which can be used to indicate the absence of a valid identifier.
#
# to_string(self: csc.model.SettingFunctionId) → str
#   Converts the SettingFunctionId into a string format.
#
# Example usage:
# Empty space here


# csc.model.SettingId Class
# Represents a unique identifier for a setting.

# Methods:
# is_null(self: csc.model.SettingId) → bool
#   Checks whether the SettingId is null.
#
# static null() → csc.model.SettingId
#   Returns a null SettingId, which can be used to indicate the absence of a valid identifier.
#
# to_string(self: csc.model.SettingId) → str
#   Converts the SettingId into a string format.
#
# Example usage:
# Empty space here


# csc.model.SettingMode Class
# Enumerates the basic types of data: Static and Animation.

# Members:
# Static = <SettingMode.Static: 0>
# Animation = <SettingMode.Animation: 1>

# Example usage:
# Empty space here


# csc.domain.Asset Class
# Represents an object resource such as meshes or textures.

# Properties:
# id -> csc.Guid
#   Gets or sets the unique identifier of the asset.
#
# Example usage:
# Empty space here


# csc.domain.IMessageHandler Interface
# Represents an interface for handling messages.

# Example usage:
# Empty space here


# csc.domain.Pivot Class
# Represents basic methods for manipulating pivots in a scene.

# Methods:
# center_of_top_objects(self: csc.domain.Pivot, arg0: Callable[[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], numpy.ndarray[numpy.float32[3, 1]]]) → numpy.ndarray[numpy.float32[3, 1]]
#   Centers the pivot of the top objects in the scene.
#
# clear_current_frame_pivot(self: csc.domain.Pivot) → None
#   Clears the pivot set for the current frame.
#
# clear_interval_pivots(self: csc.domain.Pivot) → None
#   Clears the pivots set over a range of frames.
#
# origin(self: csc.domain.Pivot) → numpy.ndarray[numpy.float32[3, 1]]
#   Returns the origin of the pivot.
#
# origin(self: csc.domain.Pivot, frame: int) → numpy.ndarray[numpy.float32[3, 1]]
#   Returns the origin of the pivot for a specific frame.
#
# origin(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) → numpy.ndarray[numpy.float32[3, 1]]
#   Returns the origin of the pivot for a specific frame and pivot state.
#
# remember_current_frame_pivot(self: csc.domain.Pivot) → None
#   Remembers the current frame's pivot position.
#
# remember_interval_pivots(self: csc.domain.Pivot) → None
#   Remembers the pivot positions over a range of frames.
#
# rotation(self: csc.domain.Pivot) → csc.math.Quaternion
#   Returns the rotation of the pivot.
#
# rotation(self: csc.domain.Pivot, frame: int) → csc.math.Quaternion
#   Returns the rotation of the pivot for a specific frame.
#
# rotation(self: csc.domain.Pivot, frame: int, pivot: csc.domain.StatePivot) → csc.math.Quaternion
#   Returns the rotation of the pivot for a specific frame and pivot state.
#
# select(self: csc.domain.Pivot, entity_id: Union[csc.model.ObjectId, csc.domain.Tool_object_id]) → None
#   Selects an entity by its ObjectId or Tool object ID.
#
# Example usage:
# Empty space here


# csc.domain.ProcessorsStorage Class
# The class serves to contain entity 3D processors.

# Example usage:
# Empty space here


# csc.domain.Scene Class
# Root class that represents a scene and provides methods for modifying or observing it.

# Methods:
# assets_manager(self: csc.domain.Scene) → domain::scene::AssetsManager
#   Retrieves the AssetsManager associated with the scene.
#
# behaviour_viewer(self: csc.domain.Scene) → csc.model.BehaviourViewer
#   Retrieves the BehaviourViewer associated with the scene.
#
# data_viewer(self: csc.domain.Scene) → csc.model.DataViewer
#   Retrieves the DataViewer associated with the scene.
#
# error(self: csc.domain.Scene, arg0: str) → None
#   Logs an error message to the scene's event log.
#
# get_current_frame(self: csc.domain.Scene, clamp_animation: bool = True) → int
#   Retrieves the current frame of the scene, with an option to clamp the animation.
#
# get_event_log_or_null(self: csc.domain.Scene) → object
#   Retrieves the event log of the scene or returns null if it doesn't exist.
#
# get_layers_selector(self: csc.domain.Scene) → csc.layers.Selector
#   Retrieves the layers selector for the scene.
#
# info(self: csc.domain.Scene, arg0: str) → None
#   Logs an informational message to the scene's event log.
#
# layers_viewer(self: csc.domain.Scene) → csc.layers.Viewer
#   Retrieves the LayersViewer associated with the scene.
#
# model_viewer(self: csc.domain.Scene) → csc.model.ModelViewer
#   Retrieves the ModelViewer associated with the scene.
#
# modify(self: csc.domain.Scene, name: str, func: function) → bool
#   Modifies the scene using a provided function.
#
# modify_update(self: csc.domain.Scene, name: str, func: function) → bool
#   Modifies the scene update using a provided function.
#
# modify_update_with_session(self: csc.domain.Scene, name: str, func: function) → bool
#   Modifies the scene update using a provided function within a session.
#
# modify_with_session(self: csc.domain.Scene, name: str, func: function) → bool
#   Modifies the scene using a provided function within a session.
#
# selector(self: csc.domain.Scene) → Selector
#   Retrieves the Selector for the scene.
#
# set_current_frame(self: csc.domain.Scene, frame: int) → None
#   Sets the current frame of the scene.
#
# set_event_log(self: csc.domain.Scene, message_handler: csc.domain.IMessageHandler) → None
#   Sets the event log handler for the scene.
#
# warning(self: csc.domain.Scene, arg0: str) → None
#   Logs a warning message to the scene's event log.

# Example usage:
# This script showcases the methods of csc.domain.Scene class
# import csc
#
# def run(scene):
#     # Initialize viewers and managers
#     am = scene.assets_manager()
#     lv = scene.layers_viewer()
#     mv = scene.model_viewer()
#     bv = mv.behaviour_viewer()
#     dv = bv.data_viewer()
#     # Get current frame int on the timeline
#     frame_no = scene.get_current_frame()
#     # Set new current frame on the timeline
#     new_frame = scene.set_current_frame(frame_no + 1)
#     null_obj_id = csc.model.ObjectId.null()
#
#     # Run Modify method
#     def mod(model, update, scene):
#         scene.error('Test error message')
#         scene.warning('Test warning message')
#         scene.info('Test info message')
#     scene.modify('Modify', mod)
#     # Run Modify Update method
#     def mod_upd(model, update, scene_updater):
#         scene_updater.generate_update()
#     scene.modify_update('Modify update', mod_upd)
#     # Run Modify with Session method
#     def mod_session(model, update, scene, session):
#         session.take_selector().select({null_obj_id}, null_obj_id)
#     scene.modify_with_session('Modify with session', mod_session)
#     # Run Modify Update with Session method
#     def mod_update_session(model, update, scene_updater, session):
#         session.take_selector().select({null_obj_id}, null_obj_id)
#         scene_updater.run_update({null_obj_id.data_id()}, frame_no)
#     scene.modify_update_with_session('Modify update with session', mod_update_session)


# csc.domain.SceneUpdater Class
# The SceneUpdater class rules the scene modification process. If the update changes, it should be regenerated. It also provides the option to run the update with specific data.

# Methods:
# generate_update(self: csc.domain.SceneUpdater) → None
#   Generates the update for the scene.
#
# run_update(self: csc.domain.SceneUpdater, local_ids: Set[csc.model.DataId], frame: int) → None
#   Runs the update for the scene with the specified local IDs and frame.
#
# run_update(self: csc.domain.SceneUpdater, local_ids: Set[csc.model.DataId], frames: csc.layers.index.FramesIndices) → None
#   Runs the update for the scene with the specified local IDs and frames.
#
# scene(self: csc.domain.SceneUpdater) → object
#   Retrieves the scene object associated with the updater.

# Example usage:
# This script demonstrates the use of the SceneUpdater class
# import csc
#
# def run(scene):
#     lv = scene.layers_viewer()
#     def mod1(model, update, scene_updater):
#         le = model.layers_editor()
#         get_scene = scene_updater.scene()
#         am = get_scene.assets_manager()
#         loc_id = csc.parts.Buffer.get().insert_object_by_path('objects/locator.casc',
#                                                               update.root().group_id(), model,
#                                                               am)
#         obj_track = lv.layer_id_by_obj_id(loc_id)
#         for frame in range(0, 6):
#             le.set_fixed_interpolation_or_key_if_need(obj_track, frame, True)
#         root_group = update.get_object_by_id(loc_id).root_group()
#         pos_node = root_group.node_deep('Position')
#
#         scene_updater.generate_update()
#         pos_node.set_value([5.0, 5.0, 5.0], 0)
#         scene_updater.run_update({pos_node.data_id()}, 0)
#
#     def mod2(model, update, scene_updater):
#         get_scene = scene_updater.scene()
#         am = get_scene.assets_manager()
#         loc_id = csc.parts.Buffer.get().insert_object_by_path('objects/locator.casc',
#                                                               update.root().group_id(), model,
#                                                               am)
#         root_group = update.get_object_by_id(loc_id).root_group()
#         pos_node = root_group.node_deep('Position')
#
#         scene_updater.generate_update()
#         for frame in range(3, 6):
#             pos_node.set_value([10.0, 10.0, 10.0], frame)
#         scene_updater.run_update({pos_node.data_id()}, csc.layers.index.FramesIndices.from_range(3, 5))
#
#     scene.modify_update('Scene update 1', mod1)
#     scene.modify_update('Scene update 2', mod2)


# csc.domain.Select Class
# Represents properties of the current selection state of the scene.

# Members:
# object_ids -> csc.model.ObjectId or csc.scene.Tool_object_id
#   Gets or sets the object IDs associated with the selection.
# pivot_id -> csc.model.ObjectId or csc.scene.Tool_object_id
#   Gets or sets the pivot ID of the selection.
# filter -> csc.scene.SelectorFilter
#   Gets or sets the filter used for selection.
# mode -> csc.scene.SelectorMode
#   Gets or sets the mode used for selection.
# types_filter -> str
#   Gets or sets the types filter used for selection.

# Example usage:
# Empty space here


# csc.domain.Selection Class
# Contains selected objects in the scene.

# Members:
# ids -> csc.model.ObjectId or csc.scene.Tool_object_id
#   Gets the IDs of the selected objects.

# Example usage:
# This script showcases the properties of csc.domain.Selection class
# import csc
#
# def run(scene):
#     selector = scene.selector()
#     selected = selector.selected()
#     obj_ids = selected.ids
#     for obj_id in obj_ids:
#         print(f"Selected Object ID: {obj_id}")


# csc.domain.SelectionChanger Class
# Contains basic methods and properties to operate on the currently selected scene objects.

# Methods:
# clear_selection(self: csc.domain.SelectionChanger) → None
#   Clears the current selection of objects.
#
# refresh_selection(self: csc.domain.SelectionChanger) → None
#   Refreshes the current selection of objects.
#
# select(self: csc.domain.SelectionChanger, select: csc.domain.Select) → None
#   Selects objects based on the provided selection criteria.
#
# select(self: csc.domain.SelectionChanger, ids: Set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id], filter: csc.domain.SelectorFilter, mode: csc.domain.SelectorMode, types_filter: Set[str], auto_pivot: bool = False) → None
#   Selects objects based on various parameters.

# Example usage:
# Empty space here


# csc.domain.Selector Class
# Contains basic methods and properties to operate on the currently selected scene objects.

# Methods:
# pivot(self: csc.domain.Selector) → Pivot
#   Retrieves the pivot object for the selection.
#
# select(self: csc.domain.Selector, select: csc.domain.Select) → None
#   Selects objects based on the provided selection criteria.
#
# select(self: csc.domain.Selector, ids: Set[Union[csc.model.ObjectId, csc.domain.Tool_object_id]], id: Union[csc.model.ObjectId, csc.domain.Tool_object_id], filter: csc.domain.SelectorFilter, mode: csc.domain.SelectorMode, type_filter: Set[str], auto_pivot: bool = False) → None
#   Selects objects based on various parameters.
#
# selected(self: csc.domain.Selector) → Selection
#   Retrieves the currently selected objects.

# Example usage:
# Empty space here


# csc.domain.SelectorFilter Class
# SelectorFilter enumerable defines various filters for selection.

# Members:
# Free = 0x00
#   Free filter with no restrictions.
# Selectable = 0x01
#   Filter that restricts selection to selectable objects.
# ObjectType = 0x02
#   Filter that restricts selection based on object type.
# Layer = 0x04
#   Filter that restricts selection based on layer.
# OnlySingle = 0x08
#   Filter that restricts selection to only a single object.
# Standart = Selectable | ObjectType | Layer
#   Standard filter combining Selectable, ObjectType, and Layer filters.
# Full = 0xFF
#   Full filter that includes all possible restrictions.

# Example usage:
# Empty space here


# csc.domain.SelectorMode Class
# SelectorMode enumerable defines different selection modes.

# Members:
# SingleSelection
#   Resets selection if new objects are selected and makes no changes if the same objects are reselected.
# MultiSelection
#   Allows multiple selections. If not all objects are selected, adds to the selection; otherwise, subtracts from it.
# NewSelection
#   Resets all previous selections and highlights the new selection.
# AdditionSelection
#   Adds the highlighted entities to the current selection.
# SubtractionSelection
#   Subtracts the highlighted entities from the current selection.

# Example usage:
# Empty space here


# csc.domain.Session Class

# Methods:
# set_current_frame(self: csc.domain.Session, frame: int) → None
#   Sets the current frame for the session.
#
# take_layers_selector(self: csc.domain.Session) → object
#   Retrieves the layers selector associated with the session.
#
# take_selector(self: csc.domain.Session) → object
#   Retrieves the selector associated with the session.

# Example usage:
# This script showcases the methods of csc.domain.Session class
# import csc
#
# def run(scene):
#     null_obj_id = csc.model.ObjectId.null()
#     def mod(model, update, scene, session):
#         session.set_current_frame(10)
#         session.take_selector().select({null_obj_id}, null_obj_id)
#     scene.modify('Session methods', mod)


# csc.domain.StatePivot Class
# Represents the basic types of pivot states in Cascadeur's domain.

# Members:
# Fixed = <StatePivot.Fixed: 0>
#   A fixed state.
# Moving = <StatePivot.Moving: 1>
#   A moving state.

# Example usage:
# Empty space here


# csc.domain.Tool_object_id Class
# Represents a unique identifier for a tool object within Cascadeur's domain.

# Methods:
# is_null(self: csc.domain.Tool_object_id) → bool
#   Checks whether the Tool_object_id is null.

# static null() → csc.domain.Tool_object_id
#   Returns a null Tool_object_id, which can be used to indicate the absence of a valid identifier.

# to_string(self: csc.domain.Tool_object_id) → str
#   Converts the Tool_object_id into a string format, useful for logging or exporting data.

# Example usage:
# Empty space here


# csc.math.Affine Class
# Represents an affine transformation in 3D space, defined by an AngleAxis.

# Properties:
# linear → numpy.ndarray[numpy.float32[3,3], flags.f_contiguous]
#   Gets the linear part of the affine transformation matrix.

# Example usage:
# Empty space here


# csc.math.AngleAxis Class
# Represents an angle and an axis for defining a rotation in 3D space.

# Properties:
# angle → float
#   Gets the angle of rotation.
# axis → numpy.ndarray[numpy.float32[3,1]]
#   Gets the axis of rotation.

# Example usage:
# Empty space here


# csc.math.Circle Class
# Represents a circle defined by a sphere and a normal vector.

# Properties:
# normal → numpy.ndarray[numpy.float32[3,1]]
#   Gets the normal vector of the circle.
# sphere → csc.math.Sphere
#   Gets the sphere that defines the circle.

# Example usage:
# Empty space here


# csc.math.OrthogonalTransform Class
# Implements an orthogonal transformation defined by position and rotation.

# Properties:
# position → numpy.ndarray[numpy.float32[3,1]]
#   Gets or sets the position of the transform.
# rotation → csc.math.Rotation
#   Gets or sets the rotation of the transform.

# Example usage:
# This script gets Orthogonal Transform values from the first found object in the scene
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#
#     def mod(model, update, scene):
#         # Get the first object from all objects in the scene
#         objects = mv.get_objects()
#         first_object_id = objects[0]
#
#         def mod(model, update, scene):
#             # Get object's transforms
#             obj_group = update.get_object_by_id(first_object_id).root_group()
#             obj_position = obj_group.node_deep('Position').value(0)
#             obj_rotation = obj_group.node_deep('Rotation').value(0)
#
#             # Get Orthogonal Transform from object transforms
#             ot = csc.math.OrthogonalTransform()
#             ot.position = obj_position
#             ot.rotation = obj_rotation.to_quaternion()
#
#             # Get transform point
#             transform_point_ot = csc.math.transform_point(ot, np.array([0.0, 50.0, 0.0], dtype=np.float32))
#             print(f"Orthogonal Transform: {transform_point_ot}")
#
#         scene.modify("Orthogonal Transform", mod)


# csc.math.ParametrizedLine Class
# Represents a parametrized line defined by a line and a normal vector.

# Methods:
# projection(self: csc.math.ParametrizedLine, arg0: numpy.ndarray[numpy.float32[3,1]]) → numpy.ndarray[numpy.float32[3,1]]
#   Projects a point onto the parametrized line.

# Example usage:
# Empty space here


# csc.math.Plane Class
# Represents a hyperplane defined by a normal vector and a point.

# Methods:
# projection(self: csc.math.Plane, arg0: numpy.ndarray[numpy.float32[3,1]]) → numpy.ndarray[numpy.float32[3,1]]
#   Projects a point onto the plane.

# Example usage:
# Empty space here


# csc.math.Quaternion Class
# Represents a quaternion for rotation calculations in 3D space.

# Properties:
# w → float
#   Gets the w component of the quaternion.
# x → float
#   Gets the x component of the quaternion.
# y → float
#   Gets the y component of the quaternion.
# z → float
#   Gets the z component of the quaternion.

# Methods:
# static from_two_vectors(arg0: numpy.ndarray[numpy.float32[3,1]], arg1: numpy.ndarray[numpy.float32[3,1]]) → csc.math.Quaternion
#   Creates a quaternion from two vectors.

# static identity() → csc.math.Quaternion
#   Returns an identity quaternion.

# inverse(self: csc.math.Quaternion) → csc.math.Quaternion
#   Computes the inverse of the quaternion.

# Example usage:
# This script showcases the methods of csc.math.Quaternion class
# import csc
# import numpy as np
#
# # Create a quaternion from two vectors
# quaternion = csc.math.Quaternion.from_two_vectors(np.array([1, 0, 0]), np.array([0, 1, 0]))
# print(f"Quaternion from v1 to v2: {quaternion}")
#
# # Get the identity quaternion
# identity_q = quaternion.identity()
# print(f"Identity Quaternion: {identity_q}")
#
# # Get the inverse quaternion
# inverse_q = quaternion.inverse()
# print(f"Inverse Quaternion: {inverse_q}")
#
# # Get scalar and vector components from a quaternion
# w_q = quaternion.w()
# x_q = quaternion.x()
# y_q = quaternion.y()
# z_q = quaternion.z()
# print(f"Components of quaternion: w({w_q}), x({x_q}), y({y_q}), z({z_q})")


# csc.math.Rotation Class
# Represents a rotation using Euler angles.

# Methods:
# static from_angle_axis(arg0: float, arg1: numpy.ndarray[numpy.float32[3,1]]) → csc.math.Rotation
#   Creates a Rotation from an angle and an axis.

# static from_euler(x: float, y: float, z: float) → csc.math.Rotation
#   Creates a Rotation from Euler angles.

# static from_quaternion(w: float, x: float, y: float, z: float) → csc.math.Rotation
#   Creates a Rotation from quaternion components.

# static from_rotation_matrix(arg0: numpy.ndarray[numpy.float32[3,3]]) → csc.math.Rotation
#   Creates a Rotation from a rotation matrix.

# to_angle_axis(self: csc.math.Rotation) → csc.math.AngleAxis
#   Converts the Rotation to an AngleAxis representation.

# to_euler_angles_x_y_z(self: csc.math.Rotation) → numpy.ndarray[numpy.float32[3,1]]
#   Converts the Rotation to Euler angles.

# to_quaternion(self: csc.math.Rotation) → csc.math.Quaternion
#   Converts the Rotation to a Quaternion.

# to_rotation_matrix(self: csc.math.Rotation) → numpy.ndarray[numpy.float32[3,3]]
#   Converts the Rotation to a rotation matrix.

# Example usage:
# This script showcases the methods of csc.math.Rotation class
# import csc
# import numpy as np
#
# # Create a rotation from Euler angles
# rotation_from_euler = csc.math.Rotation.from_euler((90, 45, 30))
# print(f"Rotation created from Euler angles: {rotation_from_euler.to_euler_angles_x_y_z()}")
#
# # Create angle-axis (csc.math.AngleAxis) from rotation
# angle_axis = rotation_from_euler.to_angle_axis()
# print(f"Angle-axis created from rotation: {angle_axis}")
#
# # Create rotation from axis and angle
# rotation = csc.math.Rotation.from_angle_axis(np.radians(90), np.array([0, 1, 0]))
# rotation2 = csc.math.Rotation.from_angle_axis(angle_axis)
# print(f"Rotation created from angle-axis: {rotation}, {rotation2}")
#
# # Convert the rotation to a quaternion
# quaternion = rotation.to_quaternion()
# print(f"Rotation converted to quaternion: {quaternion}")
#
# # Convert the quaternion to rotation
# rotation_from_quat = csc.math.Rotation.from_quaternion(0.5, 0.5, -0.5, -1)
# rotation_from_quat2 = csc.math.Rotation.from_quaternion(quaternion)
# print(f"Quaternion converted to rotation: {rotation_from_quat}, {rotation_from_quat2}")
#
# # Convert the rotation to Euler angles (in radians)
# euler = rotation.to_euler_angles()
# print(f"Euler angles: {euler}")
#
# # Convert the rotation to Euler angles (in degrees)
# euler_angles = rotation.to_euler_angles_x_y_z()
# print(f"Euler angles xyz: {np.degrees(euler_angles)}")
#
# # Convert the rotation to a rotation matrix
# rotation_matrix = rotation.to_rotation_matrix()
# print(f"Rotation matrix: {rotation_matrix}")
#
# # Convert the 3x3 rotation matrix to rotation
# rotation_from_matrix = csc.math.Rotation.from_rotation_matrix(rotation_matrix)
# print(f"Rotation: {rotation_from_matrix}")


# csc.math.ScaledTransform Class
# ScaledTransform class
# Implements transform with the scale possibility.

# Members:
# position -> Vector3f
#   Get or set position as a Vector3f object.
# rotation -> Rotation
#   Get or set rotation as a Rotation object.
# scale -> Vector3f
#   Get or set scale as a Vector3f object.

# Example usage:
# Empty space here


# csc.math.SizesInterval Class
# SizesInterval class
# Implements the sizes interval basic methods.

# Methods:
# static construct_in_right_order(first: int, second: int) → csc.math.SizesInterval
#   Constructs a SizesInterval object with the given values, ensuring the correct order.
# contains(self: csc.math.SizesInterval, i: int) → bool
#   Checks if the interval contains the given integer value.
# empty(self: csc.math.SizesInterval) → bool
#   Checks if the interval is empty.
# end(self: csc.math.SizesInterval) → int
#   Returns the end value of the interval.
# inside_interval_inclusive(self: csc.math.SizesInterval, number: int) → bool
#   Checks if a number is inside the interval, inclusive.
# static intersect_intervals(first: csc.math.SizesInterval, second: csc.math.SizesInterval) → csc.math.SizesInterval
#   Finds the intersection of two intervals.
# start(self: csc.math.SizesInterval) → int
#   Returns the start value of the interval.
# static union_overlaping_intervals(first: csc.math.SizesInterval, second: csc.math.SizesInterval) → csc.math.SizesInterval
#   Unions two overlapping intervals.

# Example usage:
# Empty space here


# csc.math.Sphere Class
# Sphere class
# Represents a sphere defined by a radius and a center point.

# Properties:
# center -> numpy.ndarray[numpy.float32[3,1]]
#   Get or set the center of the sphere.
# radius -> float
#   Get or set the radius of the sphere.

# Example usage:
# Empty space here


# csc.math.Triangle Class
# Triangle class
# Represents a triangle structure defined by three points.

# Members:
# point1 -> Vector3f
#   Get or set the first point of the triangle.
# point2 -> Vector3f
#   Get or set the second point of the triangle.
# point3 -> Vector3f
#   Get or set the third point of the triangle.

# Example usage:
# Empty space here


# csc.math.basic_transform_from_triangle Function
# Computes a basic orthogonal transform from a given triangle.
#
# Parameters:
# triangle: math::Triangle
#   The input triangle used for the transformation.
#
# Returns:
# csc.math.OrthogonalTransform
#   The computed orthogonal transform.

# Example usage:
# Empty space here


# csc.math.decompose_matrix Function
# Decomposes a 4x4 transformation matrix into a scaled transform.
#
# Parameters:
# arg0: numpy.ndarray[numpy.float32[4,4]]
#   A 4x4 matrix representing the transformation.
#
# Returns:
# domain::scene::model::data_struct::ScaledTransform
#   The decomposed scaled transform.

# Example usage:
# Empty space here


# csc.math.euler_angles_to_quaternion_x_y_z Function
# Converts a set of Euler angles to a quaternion representation.
#
# Parameters:
# euler_angles: numpy.ndarray[numpy.float32[3,1]]
#   The Euler angles (x, y, z) to be converted.
#
# Returns:
# csc.math.Quaternion
#   The resulting quaternion.

# Example usage:
# Empty space here


# csc.math.euler_flip Function
# Applies a flipping operation to Euler angles.
#
# Parameters:
# arg0: numpy.ndarray[numpy.float32[3,1]]
#   First set of Euler angles.
# arg1: numpy.ndarray[numpy.float32[3,1]]
#   Second set of Euler angles.
#
# Returns:
# csc.math.Rotation
#   The resulting rotation after flipping.

# Example usage:
# Empty space here


# csc.math.get_m3f_diag Function
# Extracts the diagonal elements of a 3x3 matrix.
#
# Parameters:
# matrix: numpy.ndarray[numpy.float32[3,3]]
#   The input 3x3 matrix.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The diagonal elements as a 3x1 vector.

# Example usage:
# Empty space here


# csc.math.ik_spline Function
# Computes an inverse kinematics spline given a set of points and quaternions.
#
# Parameters:
# arg0: numpy.ndarray[numpy.float32[3,1]]
#   Start position of the spline.
# arg1: List[numpy.ndarray[numpy.float32[3,1]]]
#   List of control points.
# arg2: List[csc.math.Quaternion]
#   List of quaternions for rotation.
# arg3: List[float]
#   Weights or constraints for the spline.
#
# Returns:
# Tuple[List[numpy.ndarray[numpy.float32[3,1]]], List[csc.math.Quaternion]]
#   Tuple containing the positions and quaternions along the spline.

# Example usage:
# Empty space here


# csc.math.ik_spline_2 Function
# A variant of the inverse kinematics spline computation.
#
# Parameters:
# arg0: numpy.ndarray[numpy.float32[3,1]]
#   Start position of the spline.
# arg1: List[numpy.ndarray[numpy.float32[3,1]]]
#   List of control points.
# arg2: List[csc.math.Quaternion]
#   List of quaternions for rotation.
# arg3: List[float]
#   Weights or constraints for the spline.
#
# Returns:
# Tuple[List[numpy.ndarray[numpy.float32[3,1]]], List[csc.math.Quaternion]]
#   Tuple containing the positions and quaternions along the spline.

# Example usage:
# Empty space here


# csc.math.inverse_transform_point Function
# Transforms a point by applying the inverse of a given orthogonal transform.
#
# Parameters:
# transform: math::OrthogonalTransform
#   The orthogonal transform to be inverted.
# point: numpy.ndarray[numpy.float32[3,1]]
#   The point to be transformed.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The transformed point.

# Example usage:
# Empty space here
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#
#     def mod(model, update, scene):
#         # Get the first object from all objects in the scene
#         objects = mv.get_objects()
#         first_object_id = objects[0]
#
#         # Get object's transforms
#         obj_group = update.get_object_by_id(first_object_id).root_group()
#         obj_position = obj_group.node_deep('Position').value(0)
#         obj_rotation = obj_group.node_deep('Rotation').value(0)
#
#         # Get Orthogonal Transform from object transforms
#         ot = csc.math.OrthogonalTransform()
#         ot.position = obj_position
#         ot.rotation = obj_rotation.to_quaternion()
#
#         # Transform the world position to position in object's local space
#         global_position = [0.0, 50.0, 0.0]
#         transform_point_ot = csc.math.inverse_transform_point(ot, global_position)
#         print(f"Inverse transform point from OT: {transform_point_ot}")
#     scene.modify("Inverse transform point", mod)

# csc.math.line_on_intersection_planes Function
# Finds the line of intersection between two planes.
#
# Parameters:
# arg0: csc.math.Plane
#   First plane.
# arg1: csc.math.Plane
#   Second plane.
#
# Returns:
# Optional[csc.math.ParametrizedLine]
#   The line of intersection, if it exists.

# Example usage:
# Empty space here


# csc.math.modify_position_by_matrix Function
# Modifies a position by applying a 3x3 matrix transformation.
#
# Parameters:
# matrix: numpy.ndarray[numpy.float32[3,3]]
#   The transformation matrix.
# position: numpy.ndarray[numpy.float32[3,1]]
#   The position to be modified.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The modified position.

# Example usage:
# Empty space here


# csc.math.point_on_intersection_planes Function
# Finds the point of intersection between two planes.
#
# Parameters:
# arg0: csc.math.Plane
#   First plane.
# arg1: csc.math.Plane
#   Second plane.
#
# Returns:
# Optional[numpy.ndarray[numpy.float32[3,1]]]
#   The point of intersection, if it exists.

# Example usage:
# Empty space here


# csc.math.project_point_on_basic_line Function
# Projects a point onto a basic line defined by a direction vector.
#
# Parameters:
# line_direction: numpy.ndarray[numpy.float32[3,1]]
#   The direction vector of the line.
# point: numpy.ndarray[numpy.float32[3,1]]
#   The point to be projected.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The projected point.

# Example usage:
# Empty space here


# csc.math.quaternion_to_euler_angles_x_y_z Function
# Converts a quaternion to Euler angles (x, y, z).
#
# Parameters:
# quaternion: csc.math.Quaternion
#   The quaternion to be converted.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The resulting Euler angles.

# Example usage:
# Empty space here


# csc.math.spheres_intersection Function
# Computes the intersection of two spheres, if it exists.
#
# Parameters:
# arg0: csc.math.Sphere
#   First sphere.
# arg1: csc.math.Sphere
#   Second sphere.
#
# Returns:
# Optional[csc.math.Circle]
#   The intersection circle, if it exists.

# Example usage:
# Empty space here


# csc.math.spheres_intersection_extended Function
# Computes an extended intersection of two spheres.
#
# Parameters:
# arg0: csc.math.Sphere
#   First sphere.
# arg1: csc.math.Sphere
#   Second sphere.
#
# Returns:
# Optional[csc.math.Circle]
#   The extended intersection circle, if it exists.

# Example usage:
# Empty space here


# csc.math.step_linear_func Function
# Computes a step function with a linear transition.
#
# Parameters:
# arg0: float
#   Start of the step.
# arg1: float
#   End of the step.
# arg2: float
#   Step position.
#
# Returns:
# float
#   The value after applying the step function.

# Example usage:
# Empty space here


# csc.math.transform_point Function
# Transforms a point using a specified transform or matrix.
#
# Overloads:
# 1. Transforms the point using an orthogonal transform.
# 2. Transforms the point using a 4x4 matrix.
#
# Parameters (overload 1):
# transform: math::OrthogonalTransform
#   The orthogonal transform to be applied.
# point: numpy.ndarray[numpy.float32[3,1]]
#   The point to be transformed.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The transformed point.
#
# Parameters (overload 2):
# matrix: numpy.ndarray[numpy.float32[4,4]]
#   The transformation matrix to be applied.
# point: numpy.ndarray[numpy.float32[3,1]]
#   The point to be transformed.
#
# Returns:
# numpy.ndarray[numpy.float32[3,1]]
#   The transformed point.

# Example usage:
# This script gets the transformed global position from the local space of a given Orthogonal Transform
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#
#     def mod(model, update, scene):
#         # Get the first object from all objects in the scene
#         objects = mv.get_objects()
#         first_object_id = objects[0]
#
#         # Get object's transforms
#         obj_group = update.get_object_by_id(first_object_id).root_group()
#         obj_position = obj_group.node_deep('Position').value(0)
#         obj_rotation = obj_group.node_deep('Rotation').value(0)
#         obj_matrix = obj_group.node_deep('Global Matrix').value(0)
#
#         # Get Orthogonal Transform from object transforms
#         ot = csc.math.OrthogonalTransform()
#         ot.position = obj_position
#         ot.rotation = obj_rotation.to_quaternion()
#
#         # Transform the local position in object's local space to world space position
#         local_position = [0.0, 50.0, 0.0]
#         transform_point_ot = csc.math.transform_point(ot, local_position)
#         transform_point_matrix = csc.math.transform_point(obj_matrix, local_position)
#         print(f"Transform point from OT: {transform_point_ot}")
#         print(f"Transform point from Matrix4x4: {transform_point_matrix}")
#     scene.modify("Transform point", mod)


# csc.math.transforms_difference Function
# Computes the difference between two orthogonal transforms.
#
# Parameters:
# first_orthogonal_transform: math::OrthogonalTransform
#   The first transform.
# second_orthogonal_transform: math::OrthogonalTransform
#   The second transform.
#
# Returns:
# csc.math.OrthogonalTransform
#   The resulting difference transform.

# Example usage:
# Empty space here


# csc.physics.PosMass Class
# PosMass class
# Represents a structure containing mass and position.

# Members:
# mass -> float
#   Get or set the mass value.
# position -> Vector3f
#   Get or set the position as a Vector3f object.

# Example usage:
# Empty space here


# csc.update.ActivityAttribute Class
# ActivityAttribute represents the activity of the data function.
# It should be a bool value. If true, the function is active; if false, inactive.
# If not set, it is always active. It is an input-only attribute.

# Example usage:
# Empty space here


# csc.update.ActualityAttribute Class
# ActualityAttribute shows whether data is actual at the start of the graph's update.
# It’s always an output attribute. It can be connected with setting functions.
# Note: Connections directly with data function activity are not supported; use the copy setting function instead.

# Example usage:
# Empty space here


# csc.update.ActualityAttributeId Class
# ActualityAttributeId is defined by the data ID.
# It’s an output-only attribute. Each data can be actual or non-actual at the start of the graph's update.

# Example usage:
# Empty space here


# csc.update.Connection Class
# Connection class
# Represents a connection between two attributes.

# Members:
# source -> AttributeId
#   Get or set the output AttributeId of the source.
# destination -> AttributeId
#   Get or set the input AttributeId of the destination.

# Example usage:
# Empty space here


# csc.update.ConstantDataAttribute Class
# ConstantDataAttribute represents an attribute of constant regular data.
# It’s always an output attribute and can be connected with setting functions or data functions activity.

# Example usage:
# Empty space here


# csc.update.ConstantDataAttributeId Class
# ConstantDataAttributeId is defined by the ConstantDatasId and the data id of the constant.
# Implements the ConstantDataAttributeId.

# Members:
# group_id -> csc.update.ConstantDatasId
#   Get ConstantDatasId.
# attribute_id -> csc.model.DataId
#   Get the data id (csc.model.DataId).

# Properties:
# group_id → csc.update.ConstantDatasId
#   Gets or sets the group id.
# attribute_id → csc.model.DataId
#   Gets or sets the attribute id.

# Example usage:
# Empty space here


# csc.update.ConstantDatas Class
# ConstantDatas represents a node of constant data. It is present in any place.

# Methods:
# add_data(self: csc.update.ConstantDatas, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3,1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3,3]], numpy.ndarray[numpy.float32[4,4]], csc.math.Quaternion, str, numpy.ndarray[bool[3,1]]]) → None
#   Adds a constant data entry with a given name and value.

# Example usage:
# Empty space here


# csc.update.ConstantDatasId Class
# ConstantDatasId is a GUID-based id. It is always equal to the group id where the constant will be used.

# Example usage:
# Empty space here


# csc.update.ConstantSettingAttribute Class
# ConstantSettingAttribute represents an attribute of a constant setting. It’s always an output attribute and can be connected with data functions.

# Example usage:
# Empty space here


# csc.update.ConstantSettingAttributeId Class
# ConstantSettingAttributeId is defined by the ConstantSettingId and the setting id of the constant.
# Implements the ConstantSettingAttributeId.

# Members:
# group_id -> csc.update.ConstantSettingsId
#   Get ConstantSettingsId.
# attribute_id -> csc.model.SettingId
#   Get csc.model.SettingId.

# Properties:
# group_id → csc.update.ConstantSettingsId
#   Gets or sets the group id.
# attribute_id → csc.model.SettingId
#   Gets or sets the attribute id.

# Example usage:
# Empty space here


# csc.update.ConstantSettings Class
# ConstantSettings represents a node of constant settings. It is present in any place.

# Methods:
# add_setting(self: csc.update.ConstantSettings, name: str, value: Union[bool, int]) → None
#   Adds a constant setting entry with a given name and value.

# Example usage:
# Empty space here


# csc.update.ConstantSettingsId Class
# ConstantSettingsId is a GUID-based id. It is always equal to the group id where the constant will be used.

# Example usage:
# Empty space here


# csc.update.ExternalProperties Class
# ExternalProperties represents a node of external properties. (E.g. is this update called during interpolation or not.) It is present in any place.

# Methods:
# property_outputs(self: csc.update.ExternalProperties) → List[csc.update.ExternalPropertyAttribute]
#   Retrieves a list of external property attributes.

# Example usage:
# Empty space here


# csc.update.ExternalPropertiesId Class
# ExternalPropertiesId is a GUID-based id. It is always equal to the group id where the external property will be used.

# Example usage:
# Empty space here


# csc.update.ExternalProperty Class
# ExternalProperty enum.
# This enumerates the basic types of ExternalProperty states: Fixation, IkFk, InterpolationType, IsInterpolation, AfterPhysics, IsKey.

# Members:
# Fixation = <ExternalProperty.Fixation: 0>
# IkFk = <ExternalProperty.IkFk: 1>
# InterpolationType = <ExternalProperty.InterpolationType: 2>
# IsInterpolation = <ExternalProperty.IsInterpolation: 3>
# fixation = <ExternalProperty.fixation: 4>
# IsKey = <ExternalProperty.IsKey: 5>

# Properties:
# name → str
#   Gets or sets the name of the property.
# value → int
#   Gets or sets the value of the property.

# Example usage:
# Empty space here


# csc.update.ExternalPropertyAttribute Class
# Represents an attribute of the external properties of the update.
# It’s always an output attribute. It is settings based and thus can be connected with setting functions or data functions activity.

# Example usage:
# Empty space here


# csc.update.ExternalPropertyAttributeId Class
# Represents the ExternalPropertyAttributeId which is defined by the ExternalPropertiesId and the value of the ExternalProperty enum.

# Members:
# node_id
#   Get GroupId
# property
#   Get ExternalProperty enum value

# Properties:
# node_id → csc.update.ExternalPropertiesId
#   Gets the node ID.
# property → csc.update.ExternalProperty
#   Gets the ExternalProperty enum value.

# Example usage:
# Empty space here


# csc.update.Group Class
# Represents a Group class in the update system.

# Methods:
# add_input(self: csc.update.Group, name: str) → csc.update.InterfaceAttribute
#   Adds an input attribute to the group with a given name.

# add_output(self: csc.update.Group, name: str) → csc.update.InterfaceAttribute
#   Adds an output attribute to the group with a given name.

# constant_datas(self: csc.update.Group) → csc.update.ConstantDatas
#   Returns a virtual node to access constant data.

# constant_settings(self: csc.update.Group) → csc.update.ConstantSettings
#   Returns a virtual node to access constant settings.

# create_group(self: csc.update.Group, name: str) → csc.update.Group
#   Creates a new subgroup within the current group.

# delete_node(self: csc.update.Group, node: csc.update.Node) → None
#   Deletes a node from the group.

# group(self: csc.update.Group, nodes: Set[csc.update.Node], name: str) → csc.update.Group
#   Creates a group using the given nodes.

# group_id(self: csc.update.Group) → csc.update.GroupId
#   Retrieves the ID of the group.

# has_node(self: csc.update.Group, name: str) → bool
#   Checks whether the group contains a node with the given name.

# input_interface_node(self: csc.update.Group) → csc.update.InterfaceNode
#   Returns the input interface node.

# interface_input(self: csc.update.Group, name: str) → csc.update.InterfaceAttribute
#   Gets the input interface attribute with the given name.

# interface_inputs(self: csc.update.Group) → List[csc.update.InterfaceAttribute]
#   Returns all input interface attributes.

# interface_node(self: csc.update.Group, direction: csc.Direction) → csc.update.InterfaceNode
#   Accesses the interface node based on the specified direction.

# interface_output(self: csc.update.Group, name: str) → csc.update.InterfaceAttribute
#   Gets the output interface attribute with the given name.

# interface_outputs(self: csc.update.Group) → List[csc.update.InterfaceAttribute]
#   Returns all output interface attributes.

# is_root(self: csc.update.Group) → csc.update.GroupId
#   Checks if the group is the root group.

# leaf_children(self: csc.update.Group) → Set[csc.update.Node]
#   Retrieves all leaf nodes, such as settings, data, and functions.

# node(self: csc.update.Group, name: str) → csc.update.Node
#   Gets a node by its name.

# node(self: csc.update.Group, node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) → csc.update.Node
#   Gets a node by its ID.

# node_deep(self: csc.update.Group, name: str) → csc.update.Node
#   Retrieves a node by name or ID recursively.

# node_with_type(self: csc.update.Group, type_name: str, name: str) → csc.update.Node
#   Finds a node by its name and type.

# node_with_type_deep(self: csc.update.Group, type_name: str, name: str) → csc.update.Node
#   Finds a node by its name and type recursively.

# nodes(self: csc.update.Group) → Set[csc.update.Node]
#   Gets all children nodes of the group (excluding their children).

# output_interface_node(self: csc.update.Group) → csc.update.InterfaceNode
#   Returns the output interface node.

# Example usage:
# This script retrieves a specified node from the specified object
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     object_id = mv.get_objects()[0]
#
#     def mod(model, update, scene):
#         root_group = update.get_object_by_id(object_id).root_group()
#         position_node = root_group.node_deep('Position')
#         print(f"Node id: {position_node}")
#     scene.modify_update('Get node', mod)


# csc.update.GroupAttributeId Class
# Represents a unique GroupAttributeId defined by a GroupId and a guid-based attribute ID.

# Members:
# group_id
#   Get GroupId
# attribute_id
#   Get csc.Guid - ID of the attribute

# Properties:
# group_id → csc.update.GroupId
#   Gets the GroupId.
# attribute_id → csc.Guid
#   Gets the GUID of the attribute.

# Example usage:
# Empty space here


# csc.update.GroupId Class
# Represents a unique identifier for a group within the update system.

# Methods:
# is_null(self: csc.update.GroupId) → bool
#   Checks if the GroupId is null.

# static null() → csc.update.GroupId
#   Returns a null GroupId, which can be used to indicate an invalid or unassigned group ID.

# to_string(self: csc.update.GroupId) → str
#   Converts the GroupId to a string representation.

# Example usage:
# Empty space here


# csc.update.HierarchyUpdate Class
# Represents a class for managing hierarchical updates and performing concrete operations with connections.

# Methods:
# add_connection(self: csc.update.HierarchyUpdate, connection: csc.update.Connection) → None
#   Adds a connection to the hierarchy update.

# remove_connection(self: csc.update.HierarchyUpdate, connection: csc.update.Connection) → None
#   Removes a connection from the hierarchy update.

# Example usage:
# Empty space here


# csc.update.InterfaceAttribute Class
# Represents a group attribute that can be connected to any attribute.

# Methods:
# group_attribute_id(self: csc.update.InterfaceAttribute) → csc.update.GroupAttributeId
#   Retrieves the group attribute ID associated with this interface attribute.

# other_side(self: csc.update.InterfaceAttribute) → csc.update.InterfaceAttribute
#   Gets the paired attribute (the opposite side of the attribute).

# set_name(self: csc.update.InterfaceAttribute, name: str) → None
#   Sets the name of the attribute.

# Example usage:
# Empty space here


# csc.update.InterfaceAttributeSide Class
# Represents an enumeration for the interface attribute side.

# Members:
# InterfaceSide = <InterfaceAttributeSide.InterfaceSide: 0>
# GroupSide = <InterfaceAttributeSide.GroupSide: 1>

# Properties:
# name → str
#   Gets the name of the enumeration value.
# value → int
#   Gets the integer value of the enumeration.

# Example usage:
# Empty space here


# csc.update.InterfaceId Class
# Represents a unique InterfaceId defined by a GroupId and a direction type (input or output).

# Members:
# group_id
#   Get GroupId
# direction
#   Get direction type (csc.Direction)

# Properties:
# group_id → csc.update.GroupId
#   Gets the GroupId.
# direction → csc.Direction
#   Gets the direction type of the node.

# Example usage:
# Empty space here


# csc.update.InterfaceNode Class
# Represents a node inside a group that manages connections with outside nodes.

# Methods:
# add_attribute(self: csc.update.InterfaceNode, name: str) → csc.update.InterfaceAttribute
#   Adds an attribute to the interface node.

# direction(self: csc.update.InterfaceNode) → csc.Direction
#   Returns the direction value for the interface node.

# interface_attributes(self: csc.update.InterfaceNode) → List[csc.update.InterfaceAttribute]
#   Gets the list of attributes for the interface node.

# move_attribute(self: csc.update.InterfaceNode, attribute: csc.update.InterfaceAttribute, position: int) → None
#   Moves an attribute to a specified position within the node.

# remove_attribute(self: csc.update.InterfaceNode, attribute: csc.update.InterfaceAttribute) → None
#   Removes an attribute from the interface node.

# Example usage:
# Empty space here


# csc.update.Node Class
# Node class represents a generic Node and implements methods that are common for all nodes.

# Methods:
# attributes(self: csc.update.Node, d: csc.Direction) → List[csc.update.NodeAttribute]
#   Array of all input and output attributes.

# full_name(self: csc.update.Node) → str
#   Name with all the parent nodes.

# has_input(self: csc.update.Node, name: str) → bool
#   Check if there is an input with such a name.

# has_output(self: csc.update.Node, name: str) → bool
#   Check if there is an output with such a name.

# id(self: csc.update.Node) → Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]
#   Get unique ID.

# input(self: csc.update.Node, name: str) → csc.update.NodeAttribute
#   Shortcut if node has only one input attribute.

# inputs(self: csc.update.Node) → List[csc.update.NodeAttribute]
#   Array of all the input attributes.

# is_active(self: csc.update.Node) → bool
#   Check whether it is active for current actuality states (see Additional functionality in csc.update.UpdateEditor).

# is_fictive(self: csc.update.Node) → bool
#   Whether it is a fictive node (constants, inputs, outputs of a group or external properties).

# name(self: csc.update.Node) → str
#   Get name.

# output(self: csc.update.Node, name: str) → csc.update.NodeAttribute
#   Shortcut if node has only one output attribute.

# outputs(self: csc.update.Node) → List[csc.update.NodeAttribute]
#   Array of all the output attributes.

# parent_group(self: csc.update.Node) → domain::update_editor::Group
#   Return parent group (where this group node is located).

# parent_object(self: csc.update.Node) → domain::update_editor::Object
#   Return object of the node. Will return null if this is not an update group.

# set_name(self: csc.update.Node, name: str) → None
#   Rename node.

# Example usage:
# Empty space here


# csc.update.NodeAttribute Class
# NodeAttribute represents a generic node attribute and the standard operations you can do with such an attribute.

# Methods:
# connect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) → None
#   Connect to another NodeAttribute.

# connected_attributes(self: csc.update.NodeAttribute) → List[csc.update.NodeAttribute]
#   Get connected attributes.

# connected_leaves(self: csc.update.NodeAttribute, get_only_first: bool = False) → List[csc.update.NodeAttribute]
#   Get connected leaves.

# connected_leaves_in_undirected_graph(self: csc.update.NodeAttribute) → List[csc.update.NodeAttribute]
#   Get connected leaves in an undirected graph.

# direction(self: csc.update.NodeAttribute) → csc.Direction
#   Get direction value.

# disconnect(self: csc.update.NodeAttribute) → None
# disconnect(self: csc.update.NodeAttribute, attribute: csc.update.NodeAttribute) → None
#   Disconnect attribute (Overloaded method).

# id(self: csc.update.NodeAttribute) → Union[csc.update.RegularFunctionAttributeId, csc.model.HyperedgeId, csc.update.RegularDataAttributeId, csc.update.ActualityAttributeId, csc.update.SettingFunctionAttributeId, csc.model.SettingId, csc.update.GroupAttributeId, csc.update.ExternalPropertyAttributeId, csc.update.ConstantDataAttributeId, csc.update.ConstantSettingAttributeId]
#   Get AttributeId.

# is_active(self: csc.update.NodeAttribute) → bool
#   Check if the attribute is active.

# name(self: csc.update.NodeAttribute) → str
#   Get name.

# node(self: csc.update.NodeAttribute) → domain::update_editor::Node
#   Get the associated node.

# Example usage:
# Empty space here


# csc.update.Object Class
# Object class represents an object node. Functionality is limited - it’s better to use update group node instead.

# Methods:
# add_input(self: csc.update.Object, name: str) → csc.update.InterfaceAttribute
#   Add an input attribute.

# add_output(self: csc.update.Object, name: str) → csc.update.InterfaceAttribute
#   Add an output attribute.

# object_id(self: csc.update.Object) → csc.model.ObjectId
#   Get object ID.

# root_group(self: csc.update.Object) → domain::update_editor::UpdateGroup
#   Get root group.

# Example usage:
# Empty space here


# csc.update.ObjectGroup Class
# ObjectGroup class represents an object group node.

# Methods:
# create_object(self: csc.update.ObjectGroup, name: str) → csc.update.Object
# create_object(self: csc.update.ObjectGroup, name: str, id: csc.model.ObjectId) → csc.update.Object
#   Create an object (Overloaded method).

# create_sub_object_group(self: csc.update.ObjectGroup, name: str) → csc.update.ObjectGroup
#   Create a sub object group.

# object_groups(self: csc.update.ObjectGroup) → Set[csc.update.ObjectGroup]
#   Get object groups.

# objects(self: csc.update.ObjectGroup) → Set[csc.update.Object]
#   Get objects.

# Example usage:
# Empty space here


# csc.update.RegularData Class
# RegularData class represents a node of a data.

# Methods:
# actuality(self: csc.update.RegularData) → csc.update.ActualityAttribute
#   Output attribute that provides actuality status.

# attribute(self: csc.update.RegularData, d: csc.Direction) → csc.update.RegularDataAttribute
#   Get attribute by direction.

# data_id(self: csc.update.RegularData) → csc.model.DataId
#   Get data ID.

# get_apply_euler_filter(self: csc.update.RegularData) → bool
#   Get apply euler filter.

# input(self: csc.update.RegularData) → csc.update.RegularDataAttribute
#   Get input attribute.

# is_actual(self: csc.update.RegularData) → bool
#   Check if this data is set to actual (see Additional functionality in csc.update.UpdateEditor).

# mode(self: csc.update.RegularData) → csc.model.DataMode
#   Check if data is Animation or Static.

# output(self: csc.update.RegularData) → csc.update.RegularDataAttribute
#   Get output attribute.

# remove_period(self: csc.update.RegularData) → None
#   Remove period in interpolation.

# set_actual(self: csc.update.RegularData, act: bool) → None
#   Set this data as actual (see Additional functionality in csc.update.UpdateEditor).

# set_apply_euler_filter(self: csc.update.RegularData, apply_euler_filter: bool) → None
#   Set apply euler filter.

# set_lerp_mode(self: csc.update.RegularData, mode: csc.model.LerpMode) → None
#   Set LERP mode.

# set_period(self: csc.update.RegularData, period: float) → None
#   Set period for interpolation.

# set_value(self: csc.update.RegularData, v: Union[bool, int, float, numpy.ndarray, csc.math.Rotation, csc.math.Quaternion, str], frame: int) → None
#   Set value (Overloaded method).

# set_view_state(self: csc.update.RegularData, view_state: csc.model.DataModifyToView) → None
#   Set view state.

# value(self: csc.update.RegularData) → Union[bool, int, float, numpy.ndarray, csc.math.Rotation, csc.math.Quaternion, str]
# value(self: csc.update.RegularData, frame: int) → Union[bool, int, float, numpy.ndarray, csc.math.Rotation, csc.math.Quaternion, str]
#   Get value (Overloaded method).

# Example usage:
# This script retrieves the values of the specified RegularData nodes
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     object_id = mv.get_objects()[0]
#     frame = 0
#
#     def mod(model, update, scene):
#         root_group = update.get_object_by_id(object_id).root_group()
#         position_node = root_group.node_deep('Position')
#         tpose_position_node = root_group.node_deep('T Pose Position')
#         # Get the value from an Animation type RegularData node
#         position_value = position_node.value(frame)
#         # Get the value from a Static type RegularData node
#         tpose_position_value = tpose_position_node.value()
#         print(f"Position: {position_value}")
#         print(f"Tpose Position: {tpose_position_value}")
#     scene.modify_update('Get values', mod)

# This script sets value of the specified RegularData node
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     object_id = mv.get_objects()[0]
#     frame = 0
#
#     def mod(model, update, scene):
#         de = model.data_editor()
#         anim_node = de.add_data(object_id, 'AnimationNode', csc.model.DataMode.Animation, 0.0).id
#         static_node = de.add_data(object_id, 'StaticNode', csc.model.DataMode.Static, True).id
#         # Set the value of an Animation type RegularData node
#         anim_node.set_value(240.455, frame)
#         # Set the value of a Static type RegularData node
#         static_node.set_value(False)
#     scene.modify('Set value', mod)

# csc.update.RegularDataAttribute Class
# RegularDataAttribute represents an attribute of a regular data. It can be connected with data functions.

# Example usage:
# Empty space here


# csc.update.RegularDataAttributeId Class
# RegularDataAttributeId is defined by the data ID. Data only has one input and one output attributes.

# Example usage:
# Empty space here


# csc.update.RegularFunction Class
# RegularFunction class represents a node that calculates the same operation done with datas.

# Methods:
# activity(self: csc.update.RegularFunction) → csc.update.ActivityAttribute
#   Activity attributes.

# arguments(self: csc.update.RegularFunction) → List[csc.update.RegularFunctionAttribute]
#   Its input arguments.

# decrease_vector(self: csc.update.RegularFunction, path: str, direction: csc.Direction) → None
#   Method that decreases vector attribute.

# func_id(self: csc.update.RegularFunction) → csc.model.HyperedgeId
#   Get ID.

# increase_vector(self: csc.update.RegularFunction, path: str, direction: csc.Direction) → csc.update.RegularFunctionAttribute
#   Method that increases vector attribute.

# is_convertible(self: csc.update.RegularFunction) → bool
#   Check whether this function will make it to the resulting data graph.

# remove_attribute(self: csc.update.RegularFunction, attribute: csc.update.RegularFunctionAttribute) → None
#   Remove a vector attribute.

# resize_vector_inputs(self: csc.update.RegularFunction, count: int, path: str) → None
#   Resize input vector attribute.

# resize_vector_outputs(self: csc.update.RegularFunction, count: int, path: str) → None
#   Resize output vector attribute.

# results(self: csc.update.RegularFunction) → List[csc.update.RegularFunctionAttribute]
#   Its output arguments.

# set_convertible(self: csc.update.RegularFunction, convertible: bool) → None
#   Set the state of the function, whether it will be used or not.

# Example usage:
# Empty space here


# csc.update.RegularFunctionAttribute Class
# RegularFunctionAttribute represents an attribute of a data function. It can be connected with data attributes.

# Example usage:
# Empty space here


# csc.update.RegularFunctionAttributeId Class
# RegularFunctionAttributeId is defined by the RegularFunctionId and the name of the attribute.

# Example usage:
# Empty space here


# csc.update.SettingData Class
# Represents a node that calculates the same operation done with settings.
# It can comprise bool or std::int8_t (Min: -128, Max: 127) value, please be careful when setting this.

# Methods:
# data_id(self: csc.update.SettingData) → csc.model.SettingId
#   Gets the unique identifier for the setting.

# output(self: csc.update.SettingData) → csc.update.SettingDataAttribute
#   Retrieves the output attribute of the setting.

# set_value(self: csc.update.SettingData, value: Union[bool, int]) → None
#   Sets the value of the setting.

# set_value(self: csc.update.SettingData, value: Union[bool, int], frame: int) → None
#   Sets the value of the setting at a specific frame.

# value(self: csc.update.SettingData) → Union[bool, int]
#   Gets the current value of the setting.

# value(self: csc.update.SettingData, frame: int) → Union[bool, int]
#   Gets the value of the setting at a specific frame.

# Example usage:
# Empty space here


# csc.update.SettingDataAttribute Class
# Represents an attribute of a setting. It can be connected with setting functions.

# Example usage:
# Empty space here


# csc.update.SettingFunction Class
# Represents a setting function, which operates on attributes of a setting.

# Methods:
# arguments(self: csc.update.SettingFunction) → List[csc.update.SettingFunctionAttribute]
#   Retrieves the input attributes of the setting function.

# decrease_input_vector(self: csc.update.SettingFunction, index: int) → None
#   Decreases the input vector attribute at a given index.

# func_id(self: csc.update.SettingFunction) → csc.model.SettingFunctionId
#   Retrieves the unique identifier for the setting function.

# increase_input_vector(self: csc.update.SettingFunction, index: int) → csc.update.SettingFunctionAttribute
#   Increases the input vector attribute at a given index.

# is_convertible(self: csc.update.SettingFunction) → bool
#   Checks whether this function is convertible and will be part of the resulting setting graph.

# remove_attribute(self: csc.update.SettingFunction, attribute: csc.update.SettingFunctionAttribute) → None
#   Removes the specified attribute from the input vector.

# resize_vector_inputs(self: csc.update.SettingFunction, index: int, count: int) → None
#   Resizes the input vector attribute at a given index to the specified count.

# results(self: csc.update.SettingFunction) → List[csc.update.SettingFunctionAttribute]
#   Retrieves the output attributes of the setting function.

# set_convertible(self: csc.update.SettingFunction, convertible: bool) → None
#   Sets whether this function will be used in the resulting setting graph or not.

# Example usage:
# Empty space here


# csc.update.SettingFunctionAttribute Class
# Represents an attribute of a setting function. It can be connected with setting functions or data function activeness attributes.

# Methods:
# is_out_true(self: csc.update.SettingFunctionAttribute) → bool
#   Checks if the attribute output is true.

# output_id(self: csc.update.SettingFunctionAttribute) → csc.model.SettingId
#   Retrieves the unique identifier for the attribute output.

# Example usage:
# Empty space here


# csc.update.SettingFunctionAttributeId Class
# Represents a unique identifier for a setting function attribute, defined by the SettingFunctionId and the index of the attribute.

# Properties:
# attribute_index → int
#   Gets the index of the attribute.

# attribute_sub_index → int
#   Gets the index of the attribute in the array.

# function_id → csc.model.SettingFunctionId
#   Gets the SettingFunctionId associated with the attribute.

# Example usage:
# Empty space here


# csc.update.Update Class
# Represents the entire update editor.

# Methods:
# delete_node(self: csc.update.Update, id: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) → None
#   Deletes a node in the update graph based on its identifier.

# get_node_by_id(self: csc.update.Update, id: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) → csc.update.Node
#   Retrieves a node from the update graph based on its identifier.

# get_object_by_id(self: csc.update.Update, arg0: csc.model.ObjectId) → csc.update.Object
#   Retrieves an object from the update graph based on its identifier.

# root(self: csc.update.Update) → csc.update.ObjectGroup
#   Returns the root object group of the update editor.

# ungroup(self: csc.update.Update, group: csc.update.Group) → None
#   Ungroups a group of nodes in the update editor.

# Example usage:
# This script gets the specified object by its Object ID
# import csc
#
# def run(scene):
#     mv = scene.model_viewer()
#     object_ids = mv.get_objects()
#     object_id = object_ids[0]
#
#     def mod(model, update, scene):
#         object = update.get_object_by_id(object_id)
#         print(object)
#     scene.modify_update('Get object by ID', mod)


# csc.update.UpdateGroup Class
# Represents an update group node in the update editor.

# Methods:
# create_regular_data(self: csc.update.UpdateGroup, name: str, value: Union[bool, int, float, numpy.ndarray[numpy.float32[3, 1]], csc.math.Rotation, numpy.ndarray[numpy.float32[3, 3]], numpy.ndarray[numpy.float32[4, 4]], csc.math.Quaternion, str, numpy.ndarray[bool[3, 1]]], mode: csc.model.DataMode = <DataMode.Static: 0>) → csc.update.RegularData
#   Creates a regular data node in the update group.

# create_regular_function(self: csc.update.UpdateGroup, name: str, function: str) → csc.update.RegularFunction
#   Creates a regular function node in the update group.

# create_setting_data(self: csc.update.UpdateGroup, name: str, value: Union[bool, int], mode: csc.model.SettingMode = <SettingMode.Static: 0>) → csc.update.SettingData
#   Creates a setting data node in the update group.

# create_setting_function(self: csc.update.UpdateGroup, name: str, function_name: str) → csc.update.SettingFunction
#   Creates a setting function node in the update group.

# create_sub_update_group(self: csc.update.UpdateGroup, name: str) → csc.update.UpdateGroup
#   Creates a sub-update group in the update group.

# create_sub_update_group2(self: csc.update.UpdateGroup, name: str, group_id: csc.update.GroupId) → csc.update.UpdateGroup
#   Creates a sub-update group with a specified group ID.

# external_properties(self: csc.update.UpdateGroup) → csc.update.ExternalProperties
#   Retrieves the external properties of the update group.

# groups(self: csc.update.UpdateGroup) → Set[csc.update.UpdateGroup]
#   Retrieves the set of all sub-update groups.

# regular_datas(self: csc.update.UpdateGroup) → Set[csc.update.RegularData]
#   Retrieves the set of regular data nodes in the update group.

# regular_functions(self: csc.update.UpdateGroup) → Set[csc.update.RegularFunction]
#   Retrieves the set of regular function nodes in the update group.

# setting_functions(self: csc.update.UpdateGroup) → Set[csc.update.SettingFunction]
#   Retrieves the set of setting function nodes in the update group.

# settings_datas(self: csc.update.UpdateGroup) → Set[csc.update.SettingData]
#   Retrieves the set of setting data nodes in the update group.

# Example usage:
# Empty space here
