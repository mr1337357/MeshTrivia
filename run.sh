FIRSTRUN=0
if [ ! -d venv ]
then
    FIRSTRUN=1
	python -m venv venv
fi

. venv/bin/activate

if [[ ${FIRSTRUN} == 1 ]]
then
    pip install -r requirements.txt
fi

python server.py $@
