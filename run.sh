FIRSTRUN=0
if [ ! -d venv ]
then
	echo 'venv not found. creating...'
    FIRSTRUN=1
	python -m venv venv
fi

. venv/bin/activate

if [[ ${FIRSTRUN} == 1 ]]
then
	echo 'installing libraries to venv'
    pip3 install -r requirements.txt
fi

python server.py $@
