echo " BUILD START"
pyhton3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noimput --clear
echo " BUILD END"