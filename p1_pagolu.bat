@ECHO OFF
IF %1==h (TYPE Readme.txt && cmd /k
)ELSE (
  python lib\project1.py %1 %2
)
