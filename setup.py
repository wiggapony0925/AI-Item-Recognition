from cx_Freeze import setup, Executable

setup(name="object detection",
      version='0.1',
      description="open cv object detection"
      Executable=[Executable("main.py")]
      )