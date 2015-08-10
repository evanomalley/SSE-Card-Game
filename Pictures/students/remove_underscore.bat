@echo off
setlocal enabledelayedexpansion
for %%a in (*_*) do (
  set file=%%a
  ren "!file!" "!file:_=!"
)