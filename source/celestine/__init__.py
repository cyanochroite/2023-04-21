from celestine.session import load
from celestine.session import Session

from celestine.string.all import PACKAGE
from celestine.string.all import BLENDER
from celestine.string.all import MAIN


bl_info = {
    "name": "Celestine",
    "description": "Blnder stuff can do stuff wow cool.",
    "author": "mem_dixy",
    "version": (0, 4, 0),
    "blender": (3, 0, 0),
    "location": "View 3D > Sidebar > Viewer",
    "warning": "Does not work. Work in progress. Not ready for publication.",
    "wiki_url": "https://celestine.readthedocs.io/en/latest/",
    "tracker_url": "https://github.com/mem-dixy/celestine/",
    "support": "COMMUNITY",
    "category": "3D View",
}


def register():
    """
    This is a function which only runs when enabling the add-on, this means the
    module can be loaded without activating the add-on.
    """
    load.module(PACKAGE, BLENDER, MAIN).register()
    main([BLENDER, MAIN], False)


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """
    load.module(PACKAGE, BLENDER, MAIN).unregister()


def main(argv, exit_on_error):
    """Run the main program."""
    session = Session(argv, exit_on_error)
    with session.interface.window(session) as window:
        for document in session.task.main(session):
            window.page(document)

# , . :
