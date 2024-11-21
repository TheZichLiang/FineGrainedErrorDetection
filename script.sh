srun --qos=default --account=class --partition=class --gres=gpu:1 --mem=32g --time=01:00:00 bash -c "python test.py &> test.out"


Start jupyter notebook:
srun --pty --qos=default --account=class --partition=class --gres=gpu:1 --mem=32g --time=01:00:00 bash
jupyter notebook --no-browser --port=8889 --ip=0.0.0.0
ssh -N -f -L localhost:8888:tron29.umiacs.umd.edu:8889 c7230021@nexusclass.umiacs.umd.edu