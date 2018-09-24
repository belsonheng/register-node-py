@echo off
set ip_address_string="IPv4 Address"
for /F "tokens=1-7 delims=:" %%a in ('ipconfig ^| find "IPv4"') do (set "localIp=%%b" & goto :next)
:next
for /F "tokens=1-7 delims=:" %%a in ('ipconfig /all ^| find "Physical"') do (set "localmac=%%b" & goto :macnext)
:macnext
echo { "hostname": "%ComputerName%", "ip_address": "%localIp%", "mac_address": "%localmac%" }
