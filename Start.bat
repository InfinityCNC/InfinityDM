@echo off
echo Installing required packages...

pip install discord
pip install asyncio
pip install pystyle
pip install colorama
pip install packaging
pip install requests
pip install aiohttp

echo All packages installed successfully.
echo Launching main.py...
python main.py
pause
