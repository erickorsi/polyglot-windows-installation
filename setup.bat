:: Install dependencies
echo "Installing dependencies for polyglot..."
python -m pip install -U pip
pip3 install -U requests
python get_dependencies.py
echo "Dependencies installed."
:: Install polyglot
echo "Installing polyglot..."
git clone https://github.com/aboSamoor/polyglot.git
cd polyglot
python setup.py install
cd ..
RMDIR /S /Q %0\..\polyglot
