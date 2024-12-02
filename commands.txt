srun --qos=default --account=class --partition=class --gres=gpu:1 --mem=32g --time=01:00:00 bash -c "python test.py &> test.out"


Start jupyter notebook:
srun --pty --qos=default --account=class --partition=class --gres=gpu:1 --mem=32g --time=02:00:00 bash
echo "ssh -N -f -L localhost:8888:$(hostname):8889 $USER@nexusclass.umiacs.umd.edu"
jupyter notebook --no-browser --port=8889 --ip=0.0.0.0
